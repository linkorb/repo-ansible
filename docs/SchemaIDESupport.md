## VSCode

VSCode requires the following extension in order to support JSON Schema definitions
via YAML `JSON YAML Schema Selector` (identifier `74th.json-yaml-schema-selector`)

Setup:

 - **File** -> **Preferences** -> **Settings** -> **Extensions** -> **JsonYamlSchemaSelector**
 - **Edit in settings.json**
 - Add the following entry
   ```json
    "yaml.schemas": {
        "https://raw.githubusercontent.com/linkorb/repo-ansible/main/repo.schema.yaml": ["repo.yaml"]
    }
   ```

## JetBrains IDEs

By default JetBrains' IDEs support JSON Schemas defined via YAML.

Setup:

 - **File** -> **Settings** -> **JSON Schema Mappings**
 - **Add**
 - **Schema file or URL** `https://raw.githubusercontent.com/linkorb/repo-ansible/main/repo.schema.yaml`
 - **Schema version** `JSON Schema Version 7`
 - **Add mapping** `File: repo.yaml`
