#!/usr/bin/env python3
import yaml
import json

import sys
import os.path

try:
  target = os.path.abspath(sys.argv[1])
except IndexError:
  sys.stderr.write('path to target repo.yaml file must be the first argument\n')
  sys.exit(1)

target_directory_name = os.path.basename(os.path.dirname(target))

defaults = {
  'name': target_directory_name,
  'description': '',
  'type': 'other',
  'codeowners': [{
    'pattern': '*',
    'owners': [
      '@joostfaassen'
    ]
  }]
}

yaml_string = yaml.dump(defaults, default_flow_style=False)

if not os.path.isfile(target):
  with open(target, 'w') as file:
    file.write(yaml.dump(defaults, default_flow_style=False))
else:
  sys.stdout.write(f'{target_directory_name} skipped!\n')
