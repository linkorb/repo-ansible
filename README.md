<!-- Managed by https://github.com/linkorb/repo-ansible. Manual changes will be overwritten. -->
repo-ansible
============

Ansible playbooks with templated configuration to apply to all LinkORB code repositories.

What benefits do you get from using repo-ansible for your repository?

 - **CodeSpace devcontainers**<br>
   LAMP-based devcontainer with Apache, MariaDB and a phpMyAdmin.
 - **automated security and dependency updates via Dependabot**<br>
   Organization-wide settings ensure security alerts and pull requests are enabled for all repositories,
   and repo-ansible, doubles down on this configuration, makes sure that security and minor version updates
   created by Dependabot will automatically get merged.
 - **Contributors support**<br>
   Community guidelines, contributing notes, git hooks, codeowners for automated PR assignment, QA tooling/configuration,
   and the standardized LinkORB pull request template.
 - **Standardized repository files, GitHub repository management, and much more to come!**




## Get Started

### Configure

The playbook depends on the `repo.yml` configuration file which must reside at the root of your repository.
This configuration let's you define variables that are used throughout generation of repository files, workflows,
and in general standardisation across the organization repositories.

For example, you use `repo.yml` to define your projects repository name, description, license, visibility, code owners,
etc.

For all the options and switches, please refer to the JSON Schema definition of the configuration file:
[repo.schema.yaml](repo.schema.yaml).

 - [Looking for repo.yaml schema integration within your IDE?](./docs/SchemaIDESupport.md)

<details>
<summary>Review README.md file auto-generation, switches and rules</summary>

#### Define README docs section content

The content for each section of this README was either retrieved from `repo.yaml` or Markdown partials stored in the
`docs/partials` folder. Managing content in this way allows you to centrally define documentation in
`repo.schema.yaml` inherited by each affected codebase while also allowing you to define repo-specific content in
`repo.yaml` and within the `/docs/partials` folder as Markdown partials.

When a playbook generates the README, it checks for Markdown partials in the `/docs` folder. If present, they override
repo-specific content defined in `repo.yaml` or content inherited from `repo.schema.yaml` defaults.

For example, if you define `readme.usage.content` in `repo.yaml`, but a Markdown file named `readme.usage.md` exists
in the `/docs` foder, the dynamic README inserts the Markdown content.

To make this possible, tasks defined in `retrieve-docs-data.yaml` retrieve the docs files data such as the filename
and path for each Markdown file so `README.md.j2` can check for the presence of Markdown files for each README section
and insert Markdown content if there is a match.
</details>

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

## Contributing

We welcome contributions to make this repository even better. Whether it's fixing a bug, adding a feature, or improving documentation, your help is highly appreciated. To get started, fork this repository then clone your fork.

Be sure to familiarize yourself with LinkORB's [Contribution Guidelines](/CONTRIBUTING.md) for our standards around commits, branches, and pull requests, as well as our [code of conduct](/CODE_OF_CONDUCT.md) before submitting any changes.

If you are unable to implement changes you like yourself, don't hesitate to open a new issue report so that we or others may take care of it.
## Brought to you by the LinkORB Engineering team

<img src="http://www.linkorb.com/d/meta/tier1/images/linkorbengineering-logo.png" width="200px" /><br />
Check out our other projects at [linkorb.com/engineering](http://www.linkorb.com/engineering).
By the way, we're hiring!
