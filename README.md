<!-- Managed by https://github.com/linkorb/repo-ansible. Manual changes will be overwritten. -->

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


### Short reference configuration

> Required properties are **bolded**. YAML hierarchies are represented by newlines in the property column.
> The table is not exhaustive, only the most common properties and groups are documented in here. Refer to the
> repo.schema.yaml file for a complete overview of properties.

| Property | Default | Description |
| --- | --- | --- |
| version `string` |-| Version of compatible repo-ansible release. Automatically updated during repo-ansible runs.|
| **name** `string` |-| The git repository name.|
| **description** `string` |-| Repository description that shows up in the sidebar on GitHub, and as the first line of the README after the repository name.|
| **type** `string` |-| Classification of repository type. Influences what additional files repo-ansible will generate when run.<br>The last 3 listed types have been deprecated and should not be used on new projects.&nbsp; Accepted values:`php-web`,`php-library`,`php-cli`,`nodejs-web`,`nodejs-library`,`nodejs-cli`,`other`,`application`,`library`,`symfony-bundle`,||
| **codeowners** `array` |-| Each array item contains a file/directory pattern and an array of individuals or teams responsible for reviewing and maintaining files/directories that match the specified pattern. For a list of allowed patterns, refer to [CODEOWNERS syntax](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).|
| license `string` |proprietary| Repository license&nbsp; Accepted values:`mit`,`gpl-v3`,`proprietary`,||
| license_year `number` |-| Year when the license was applied to the repository. Used with the MIT license, as it includes the year as part of the generated LICENSE file. Defaults to current year if not set.|
| visibility `string` |private| GitHub repository visibility.&nbsp; Accepted values:`public`,`private`,||
| lifecycle `string` |-| Project lifecycle stage.&nbsp; Accepted values:`dev-research`,`dev-prod-bound`,`dev-prod`,`dev-maintenance`,`deprecated-prod`,`archived`,||
| user_scope `array` |-| Additional project classification in terms of users served.&nbsp; Accepted values:`external-customer-facing-app`,`internal-team-facing-app`,`enables-external-customer-facing-apps`,`enables-internal-team-facing-apps`,`internal-devops-tooling`,||
| github<br>topics `array` |-| GitHub topics. An array of strings.|
| github<br>default_branch `string` |main| Default branch configuration in GitHub (default main). Override for older repositories that still use master branch. Consider updating your repository to include a main branch and remove this option.|
| github<br>workflows<br>review `boolean` |true| The review workflow will trigger for pull requests and will check if the commit messages conform with conventional commits, and if cards are referenced as part of the commit message.|
| github<br>features<br>dependabot_auto_merge `boolean` |true| Generate workflow that automatically merges Dependabot PRs for patch and minor version releases.<br> *Note that merging the PR won't automatically trigger other followup workflows.*|
| github<br>features<br>downloads `boolean` |true| Enable repository downloads.|
| github<br>features<br>squash_merge `boolean` |true| Allow squash-merging pull requests.|
| github<br>features<br>merge_commit `boolean` |true| Allow merging pull requests with merge commit.|
| github<br>features<br>rebase_merge `boolean` |true| Allow rebase-merging pull requests.|
| github<br>features<br>sdlc_workflows `boolean` |false| **EXPERIMENTAL** Software Development Lifecycle Workflows. Property will likely be removed in the future, and enabled by default, when workflows have been stabilized.|
| github<br>features<br>wiki `boolean` |false| Enable Wiki tab.|
| github<br>features<br>issues `boolean` |false| Enable issues tab.|
| github<br>features<br>projects `boolean` |false| Enable projects tab.|
| github_workflows<br>build<br>extra_docker_build_args `object` |{}| Key-value pairs to use as build args during the docker build step of build and release workflow|
| github_workflows<br>release<br>commit_changed_files `array` |[]| A list of files in addition to CHANGELOG.md and package.json (for repo.type starting with `nodejs-`) to include in the commit with changes.|
| github_workflows<br>release<br>issue_url_format `string` || Override the base URL for the issues mentioned with conventional-commits. Use {{id}} for the issue ID, as well other placeholders mentioned in https://github.com/conventional-changelog/conventional-changelog-config-spec/blob/master/versions/2.2.0/README.md#substitutions|
| reviewdog<br>platforms `array` |[]| A broad way to categorize programming languages, libraries, and frameworks, and for which we have an external tool we can use to assure code quality during review.&nbsp; Accepted values:`php`,`twig`,||
| devcontainer<br>custom_docker_compose_yaml `boolean` |false| When enabled the compose file located at .devcontainer/docker-compose.yaml will no longer get automatically updated. Allowing users to customize their docker-compose setup.|
| devcontainer<br>postCreateCommand `string` |-| Additional (shell) commands to run when the containers is created. For a typical project you would specify commands that only need to run once when the project is setup. For example you might add a command in here to load database fixtures for your project.|
| devcontainer<br>postStartCommand `string` |-| Additional (shell) commands to run when the container is started. This event takes place after the create event, but opposed to the create event it's triggered every time the container is started (including when it's resumed from a suspended state). In a typical JavaScript application you might set it to run a `npm run dev` or equivalent step.|
| devcontainer<br>customizations_vscode<br>extensions `array` |-| Additional extensions to install. Refer to the [group_vars/all.yaml](group_vars/all.yaml) file for extensions installed by default.|
| devcontainer<br>customizations_vscode<br>settings `object` |-| Settings overrides for VSCode and installed extensions. Refer to the [group_vars/all.yaml](group_vars/all.yaml) file regarding proper format and default values.|
| devcontainer<br>private_packagist `boolean` |true| Repository requires private packagist access. Property is ignored is not of type php-*, or the other (deprecated) types: application, library, symfony-bundle.|
| devcontainer<br>repository `string` |ghcr.io/linkorb/php-docker-base| Image to use for devcontainer (registry image URL)|
| devcontainer<br>tag `string` |php8-review| Image tag|
| archived `boolean` |false| Setting this option to `true` will cause the repository to be archived. Once archived, it can only be unarchived manually.|
| omit_files `array` |[]| **EXPERIMENTAL** A list of files to skip during file generation.|
 - [Looking for repo.yaml schema integration within your IDE?](./docs/SchemaIDESupport.md)

