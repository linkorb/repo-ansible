#!/usr/bin/env python3
import yaml
import json

import sys
import os.path
import pprint

from jinja2 import Environment, FileSystemLoader


def extract_properties(schema_yaml, into_list, prefix = None, required = []):
    # XXX ignore readme for now as it contains references
    ignored = ['$meta', 'readme', 'phpqa', 'php', 'docker', 'security', 'website']
    for k,v in schema_yaml.items():
      if k in ignored:
        continue

      key = (prefix + "." + k) if prefix != None else k

      if v['type'] == "object" and 'properties' in v:
        extract_properties(v['properties'], into_list, prefix = key, required=v['required'] if 'required' in v else [])
        continue

      enum = None
      if v['type'] == "array" and 'items' in v and 'enum' in v['items']: # TODO `items in v` should be fixed in schema
        enum = v['items']['enum']

      if v['type'] == "string" and 'enum' in v:
        enum = v['enum']

      into_list.append({
        'name': key,
        'type': v['type'],
        'default': v['default'] if 'default' in v else None,
        'description': v['description'] if 'description' in v else None,
        'enum': enum,
        'required': k in required
      })

    return into_list


with open('repo.schema.yaml', 'r') as file:
    schema_yaml = yaml.safe_load(file)
    properties = extract_properties(schema_yaml['properties'], [], required=schema_yaml['required'])


env = Environment(loader=FileSystemLoader('.'))


def lowercase_bools_filter(value):
    if isinstance(value, bool):
      return str(value).lower()
    return value

def display_name_filter(property):
    # display yaml hierarchy via newlines
    hierarchy = property['name'].split('.')
    name = "<br>".join(hierarchy)
    if property['required']:
      return '**' + name + '**'
    return name

env.filters['lowercase_bools'] = lowercase_bools_filter
env.filters['display_name'] = display_name_filter

template_str = '''
### Short reference configuration

> Required properties are **bolded**. YAML hierarchies are represented by newlines in the property column.
> The table is not exhaustive, only the most common properties and groups are documented in here. Refer to the
> repo.schema.yaml file for a complete overview of properties.

| Property | Default | Description |
| --- | --- | --- |{% for property in properties %}
| {{ property|display_name }} `{{ property.type }}` |
{%- if property.default is not none -%}{{ property.default|lowercase_bools }}{%- else -%}-{%- endif -%}
| {{ property.description|replace("\n", "") }} {%- if property.enum is not none -%}&nbsp; Accepted values:
{%- for value in property.enum -%} `{{ value }}`, {%- endfor -%}|{%- endif -%} |
{%- endfor -%}
'''

template = env.from_string(template_str)
rendered_template = template.render(properties=properties)

with open("docs/partials/readme.usage.after.md", "w") as f:
    f.write(rendered_template)
