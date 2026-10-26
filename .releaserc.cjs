/**
 * Managed by https://github.com/linkorb/repo-ansible. Manual changes will be overwritten.
 *
 * Configuration file used by the release workflow .github/workflows/30-release-and-build.yaml
 */
/**
 * @type {import('semantic-release').GlobalConfig}
 */
module.exports = {
  branches: ["main"],
  debug: "True",
  plugins: [
    [ "@semantic-release/commit-analyzer", { preset: "angular", releaseRules: [
          { type: "chore",    release: "patch" },
          { type: "ci",       release: "patch" },
          { type: "docs",     release: "patch" },
          { type: "refactor", release: "patch" },
          { type: "style",    release: "patch" },
          { type: "test",     release: "patch" },
    ] } ],
    "@semantic-release/release-notes-generator",
    [ "@semantic-release/github", {successCommentCondition: false, failCommentCondition: false} ],
    "@semantic-release/changelog",
    [ "@semantic-release/npm", { npmPublish: false } ],
    [ "@semantic-release/exec", { generateNotesCmd: "echo -n ${nextRelease.version} > .gitrelease" } ],
    [ "@semantic-release/git", {
        assets: [
          "package.json",
          "CHANGELOG.md",
          "package.json",
          "package-lock.json",
          ".gitrelease",
          "CHANGELOG.md"
        ],
        message: "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
    } ]
  ]
}
