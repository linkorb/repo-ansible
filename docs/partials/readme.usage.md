### Install repo-ansible and its dependencies

Ansible is required.
[How do I install Ansible on my system?](./docs/AnsibleInstallation.md)
[Encountered issues with Ansible execution?](./docs/AnsibleInstallation.md#Debugging-Ansible-issues)

Grab the latest version of the repository and its dependencies.

```shell
$ git clone https://github.com/linkorb/repo-ansible.git /tmp/repo-ansible

$ pip3 install -r /tmp/repo-ansible/requirements.txt
```

### Run the playbook

> [!NOTE]
> During execution your repository's' **README.md will be overwritten** with the generation rules used in repo-ansible.
> If you're running the playbook for the first time on your repository, be sure to
> *Review README.md file auto-generation, switches and rules* ↑


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
