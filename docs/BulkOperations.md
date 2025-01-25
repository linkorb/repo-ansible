
The repository contains the bulk-apply playbook that can simultaneously operate across multiple repositories.

These bulk operations require an inventory file that makes up the "hosts" upon which it should operate. In this
context, the hosts are the repository names, which will be: checked out, modified per
their `repo.yaml` configuration file, and commited back upstream.

**Install the [GitHub CLI](https://cli.github.com/) and [jq](https://jqlang.github.io/jq/) dependencies.**

#### Generate an inventory

To generate an inventory across all the linkorb repositories you have access to, the following command can be
used (an arbitrarily large limit of 1000 results was chosen so it works for all possible users):

```shell
gh search repos --owner=linkorb --limit=1000 \
  --archived=false \
  --json name \
  --jq '.[] | .name + " ansible_host=localhost"' \
  | tee generated-inventory.ini
```

> **Note** `generated-inventory.ini` file is part of `.gitignore` to avoid accidental file commits.

> An entry within the inventory follows the form `REPOSITORY_NAME ansible_host=localhost`


#### Bulk apply repo-ansible


```shell
ansible-playbook -i generated-inventory.ini bulk-apply.yaml
```

#### Running select sections of bulk-apply.yaml

For example you can check out all repositories defined in the inventory to the `./workspace/` directory using:

```shell
ansible-playbook -i generated-inventory.ini \
  --tags checkout bulk-apply.yaml
```

> [!NOTE]
> `./workspace` is part of `.gitignore` to avoid accidental commits of checkout repositories.

> If you'd like to checkout the repositories in a different directory, specify an absolute directory path via the
> `REPO_ANSIBLE_BASE_PATH` environment variable.

The changes can be committed back upstream using either pull requests or directly pushing a commit into the
default branch.

```shell
ansible-playbook -i generated-inventory.ini \
  --tags commit-changes -e changes=pull-request bulk-apply.yaml
```

```shell
ansible-playbook -i generated-inventory.ini \
  --tags commit-changes -e changes=push bulk-apply.yaml
```

Alternatively, when `bulk-apply.yaml` is executed, the `REPO_ANSIBLE_CHANGES` environment variable can be set to
either `pull-request`, or `push` to invoke the desired commit path to be taken (by default, this step is skipped).

#### Bulk apply across repositories and create pull requests with changes

```shell
REPO_ANSIBLE_CHANGES=pull-request \
  ansible-playbook -i generated-inventory.ini bulk-apply.yaml
```
