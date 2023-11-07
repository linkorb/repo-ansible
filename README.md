<!-- Managed by https://github.com/linkorb/repo-ansible. Manual changes will be overwritten. -->
repo-ansible
============

An ansible playbook with templated configuration to apply to all LinkORB code repositories.



## Installation

### Install Ansible

To install Ansible, follow the general steps outlined in the [Ansible installation guidelines](https://docs.ansible.com/ansible/latest/installation_guide/index.html), tailored to your operating system.

### Optional: Install Ansible in GitHub codespaces

GitHub Codespaces typically provides a Linux-based environment (usually Ubuntu or a similar distribution). In such an environment, you may run the following commands to install Ansible:

```shell
# Refresh the package lists
sudo apt update
# Install Python packages
sudo pip install ansible
# Verify installation
ansible --version
```

### Install Python package dependencies

Run the following command to install the Python packages listed in the `requirements.txt` file:

```shell
pip3 install -r requirements.txt
```

### Optional: Install tools for bulk operations

Install [GitHub CLI](https://cli.github.com/) and [jq](https://jqlang.github.io/jq/) for the ability to generate repository inventory files and perform [bulk operations](#perform-bulk-operations) using playbooks (e.g. playbook-all.yaml).

### Take it for a spin!

Now that you have set up the project, [run your first playbook](#run-a-playbook).
## Configuration 

### Define playbook variables in `repo.yaml`

Define playbook variables within `repo.yaml` in the root of your repository.

This configuration file allows you to define variables used throughout the playbook and its templates. For example, the `repo.yaml` defines the `name`, `license`, and `visibility` of your repository, and the Docker base image to use.

Please refer to [repo.schema.yaml](repo.schema.yaml) to view this project's schema.

### Define README docs section content

The content for each section of this README was either retrieved from `repo.yaml` or Markdown partials stored in the `docs/partials` folder. Managing content in this way allows you to centrally define documentation in `repo.schema.yaml` inherited by each affected codebase while also allowing you to define repo-specific content in `repo.yaml` and within the `/docs/partials` folder as Markdown partials.

When a playbook generates the README, it checks for Markdown partials in the `/docs` folder. If present, they override repo-specific content defined in `repo.yaml` or content inherited from `repo.schema.yaml` defaults. 

For example, if you define `readme.usage.content` in `repo.yaml`, but a Markdown file named `readme.usage.md` exists in the `/docs` foder, the dynamic README inserts the Markdown content.

To make this possible, tasks defined in `retrieve-docs-data.yaml` retrieve the docs files data such as the filename and path for each Markdown file so `README.md.j2` can check for the presence of Markdown files for each README section and insert Markdown content if there is a match.

### Customization

If `repo-ansible` generates a sub-optimal configuration, you can add a configuration option (in `repo.schema.yaml`) to improve the logic or to turn off a certain template or check.

## Usage

### Run a playbook

From the root of your project, run the following commands to execute a playbook:

```sh
ansible-playbook playbook-cwd.yaml
```

The playbook will:

1. Load the `repo.yaml` file to the root of your repository.
2. Validate it against this repository's `repo.schema.yaml` file.
3. Start applying templates and checks to your repository.

### Perform bulk operations

The repository contains playbooks that can simultaneously operate across multiple repositories (e.g., `playbook-all.yaml`).

These bulk operations require an inventory file that makes up the "hosts" upon which it should operate. In this
context, the hosts are the names of the repositories, which should be in an automatic fashion: checked out, modified per
their `repo.yaml` configuration file, and push these changes upstream.

#### Generate an inventory

> **Note** the GitHub terminal client must be installed for inventory generation, push, and pull request operations.

To generate an inventory across all the linkorb repositories you have access to, the following command can be
used (an arbitrarily large limit of 1000 results was chosen so it works for all possible users):

```shell
gh search repos --owner=linkorb --limit=1000 \
  --archived=false \
  --json name,defaultBranch \
  --jq '.[] | .name + " default_branch=" + .defaultBranch + " ansible_host=localhost"' \
  | tee generated-inventory.ini
```

> **Note** `generated-inventory.ini` is part of `.gitignore` to avoid accidental file commits.

> An entry within the inventory is of the form `REPOSITORY_NAME default_branch=DEFAULT_BRANCH ansible_host=localhost`

#### Run a playbook in bulk

You can selectively run the playbooks defined within this repository. For example you
could check them all out within the `./workspace/` directory (by default) using:

```shell
ansible-playbook -i generated-inventory.ini playbook-checkout.yaml
```

> **Note** `./workspace` is part of `.gitignore` to avoid accidental commits of checkout repositories.

> If you'd like to checkout the repositories in a different directory, specify an absolute directory path via the
> `REPO_ANSIBLE_BASE_PATH` environment variable.

The changes can be committed back upstream using either pull requests or directly pushing a commit into the
default branch. Via specific playbooks:

```shell
ansible-playbook -i generated-inventory.ini playbook-pull-request.yaml
```

```shell
ansible-playbook -i generated-inventory.ini playbook-push.yaml
```

Alternatively, when `playbook-all.yaml` is executed, the `REPO_ANSIBLE_CHANGES` environment variable can be set to
either `pull-request`, or `push` to invoke the desired commit path to be taken (by default, this step is skipped).

#### Bulk apply across repositories and create pull requests with changes

```shell
REPO_ANSIBLE_CHANGES=pull-request \
  ansible-playbook -i generated-inventory.ini playbook-all.yaml
```
## Dependencies security

Organization-wide Dependabot alerts and pull requests are enabled for security vulnerabilities. Initially this
repository generated a separate `dependabot.yaml` configuration file which would have served the same purpose as the
global organization-wide settings.


## Brought to you by the LinkORB Engineering team

<img src="http://www.linkorb.com/d/meta/tier1/images/linkorbengineering-logo.png" width="200px" /><br />
Check out our other projects at [linkorb.com/engineering](http://www.linkorb.com/engineering).
By the way, we're hiring!
