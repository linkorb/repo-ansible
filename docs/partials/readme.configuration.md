## Get Started

### Configure

The playbook depends on the `repo.yml` configuration file which must reside at the root of your repository.
This configuration let's you define variables that are used throughout generation of repository files, workflows,
and in general standardisation across the organization repositories.

For example, you use `repo.yml` to define your projects repository name, description, license, visibility, code owners,
etc.

For all the options and switches, please refer to the JSON Schema definition of the configuration file:
[repo.schema.yaml](/repo.schema.yaml).

 - [Looking for repo.yaml schema integration within your IDE?](/docs/SchemaIDESupport.md)

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
