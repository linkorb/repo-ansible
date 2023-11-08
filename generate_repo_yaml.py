#!/usr/bin/env python3


# THIS SCRIPT MUST NOT BE RELIED UPON as it's only intended for the generation
# of initial repo.yaml files when running bulk operations, by the users that deal
# with bulk repository operations, and will be removed in followup pull-requests.


import yaml
import json

import sys
import os.path
import hashlib


def detect_license(in_directory):
  name = os.path.basename(in_directory)

  license_file = in_directory + '/LICENSE'

  # fallback to LICENSE.md as some repositories seem to use this convention
  license_file = license_file if os.path.isfile(license_file) else (in_directory + '/LICENSE.md')

  if os.path.isfile(license_file):

    with open(license_file, 'r') as file:

      first_line = file.readline().strip().lower()
      second_line = file.readline().strip().lower()

      if "mit license" in first_line:
        return 'mit'

      if "gnu general public license" in first_line and "version 3" in second_line:
        return "gpl-v3"

      if "gnu lesser general public license" in first_line and "version 3" in second_line:
        sys.stderr.write(f'{name}\t\t LGPL license\n')
        return None


  composer_json = in_directory + '/composer.json'

  if os.path.isfile(composer_json):

    with open(composer_json, 'r') as file:

      composer = json.load(file)

      if composer.get("license") is not None:
        composer_license = composer.get("license").lower()

        if 'mit' == composer_license:
          return 'mit'

        if 'isc' == composer_license:
          sys.stderr.write(f'{name}\t\t ISC license\n')
          return None

        if 'bsd' == composer_license:
          sys.stderr.write(f'{name}\t\t BSD license\n')
          return None

        if 'proprietary' == composer_license:
          return 'proprietary'


  package_json = in_directory + '/package.json'

  if os.path.isfile(package_json):

    with open(package_json, 'r') as file:

      package = json.load(file)

      if package.get("license") is not None:
        package_license = package.get("license").lower()

        if 'mit' == package_license:
          return 'mit'

        if 'isc' == package_license:
          sys.stderr.write(f'{name}\t\t ISC license\n')
          return None

        if 'bsd' == package_license:
          sys.stderr.write(f'{name}\t\t BSD license\n')
          return None

        if 'proprietary' == package_license:
          return 'proprietary'


  return None



for directory in os.listdir('workspace'):
  in_directory = os.path.abspath('workspace/' + directory)

  target = in_directory + '/repo.yaml'

  defaults = {
    'name': directory,
    'description': '',
    'type': 'other',
    'codeowners': [{
      'pattern': '*',
      'owners': [
        '@joostfaassen'
      ]
    }],
    'readme': {
      'enable_generation': False
    }
  }

  if not os.path.isfile(target):
    license = detect_license(in_directory)

    if license is None:
      print(f'{directory}\t\t no/invalid license, skipping repo.yaml generation')

    else:
      defaults["license"] = license
      yaml_string = yaml.dump(defaults, default_flow_style=False)

      with open(target, 'w') as file:
        file.write(yaml_string)

  else:
    sys.stdout.write(f'{directory}\t\t repo.yaml already exists\n')
