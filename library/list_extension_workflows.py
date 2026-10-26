#!/usr/bin/env python3

import os
import sys
import json
import re

import yaml

root_directory = sys.argv[1]

def append_to_dict_key(d, key, value):
    if key not in d:
        d[key] = []
    d[key].append(value)

# only workflows that can be called are follow-ups; YAML 1.1 reads a bare `on` key as True
def is_callable(file_path):
    try:
        with open(file_path, encoding="utf-8") as f:
            workflow = yaml.safe_load(f)
    except (OSError, UnicodeDecodeError, yaml.YAMLError) as e:
        print(f"skipping {file_path}: {e}", file=sys.stderr)
        return False
    if not isinstance(workflow, dict):
        return False
    triggers = workflow.get('on', workflow.get(True))
    if isinstance(triggers, str):
        return triggers == 'workflow_call'
    if isinstance(triggers, (list, dict)):
        return 'workflow_call' in triggers
    return False


workflows_prefix = ".github/workflows"
search_directory = os.path.join(root_directory, workflows_prefix)
name_re = re.compile(r"(\d)(\d)-(.+)\.ya?ml")
file_buckets = {}

for filename in sorted(os.listdir(search_directory)):
    file_path = os.path.join(search_directory, filename)
    match = name_re.fullmatch(filename)
    if not match or match[2] == "0" or not os.path.isfile(file_path):
        continue
    if not is_callable(file_path):
        continue
    append_to_dict_key(file_buckets, match[1] + "0", {
        "name": match[3],
        "path_from_root": os.path.join(workflows_prefix, filename)
    })


print(json.dumps(file_buckets, indent=2))
