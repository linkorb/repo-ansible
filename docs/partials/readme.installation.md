## Quick start

Ensure that Docker is installed on your system and you are using either Linux, MacOS, or WSL under Windows.

Create and configure a `repo.yaml` file for your repository. See the
[configuration table below](#short-reference-configuration) and the associated [repo.schema.yaml](repo.schema.yaml) file
for available options.

Run repo-ansible in a single project via docker:

```shell
docker run --pull always --rm -v "$PWD":/app ghcr.io/linkorb/repo-ansible:latest
```

Run repo-ansible against multiple projects via docker assuming
all target project are the only contents of the current folder:

```shell
docker run --pull always --rm \
   -w /opt/repo-ansible \
   -v $PWD:/opt/repo-ansible/workspace \
   -e REPO_ANSIBLE_SKIP_CHECKOUT=true \
   ghcr.io/linkorb/repo-ansible:latest bash -c 'ls workspace | \
   xargs -I NAME echo "NAME ansible_host=localhost" >> generated-inventory.ini && \
   uv run ansible-playbook -i generated-inventory.ini bulk-apply.yaml'
```

> [!NOTE]
> During execution your repository's' **README.md will be overwritten** with the generation rules used in repo-ansible.
> If you're running the playbook for the first time on your repository, be sure to
> review [Readme file auto-generation](#readme-file-auto-generation)

### Running repo-ansible playbooks manually

1. Python and other dependencies are managed through [uv](https://github.com/astral-sh/uv) and the [pyproject.toml](pyproject.toml) file.
2. Clone the latest version of this repository.

   ```shell
   git clone https://github.com/linkorb/repo-ansible.git /tmp/repo-ansible
   ```

3. To run repo-ansible against a single project, navigate to that target project's folder and run the following command:

   ```shell
   uv run --project /tmp/repo-ansible ansible-playbook /tmp/repo-ansible/apply.yaml
   ```

The playbook will load and validate `repo.yaml` according to the schema; then proceed to apply templates and checks to
your repository.

- [Looking for a way to apply repo-ansible across multiple repositories?](./docs/BulkOperations.md)
