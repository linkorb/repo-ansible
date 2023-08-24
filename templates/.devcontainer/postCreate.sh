#!/usr/bin/env bash

git config commit.template .devcontainer/git/linkorb_commit.template

composer config --global --auth http-basic.repo.packagist.com "$GITHUB_USER" "$PACKAGIST_TOKEN"
composer install
