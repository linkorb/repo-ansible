For your Windows, MacOS, or Linux workstation you can follow the official [Ansible installation guidelines](https://docs.ansible.com/ansible/latest/installation_guide/index.html).

### Installing Ansible in GitHub default CodeSpaces devcontainer


```shell
$ pip3 install ansible

$ export PATH="/home/vscode/.local/bin/:$PATH"
```

### Debugging Ansible issues

#### pip3: command not found

If the container you're working in doesn't already have pip3 installed - like the default CodeSpaces devcontainer does -
and it's a Debian / Ubuntu flavoured container, run:

```shell
sudo apt-get update && sudo apt-get install -y python3-pip
```

#### error: externally-managed-environment

If you get this message when trying to install Ansible, or another Python dependency, you are probably running on a
newer Debian / Ubuntu based container. You can either pass the the `--break-system-packages` flag to each `pip3` call
or you can remove the special flag file that prevents you from running pip by running:

```shell
sudo rm /usr/lib/python3.*/EXTERNALLY-MANAGED || true
```

> [!NOTE]
> Since we use Python only for Ansible, this works well as a workaround, but if you were to run pandas, PyTorch, or
> other heavy Python library ecosystems look into alternatives like venv / pipx.

#### ERROR: Ansible could not initialize the preferred locale: unsupported locale setting

A known issue within the repo-ansible generated devcontainer is a default locale configuration incompatible which is
incompatible with ansible and will result in the above error message.

To work around this issue you can either prefix your command, or export, the following environment variable
`LC_ALL=C.UTF-8`
