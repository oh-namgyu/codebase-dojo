# Changelog

All notable changes are documented here. Format: [Keep a Changelog](https://keepachangelog.com/), versioning: [SemVer](https://semver.org/).

## [0.1.1] - 2026-10-16
### Added
- `tests/test_skill.py`: validates `SKILL.md` frontmatter (no BOM, name, description length) and runs in CI.
- CI workflow: checks that the required files are present, validates `SKILL.md`, and greps for obvious secrets.
- Dependabot weekly updates for GitHub Actions, with auto-merge of patch/minor updates once checks pass.

### Changed
- README: Korean summary at the top, CI/License/Release badges, and a standardized License section that links `SECURITY.md`.
- CI actions bumped: `actions/checkout` 4 → 7, `dependabot/fetch-metadata` 2 → 3.

## [0.1.0] - 2026-06-19
### Added
- Initial public release.
