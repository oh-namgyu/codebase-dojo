# Security Policy

## Reporting a Vulnerability

If you find a security issue in codebase-dojo, please report it **privately**
instead of opening a public issue:

- Preferred: use GitHub's **private vulnerability reporting** —
  the repository's **Security** tab → **Report a vulnerability**.
- Please don't disclose exploit details in public issues or pull requests
  until a fix is available.

Where possible, include the affected file(s), a description of the issue, and a
minimal way to reproduce it.

## Scope

codebase-dojo is a [Claude Code](https://docs.claude.com/en/docs/claude-code)
skill — it ships **prompt instructions and documentation, not a running
service.** It has no server, no network endpoints, and stores no credentials.
The areas worth scrutiny are:

- The skill instructions (`SKILL.md`) — e.g. prompt-injection paths, or
  instructions that could lead to unsafe shell/file actions.
- Example content under `examples/`.

The learner's journal (`.dojo/<project>.md`) is generated locally inside the
user's own repository and is never transmitted anywhere by this skill.

## Supported Versions

Fixes land on the `main` branch. There are no separately maintained release
branches.

## Response

This is a community project maintained on a best-effort basis. We aim to
acknowledge valid reports within a reasonable time and address confirmed issues
on `main`.
