For your Windows, MacOS, or Linux workstation you can follow the official [Ansible installation guidelines](https://docs.ansible.com/ansible/latest/installation_guide/index.html).

### Installing Ansible in GitHub CodeSpaces / devcontainer


```shell
$ pip3 install ansible

$ export PATH="/home/vscode/.local/bin/:$PATH"
```

### Debugging Ansible issues

A known issue within the repo-ansible generated devcontainer is a default locale configuration incompatible which is
incompatible with ansible and will result in the following error message:

```shell
$ ansible
ERROR: Ansible could not initialize the preferred locale: unsupported locale setting
```

To work around this issue you can either prefix your command, or export, the following environment variable
`LC_ALL=C.UTF-8`
