#!/usr/bin/env python3

import os
import sys
import json
import re

root_directory = sys.argv[1]

def append_to_dict_key(d, key, value):
    if key not in d:
        d[key] = []
    d[key].append(value)


workflows_prefix = ".github/workflows"
search_directory = os.path.join(root_directory, workflows_prefix)
name_re = re.compile(r"\d\d-(.*?).ya?ml")
file_buckets = {}

for filename in os.listdir(search_directory):
    file_path = os.path.join(search_directory, filename)
    if os.path.isfile(file_path):
        first_two = filename[0:2]
        if first_two.isdigit() and filename[2] == '-' and int(first_two) % 10 != 0:
            bucket = first_two[0] + "0"
            root_relative_file = os.path.join(workflows_prefix, filename)
            name = re.match(r"\d\d-(.*?).ya?ml", filename).group(1)
            append_to_dict_key(file_buckets, bucket, {
                "name": name,
                "path_from_root": root_relative_file
            })


print(json.dumps(file_buckets, indent=2))
