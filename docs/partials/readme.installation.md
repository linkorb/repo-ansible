## Quick start

Ensure that Docker is installed on your system and you are using either Linux, MacOS, or WSL under Windows.

Create and configure a  `repo.yaml` file for your repository. Reference the
[configuration table below](#short-reference-configuration) and the associated repo.schema.yaml file.

Run repo-ansible for your project via docker:

```shell
# always pull latest version first
docker pull ghcr.io/linkorb/repo-ansible:latest
docker run --rm -v "$PWD":/app ghcr.io/linkorb/repo-ansible:latest
```

> This command will execute the repo-ansible apply.yaml in your current directory and report on the tasks
> that reported changes throughout the execution.


> [!NOTE]
> During execution your repository's' **README.md will be overwritten** with the generation rules used in repo-ansible.
> If you're running the playbook for the first time on your repository, be sure to
> review [Readme file auto-generation](#readme-file-auto-generation)

### Running repo-ansible playbooks manually

Ansible is required.
[How do I install Ansible on my system?](./docs/AnsibleInstallation.md)
[Encountered issues with Ansible execution?](./docs/AnsibleInstallation.md#Debugging-Ansible-issues)

Grab the latest version of the repository and its dependencies.

```shell
$ git clone https://github.com/linkorb/repo-ansible.git /tmp/repo-ansible

$ pip3 install jsonschema
```

**Run the playbook**


```shell
/your-repository $ ansible-playbook /tmp/repo-ansible/apply.yaml

PLAY [localhost] **************************************************************************

TASK [Gathering Facts] ********************************************************************
ok: [localhost]

...
```

The playbook will load and validate `repo.yaml` according to the schema; then proceed to apply templates and checks to
your repository.

 - [Looking for a way to apply repo-ansible across multiple repositories?](./docs/BulkOperations.md)
