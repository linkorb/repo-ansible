#!/usr/bin/env python3
import yaml
import json

import sys
import os.path


def extract_defaults(schema_yaml):
    if 'default' in schema_yaml:
        return schema_yaml['default']

    if 'properties' in schema_yaml:
        collect = {}
        for v in schema_yaml['properties']:
            got = extract_defaults(schema_yaml['properties'][v])
            if got is not None:
                collect[v] = got
        return collect if len(collect) else None
    else:
        return None


# Function definition copied from pydantic.v1.utils
#
# The MIT License (MIT)
# Copyright (c) 2017 to present Pydantic Services Inc. and individual contributors.
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
def deep_update(mapping, *updating_mappings):
    updated_mapping = mapping.copy()
    for updating_mapping in updating_mappings:
        for k, v in updating_mapping.items():
            if k in updated_mapping and isinstance(updated_mapping[k], dict) and isinstance(v, dict):
                updated_mapping[k] = deep_update(updated_mapping[k], v)
            else:
                updated_mapping[k] = v
    return updated_mapping

with open('repo.schema.yaml', 'r') as file:
    schema_yaml = yaml.safe_load(file)
    defaults = extract_defaults(schema_yaml)

if not os.path.isfile(sys.argv[1]):
    sys.stderr.write(f'{sys.argv[1]} file not found!')
    sys.exit(1)

with open(sys.argv[1], 'r') as file:
    repo_yaml = yaml.safe_load(file)

print(json.dumps(deep_update(defaults,repo_yaml), indent=2))