### Readme file auto-generation

The content for each section of this README was either retrieved from `repo.yaml` or Markdown partials stored in the
`docs/partials` folder. Managing content in this way allows you to define repo-specific content in
`repo.yaml` and within the `/docs/partials` folder as Markdown partials.

For example, if you define `readme.usage.content` in `repo.yaml`, but a Markdown file named `readme.usage.md` exists
in the `/docs` folder, the dynamic README inserts the Markdown content.

To make this possible, tasks defined in `retrieve-docs-data.yaml` retrieve the docs files data such as the filename
and path for each Markdown file so `README.md.j2` can check for the presence of Markdown files for each README section
and insert Markdown content if there is a match.


## Contributing

We welcome contributions to make this repository even better. Whether it's fixing a bug, adding a feature, or improving documentation, your help is highly appreciated. To get started, fork this repository then clone your fork.

Be sure to familiarize yourself with LinkORB's [Contribution Guidelines](/CONTRIBUTING.md) for our standards around commits, branches, and pull requests, as well as our [code of conduct](/.github/CODE_OF_CONDUCT.md) before submitting any changes.

If you are unable to implement changes you like yourself, don't hesitate to open a new issue report so that we or others may take care of it.
## Brought to you by the LinkORB Engineering team

<img src="http://www.linkorb.com/d/meta/tier1/images/linkorbengineering-logo.png" width="200px" /><br />
Check out our other projects at [linkorb.com/engineering](http://www.linkorb.com/engineering).
By the way, we're hiring!
