<!-- Managed by https://github.com/linkorb/repo-ansible. Manual changes will be overwritten. -->
<!-- Repo-specific guidance: docs/partials/copilot-instructions.md (appended below).
     Enabled by github.features.copilot_instructions in repo.yaml. -->
# Copilot instructions for repo-ansible

Ansible playbooks with templated configuration to apply to all LinkORB code repositories.

## Engineering controls

- Files containing the header `Managed by https://github.com/linkorb/repo-ansible` are
  generated. Flag any change that hand-edits them; the edit will be overwritten on the
  next repo-ansible run. The correct change is in `repo.yaml` or `docs/partials/` instead.
- External GitHub Actions and reusable workflows (`uses: owner/repo@ref`) must be pinned to a
  full commit SHA with a version comment (`# vN https://github.com/...`), never a mutable tag
  like `@v4`. Tags can be repointed to malicious commits when an action's repository is
  compromised; a pinned SHA is immutable and blocks that supply-chain attack. Flag any external
  `uses:` that is not SHA-pinned. Local references (`uses: ./...`) can't carry a ref and are exempt.
- Flag new or version-changed dependencies in manifest files (composer.json, package.json,
  etc.) with copyleft licenses: AGPL always; GPL/LGPL for discussion.
- Flag new files or code blocks that appear to be third-party source (foreign copyright
  headers, embedded license notices, wholesale-copied implementations) so licensing can
  be verified. These bypass dependency manifests and are invisible to dependency scanners.
