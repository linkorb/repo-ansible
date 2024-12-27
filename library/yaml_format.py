#!/usr/bin/env python3

import yaml
import sys

# https://stackoverflow.com/questions/45004464/yaml-dump-adding-unwanted-newlines-in-multiline-strings
yaml.SafeDumper.org_represent_str = yaml.SafeDumper.represent_str

# Represent strings as multiline within YAML file, if the string contains the newline character
def repr_str(dumper, data):
    if '\n' in data:
        return dumper.represent_scalar(u'tag:yaml.org,2002:str', data, style='|')
    return dumper.org_represent_str(data)


yaml.add_representer(str, repr_str, Dumper=yaml.SafeDumper)


file_path = sys.argv[1]
with open(file_path, 'r') as file:
    document = file.read()

structure = yaml.safe_load(document)
with open(file_path, 'w') as file:
  yaml.safe_dump(structure, file)
