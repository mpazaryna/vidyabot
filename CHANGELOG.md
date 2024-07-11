# CHANGELOG



## v0.1.0 (2024-07-11)

### Build

* build(release): add release automation script

- feat(release): implement release.py for automating the release process

This commit adds a Python script to streamline the release process using semantic-release. ([`4fdcb2c`](https://github.com/mpazaryna/vidyabot/commit/4fdcb2cc7aa99635c1680f822259badaee886778))

* build(poetry): update project structure in pyproject.toml

- fix(build): change packages directory from vidyabot to api
- fix(test): update pytest configuration to look in api/tests
- fix(version): update semantic_release to look for version in api/__init__.py

This commit aligns the pyproject.toml configuration with the new monorepo structure. ([`efa45b5`](https://github.com/mpazaryna/vidyabot/commit/efa45b50ac7999c2db97e47a7c0cdc180c152db4))

* build(poetry): configure project with pyproject.toml

- feat(deps): add core dependencies (openai, langchain, groq, httpx)
- feat(dev-deps): add development tools (pytest, black, isort, flake8)
- feat(build): set up poetry build system
- feat(test): configure pytest with coverage
- feat(style): set up black and isort for code formatting
- feat(lint): configure flake8 for linting
- feat(release): add python-semantic-release configuration

This commit establishes the project&#39;s core configuration, including
dependencies, development tools, and release management setup. ([`685cae4`](https://github.com/mpazaryna/vidyabot/commit/685cae4e833f849855b16b96258f82b8872bd09c))

### Documentation

* docs(readme): update changelog and release process for Python projects

- feat(docs): replace npm/standard-version with python-semantic-release
- feat(docs): add instructions for setting up python-semantic-release
- feat(docs): include Python script for release automation
- chore(docs): adjust project configuration for semantic-release

This commit updates the release process documentation to be compatible with Python projects using Poetry. ([`0410c05`](https://github.com/mpazaryna/vidyabot/commit/0410c05c334a93a2669471cb8e93cc6fcf58b38b))

### Feature

* feat(core): initialize package with version

- feat(core): add __init__.py file to vidyabot package
- feat(version): set initial version to 0.1.0

This commit sets up the main package structure and initializes version tracking. ([`b6bcf9f`](https://github.com/mpazaryna/vidyabot/commit/b6bcf9ff2f2bc144ce8497ec12495d3e4f4fdde9))

### Unknown

* first commit ([`48b6594`](https://github.com/mpazaryna/vidyabot/commit/48b6594d2a262b8dae5df10ecef12a489d48eff0))
