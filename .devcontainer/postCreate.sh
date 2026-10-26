#!/usr/bin/env bash
# Managed by https://github.com/linkorb/repo-ansible. Manual changes will be overwritten.

# This is a workaround on an issue with the devcontainer reported on Windows where followup git config commands would
# fail. #9067
git config --global --add safe.directory /app

git config commit.template .devcontainer/git/linkorb_commit.template

composer config --global --auth http-basic.repo.packagist.com \
  "${GITHUB_USER:-$GITHUB_USER_ON_HOST}" "${PACKAGIST_TOKEN:-$PACKAGIST_TOKEN_ON_HOST}"

