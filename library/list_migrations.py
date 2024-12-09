#!/usr/bin/env python3

import sys
import os
import re
import json

version_string = sys.argv[1]
version_parts = version_string[1:].split('.')

input_version = tuple(map(int, version_parts))

def extract_version_string(filename):
  return filename.split('-')[1][0:-5] # drop ".yaml" suffix

def migration_version(filename):
  version_part = extract_version_string(filename)[1:].split('.')[0:3]  # drop "v" prefix

  return tuple(map(int, version_part))

def greater(version_source, version_target):
  if version_source[0] > version_target[0]:
    return True
  if version_source[0] < version_target[0]:
    return False

  if version_source[1] > version_target[1]:
    return True
  if version_source[1] < version_target[1]:
    return False

  if version_source[2] > version_target[2]:
    return True
  if version_source[2] < version_target[2]:
    return False
  
  # Returns true when versions are equal. This allows us to pin a migration to an existing
  # version (latest), instead of having to guess the next version number when writing a
  # repo-ansible migration file.
  return True

pattern = re.compile(r"-v\d+\.\d+\.\d+\.yaml$")
def is_migration(filename):
  return pattern.search(filename) is not None


directory = './tasks/migrations/'
files = [f for f in os.listdir(directory)
           if os.path.isfile(os.path.join(directory, f))
              and is_migration(f)
              and greater(migration_version(f), input_version)]

migrations = []
for i in files:
  migrations.append({
    'version': extract_version_string(i),
    'filename': i
  })

print(json.dumps(migrations, indent=2))
