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
