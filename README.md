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
