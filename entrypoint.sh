#!/bin/bash
set -e

# Check if repo.yaml exists in /app
if [ ! -f /app/repo.yaml ]; then
  echo "repo.yaml not found in the current directory."
  exit 1
fi

# Run the Ansible playbook
ansible-playbook /opt/repo-ansible/playbook-cwd.yaml