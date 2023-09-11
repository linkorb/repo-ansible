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