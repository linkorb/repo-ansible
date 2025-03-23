# Github Actions

What Github permissions to set and how to configure auth for github actions.
Plus some tips and tricks.  Well, some tips at least.

Note: "repo" hereinafter refers to the repo in which the action is run.


## Workflows

### Git Checkout (actions/checkout)

Reads the repo.

No auth configuration needed - by default sets its "token" input to
`github.token`.  Recommends using a minimally privileged PAT though.

### Semantic Release (codfish/semantic-release-action)

Reads from and writes to the repo.

Set the step's `env.GITHUB_TOKEN` to `secrets.GITHUB_TOKEN` as in the
[action's doc][semantic-release-action-doc]

### PR Labeler

Inspects the commits in a pull-request, and applies a series of labels based on conventional-commits nouns.

The tokens are defined in the `.github/settings.yml` file, with the repo-ansible
template located at `templates/.github/settings.yml.j2`.

### Login to Container Registry ghcr.io (docker/login-action)

Logs in to ghcr, ready for subsequent actions to push and pull container
images.

Set the step's registry, username and password inputs to ghcr.io,
`github.actor` and `secrets.GITHUB_TOKEN` as described in the [action's
doc][checkout-action-doc]

### Build and push (docker/build-push-action)

Builds container images and pushes them to the logged-in container registry.

No auth config needed, but when building PHP app containers don't forget to set
build-args like `PACKAGIST_TOKEN` set to `secrets.PACKAGIST_TOKEN`.  The repo
needs access to (and most likely already has access to) the secret set at the
Organisation level.  See it at the repo Settings > Secrets & Variables >
Actions > Secrets (tab) > Organization secrets section.

### Cleanup packages (actions/delete-package-versions)

Deletes old versions of packages (container images) from ghcr.io

No auth config needed - uses [Automatic token authentication][auto-token-auth]
to login to the Container Registry - just ensure the repo has Admin role for
the package it wants to delete.


## Permissions

This section shows what github permissions to change when using particular
authentication tokens in actions.

### `secrets.GITHUB_TOKEN` and `github.token`

Actions accessing the repo: When using this token, no permissions need be set
for actions accessing the repo.  The privileges are [documented
here][auto-token-auth].

Actions accessing the ghcr Container registry: The token can be used to login
to ghcr.io (say, with username=$github.actor), but package permissions
determine what the login is permitted to access.

In the "Manage Actions access" section of the package settings, add the repo
and give it one of the Roles:
    - Read: can pull the package
    - Write: can pull and push the package
    - Admin: can pull, push and delete versions of the package A common scheme
      is to give the repo the Admin role over its own package and Read over
other packages it uses (e.g. php-docker-base).


## Tips

### Workflow

- Conditionally run steps: set job-level environment variables and use them
  with the step "if:" ([source][using-encrypted-secrets-in-a-workflow]).

### Github Permissions

- Minimal `GITHUB_TOKEN` privileges: Use the privileges key at workflow or job
  level to set minimal set of privs (priv not set = no access; except metadata
which = read)

- Pull the php-docker-base container image:  In actions that build container
  images based on php-docker-base, add the repo to the "Manage Actions access"
section of the [php-docker-base package settings][php-docker-base-pkg-settings]
and give it the Read role.


[using-encrypted-secrets-in-a-workflow]: <https://docs.github.com/en/actions/security-guides/encrypted-secrets#using-encrypted-secrets-in-a-workflow>
[auto-token-auth]: <https://docs.github.com/en/actions/security-guides/automatic-token-authentication>
[php-docker-base-pkg-settings]: <https://github.com/orgs/linkorb/packages/container/php-docker-base/settings>
[semantic-release-action-doc]: <https://github.com/codfish/semantic-release-action/tree/main#basic-usage>
[checkout-action-doc]: <https://github.com/docker/login-action#github-container-registry>
