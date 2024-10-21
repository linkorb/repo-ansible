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
