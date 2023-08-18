repo-ansible
============

An ansible playbook with templated configuration to apply to all LinkORB code repositories.

## Installation

* Ensure [ansible](https://www.ansible.com/) is installed
* Ensure [GitHub cli](https://cli.github.com/) is installed. *Only required for bulk operations via repo-ansible:
repository inventory generation, bulk operations (playbook-all.yaml).*
* Ensure you have a local copy of this repository somewhere on your system

## Configuration

The playbook is configured using a `repo.yml` file in the root of your repository.

This configuration let's you define variables that are used throughout the playbook and it's templates. For example, the `repo.yml` defines the name, license and visibility of your repository, the Docker base image to use.

Please refer to [repo.schema.yaml](repo.schema.yaml) for the schema of this file.

## Usage

```sh
pip3 install -r requirements.txt
cd path/to/my-application-repo
ansible-playbook path/to/repo-ansible/playbook-cwd.yaml
```

The playbook will:

1. load the `repo.yaml` file in the root of your repository
2. validate it against the `repo.schema.yaml` file in this repository
3. start applying templates and checks to your repository


## Bulk operations

The repository contains playbooks that can operate across multiple repositories at once (eg `playbook-all.yaml`).

These types of bulk operations require an inventory file that makes up the "hosts" upon which it should operate. In this
context the hosts are the names of the repositories, which should be in an automatic fashion: checked out, modified per
their `repo.yaml` configuration file, and push these changes upstream.

> **Note** the GitHub terminal client needs to be installed for inventory generation, push, pull-request operations.

In order to generate an inventory across all the linkorb repositories you have access to, the following command can be
used (an arbitrarily large limit of 1000 results was chosen so it works for all possible users):

```shell
gh search repos --owner=linkorb --limit=1000 \
  --json name --jq '.[] | .name + " ansible_host=localhost"' \
  | tee generated-inventory.ini
```

> **Note** `generated-inventory.ini` is part of `.gitignore` to avoid accidental commits of the file.

> An entry within the inventory is of the form `REPOSITORY_NAME ansible_host=localhost`, hence why jq is used to
> concatenate the string for each result returned from `gh repos` command.

After the inventory is generated you can selectively run the playbooks defined within this repository. For example you
could check them all out within the `./workspace/` directory (by default) using:

```shell
ansible-playbook -i generated-inventory.ini playbook-checkout.yaml
```

> **Note** `./workspace` is part of `.gitignore` to avoid accidental commits of checkout repositories.

> If you'd like to checkout the repositories in a different directory, specify an absolute directory path via the
> `REPO_ANSIBLE_BASE_PATH` environment variable.

## Improvements

If `repo-ansible` generates configuration that is sub-optimal, you can add a configuration option (in `repo.schema.yaml) to improve the logic, or to disable a certain template or check.

## TODO

- [ ] Add configuration options to disable Docker related content for non-applications
- [ ] Add code quality config files for phpcs, phpstan, psalm, phpmd, etc.
- [ ] Add consistency checks for `composer.json`, `package.json`, etc to validate that name, license, etc are consistent with `repo.yml`
- [ ] Improve the README.md template to conditionally include sections about doctrine, fixtures, etc
- [ ] Improve configuration to support non-PHP repositories
- [ ] Generate configuration documentation from .env.yaml if it exists
- [ ] Refactor checks for CI
- [ ] Add bulk-repo operations to pull/fetch, apply and push changes to all repositories in a given organization


## Notes

### Dependencies security

Organization-wide Dependabot alerts and pull requests are enabled for security vulnerabilities. Initially this
repository generated a separate `dependabot.yaml` configuration file which would have served the same purpose as the
global organization-wide settings.

## Brought to you by the LinkORB Engineering team

<img src="http://www.linkorb.com/d/meta/tier1/images/linkorbengineering-logo.png" width="200px" /><br />
Check out our other projects at [linkorb.com/engineering](http://www.linkorb.com/engineering).
By the way, we're hiring!
