## Configuration 

### Define playbook variables in `repo.yaml`

Define playbook variables within `repo.yaml` in the root of your repository.

This configuration file allows you to define variables used throughout the playbook and its templates. For example, the `repo.yaml` defines the `name`, `license`, and `visibility` of your repository, and the Docker base image to use.

Please refer to [repo.schema.yaml](repo.schema.yaml) to view this project's schema.

### Define README docs section content

The content for each section of this README was either retrieved from `repo.yaml` or Markdown partials stored in the `docs/partials` folder. Managing content in this way allows you to centrally define documentation in `repo.schema.yaml` inherited by each affected codebase while also allowing you to define repo-specific content in `repo.yaml` and within the `/docs/partials` folder as Markdown partials.

When a playbook generates the README, it checks for Markdown partials in the `/docs` folder. If present, they override repo-specific content defined in `repo.yaml` or content inherited from `repo.schema.yaml` defaults. 

For example, if you define `readme.usage.content` in `repo.yaml`, but a Markdown file named `readme.usage.md` exists in the `/docs` foder, the dynamic README inserts the Markdown content.

To make this possible, tasks defined in `retrieve-docs-data.yaml` retrieve the docs files data such as the filename and path for each Markdown file so `README.md.j2` can check for the presence of Markdown files for each README section and insert Markdown content if there is a match.

### Customization

If `repo-ansible` generates a sub-optimal configuration, you can add a configuration option (in `repo.schema.yaml`) to improve the logic or to turn off a certain template or check.