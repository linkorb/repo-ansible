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

### README status badges

Generated READMEs gain status badges only when the target project's `repo.yaml` opts in. Leave the keys unset to keep the README unchanged. `coverage` defaults to false.

```yaml
readme:
  badges:
    tests: unit-tests.yml   # filename under .github/workflows
    coverage: true          # boolean, default false
```

`tests` is the workflow filename only, including the extension. Letters, digits, `.`, `_`, and `-` are allowed. When it is set, the README renders a Tests badge on the same row as the Release badge:

```markdown
[![Tests](https://github.com/linkorb/NAME/actions/workflows/FILENAME/badge.svg?branch=DEFAULT)](https://github.com/linkorb/NAME/actions/workflows/FILENAME)
```

`DEFAULT` is `github.default_branch`, or `main` when that value is absent. The `branch` query keeps the badge on the default branch. The badge is a normal GitHub Actions badge, so it is visible to anyone who can already see the repository. If `.github/workflows/FILENAME` is missing, the playbook fails with the missing path. When `tests` is omitted, repo-ansible does not check for a workflow file and does not render the badge.

The Release badge is unchanged. It is still rendered only when `type` is not `other` and `github.features.sdlc_workflows` is true.

`coverage` adds a relative image:

```markdown
![Coverage](./.github/badges/coverage.svg)
```

Each repository's CI publishes `.github/badges/coverage.svg`. repo-ansible leaves that file alone, so a later run does not replace the percentage. Until the first publish, the image can be missing. An Actions badge is only pass or fail, and `raw.githubusercontent.com` cannot read a private repository, so the percentage has to live in the repository itself.

`library/publish_coverage_badge.py` writes the SVG from a percentage, a PHPUnit `clover.xml`, or an `lcov.info`. It does not commit, push, or contact GitHub. The calling workflow commits the file only on the default branch, only when the SVG changed, with `[skip ci]` in the message so the badge commit does not start another test run.

The label is the percentage rounded to the nearest integer. The color is red below 50, yellow below 80, and green from 80 upward. Unknown or empty input writes a neutral grey badge labeled `n/a`.

```shell
python3 publish_coverage_badge.py --percent 82
python3 publish_coverage_badge.py --clover coverage/clover.xml
python3 publish_coverage_badge.py --lcov coverage/lcov.info
```

The helper lives in this public repository, so a private project's workflow can download it and then commit the SVG itself:

```yaml
- name: Publish coverage badge
  if: github.ref == format('refs/heads/{0}', github.event.repository.default_branch)
  run: |
    curl -fsSL -o /tmp/publish_coverage_badge.py \
      https://raw.githubusercontent.com/linkorb/repo-ansible/main/library/publish_coverage_badge.py
    python3 /tmp/publish_coverage_badge.py --clover coverage/clover.xml
    git add -- .github/badges/coverage.svg
    if git diff --cached --quiet -- .github/badges/coverage.svg; then
      exit 0
    fi
    git commit -m "chore: update coverage badge [skip ci]"
    git push
```

The job needs permission to push, and a git author, the same way the repository's other bot commits are configured. The default output path is `.github/badges/coverage.svg`.
