# CHANGELOG



## v0.4.0 (2024-07-11)

### Build

* build: synchronize version in __init__.py with latest release

- Manually update __version__ to 0.3.0 to match the latest release
- Ensure consistency between git tags and package version ([`a6b8604`](https://github.com/mpazaryna/vidyabot/commit/a6b8604253d6b6194594e46d545ab3ca4b37d830))

* build: implement dynamic versioning and clean up pyproject.toml

- Add poetry-dynamic-versioning for consistent version management
- Resolve conflicts in build-system configuration
- Clean up and organize pyproject.toml ([`3e19a68`](https://github.com/mpazaryna/vidyabot/commit/3e19a686d3960f4a49b818743e189941c6e2b2bc))

### Chore

* chore: clean up project structure

- Remove unnecessary __init__.py from root
- Ensure correct __init__.py in api/ directory ([`d5b2cf0`](https://github.com/mpazaryna/vidyabot/commit/d5b2cf0e781099904acb20b3752f0ccae505c205))

* chore: cleanup after command line scripts. ([`99c1cd5`](https://github.com/mpazaryna/vidyabot/commit/99c1cd59048e93353b0deec24ab22e4e81142966))

### Feature

* feat(cli): add thank you message to CLI output

- Include an additional line thanking the user
- Enhance user experience with friendly message

This commit adds a small but meaningful improvement to the CLI interaction. ([`0cafaf6`](https://github.com/mpazaryna/vidyabot/commit/0cafaf6cbe24bdae7eed129d40f165f3ec44c582))

### Style

* style(cli): fix line length in hello world function

- Split long line in hello_world function to comply with PEP 8
- Maintain functionality while improving code style

This commit ensures the CLI code adheres to style guidelines. ([`949fc36`](https://github.com/mpazaryna/vidyabot/commit/949fc362e93e03dcd2debebde6c6893052b666ae))

* style(cli): fix line length in hello world function

- Split long line in hello_world function to comply with PEP 8
- Maintain functionality while improving code style

This commit ensures the CLI code adheres to style guidelines. ([`e39b158`](https://github.com/mpazaryna/vidyabot/commit/e39b158bb2c783f39888533f07a679cdc6c390ab))

### Test

* test(cli): update hello world test to match new CLI output

- Adjust test assertion to include the new thank you message
- Ensure test accurately reflects current CLI behavior

This commit aligns the test with the updated CLI functionality. ([`b36de6a`](https://github.com/mpazaryna/vidyabot/commit/b36de6a4ad493fd477fdc35ffd8880aebf0f7f6f))


## v0.3.0 (2024-07-11)

### Chore

* chore(release): prepare for initial release

- build(config): update semantic-release configuration in pyproject.toml
- chore(version): set initial version to 0.1.0 in api/__init__.py

This commit finalizes the configuration for the initial release and sets the starting version. ([`d780af8`](https://github.com/mpazaryna/vidyabot/commit/d780af8ce06e6e3864b8ffce6ca789a25beed34f))

* chore(release): bump version to 0.2.0 ([`c87f6db`](https://github.com/mpazaryna/vidyabot/commit/c87f6dbb5916fb73720d1f68c627cee5688fa0cb))

### Feature

* feat(cli): enhance hello world message

- Update hello world message to include &#39;v2&#39;
- Update corresponding test to match new message

This commit improves the hello world functionality with a version indicator. ([`dcf3e8e`](https://github.com/mpazaryna/vidyabot/commit/dcf3e8e615a8629e801e6c4c4ee935521803d33d))


## v0.2.0 (2024-07-11)

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
