## Quick start

Ensure that python is installed on your system and you are using either Linux, MacOS, or WSL under Windows.

Create and configure a  `repo.yaml` file for your repository. Reference the
[configuration table below](#short-reference-configuration) and the associated repo.schema.yaml file.

Run repo-ansible, from your repository folder run the following commands:

```shell
curl -L -o /tmp/repo-ansible.run https://github.com/linkorb/repo-ansible/releases/latest/download/repo-ansible.run
chmod +x /tmp/repo-ansible.run
/tmp/repo-ansible.run
```

> This command will install Ansible for you, install the associated dependencies and run the bundled playbook
> (playbook-cwd.yaml) for your repository taking in account the repo.yaml configuration file.


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

$ pip3 install -r /tmp/repo-ansible/requirements.txt
```

**Run the playbook**


```shell
/your-repository $ ansible-playbook /tmp/repo-ansible/playbook-cwd.yaml

PLAY [localhost] **************************************************************************

TASK [Gathering Facts] ********************************************************************
ok: [localhost]

...
```

The playbook will load and validate `repo.yaml` according to the schema; then proceed to apply templates and checks to
your repository.

 - [Looking for a way to apply repo-ansible across multiple repositories?](./docs/BulkOperations.md)
