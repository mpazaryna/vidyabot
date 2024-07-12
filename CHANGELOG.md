# CHANGELOG



## v0.6.1 (2024-07-12)


## v0.6.0 (2024-07-12)

### Feature

* feat: add new functionality to test semantic-release

This commit is to test if semantic-release correctly updates the version. ([`a57a46a`](https://github.com/mpazaryna/vidyabot/commit/a57a46aefdee45eb293935bd4b2a2679f2ea2ca3))


## v0.5.3 (2024-07-12)

### Fix

* fix: force version update for testing

This commit is to test if semantic-release correctly updates the version. ([`e6836a5`](https://github.com/mpazaryna/vidyabot/commit/e6836a5a5c6f502cad7e62014f9211d0601a4b4e))


## v0.5.2 (2024-07-12)

### Chore

* chore: update release script to use Poetry for command execution

- Modify run_command function to execute semantic-release within Poetry environment
- Ensure consistency with project&#39;s dependency management
- Improve isolation and version control of the release process ([`d475a1b`](https://github.com/mpazaryna/vidyabot/commit/d475a1b84d64d52cbe4043b3a2f09f853970f1e1))

### Fix

* fix: manually bump version to 0.5.1 ([`ea3a02a`](https://github.com/mpazaryna/vidyabot/commit/ea3a02a6f79869b4d9b0955692086297877bd1f5))


## v0.5.1 (2024-07-12)

### Chore

* chore: add version history note to README

- Documents recent manual version synchronization
- Provides context for future contributors about the versioning process ([`9ff39b0`](https://github.com/mpazaryna/vidyabot/commit/9ff39b04ec77e6be03838ae5367f318df7d0d769))

* chore: update __version__ to 0.5.0 to align with latest release

- Syncs internal version number with the latest GitHub release tag
- Ensures consistency between codebase and published releases ([`856218b`](https://github.com/mpazaryna/vidyabot/commit/856218b6edd48562db4f4b1c4c3e35a8478902d6))

### Fix

* fix: resolve version sync issue

- Adjust semantic-release configuration to recognize chore commits
- Ensure proper version bumping for maintenance tasks ([`150a28b`](https://github.com/mpazaryna/vidyabot/commit/150a28ba9c056815126e6cfa9bd9206142adaaa3))

* fix: resolve version sync issue

- Adjust semantic-release configuration to recognize chore commits
- Ensure proper version bumping for maintenance tasks ([`6611366`](https://github.com/mpazaryna/vidyabot/commit/6611366fe8838c703aad0f7e2cabd54a78000893))


## v0.5.0 (2024-07-12)

### Documentation

* docs: Add FUTURE_IMPROVEMENTS.md for tracking planned enhancements ([`353da2c`](https://github.com/mpazaryna/vidyabot/commit/353da2c26c6aaec14f3895c895a041e318dec0ad))

* docs: add feature development workflow to guide

- Include step-by-step process for feature branch development
- Detail GitHub Issues, branching, and Pull Request procedures
- Emphasize code review and clean merge practices

This commit enhances project documentation with clear guidelines for feature development using Git and GitHub. ([`fb68d75`](https://github.com/mpazaryna/vidyabot/commit/fb68d75b12915243a80e28be2b66ef8b6ecc608d))

* docs: add dependency management workflow to development guide

- Include step-by-step process for updating dependencies
- Add best practices for maintaining up-to-date and secure dependencies

This commit enhances project documentation with clear guidelines for dependency management. ([`8c2226a`](https://github.com/mpazaryna/vidyabot/commit/8c2226af22abce003384b597e0b4fb78d39c7c71))

* docs: add development guide and Poetry cheat sheet

- Create DEVELOPMENT.md with project overview and structure
- Include Poetry commands cheat sheet for quick reference
- Document development workflow and best practices

This commit enhances project documentation for easier onboarding and reference. ([`13bb64c`](https://github.com/mpazaryna/vidyabot/commit/13bb64c38546e1546510b77604b9ea5cead0051f))

### Feature

* feat(server): Implement robust server management system

- Create scripts/manage_server.py for server lifecycle management
  - Implement start, stop, and restart functionality
  - Add process discovery and management using psutil
  - Handle edge cases like stale PID files and port conflicts

- Create scripts/run_server.py for FastAPI application execution
  - Configure Uvicorn to run the FastAPI app
  - Implement logging to server.log with rotation

- Update api/src/main.py to work with the new server management system
  - Ensure compatibility with Uvicorn runner

- Improve error handling and logging across all components
  - Add detailed error messages and logging for better debugging

- Resolve issues with process detachment and port conflicts
  - Ensure clean process termination and port release

This commit provides a robust server management system, allowing for
easy starting, stopping, and restarting of the FastAPI server. It
addresses previous issues with process management, logging, and port
conflicts, providing a more stable and maintainable server infrastructure. ([`1d1e2f6`](https://github.com/mpazaryna/vidyabot/commit/1d1e2f6cf1c15871541f82915376bb1117816039))

* feat(api): Implement FastAPI server and add tests

- Add FastAPI server implementation in api/src/main.py
  - Create root endpoint (/)
  - Implement /users endpoint to fetch user data
- Create unit tests for FastAPI endpoints in api/tests/test_main.py
- Update pyproject.toml:
  - Add FastAPI and Uvicorn as dependencies
  - Include start-server and start-server-prod scripts
- Implement server management script in scripts/manage_server.py
- Add graceful shutdown handling to scripts/start_server.py

This commit sets up the basic FastAPI server structure, adds
initial endpoints, implements unit tests, and provides scripts
for server management. It maintains the existing dynamic versioning
configuration. ([`e9a1ea5`](https://github.com/mpazaryna/vidyabot/commit/e9a1ea527a1d456aaea4b05820963f4308ba82d6))

* feat(api): Implement user data retrieval and improve project structure

Add get_user_data() function and related improvements:

Create get_user_data() in api/src/data/user_data.py

- Add tests in api/tests/test_user_data.py
- Create static_data directory for JSON storage
- Update .gitignore (exclude build artifacts, include poetry.lock)
- Add type hints and comprehensive docstrings
- Implement test for docstring presence

This commit sets up user data retrieval from a local JSON file with
the intention of future refactoring for external data sources. It also
improves the project structure and documentation. ([`df6f626`](https://github.com/mpazaryna/vidyabot/commit/df6f626b78aa96aacbc860cc8ea87df157204dc1))

### Fix

* fix(tests): Resolve test failures and improve error handling

- Update main.py to better handle exceptions from get_user_data()
- Modify test_main.py to use json.dumps for mock data, ensuring proper JSON formatting
- Update test_user_data.py to use json.dumps for mock data
- Improve error handling and exception raising in user_data.py
- Ensure consistent behavior across the main application and tests

This commit resolves issues with JSON parsing in tests, improves error
handling in the main FastAPI application, and ensures that the get_user_data()
function correctly handles potential exceptions. All tests are now passing,
providing a stable foundation for further development. ([`0297ee4`](https://github.com/mpazaryna/vidyabot/commit/0297ee4a4c73ad6a1e5b5164e2588bf6c892594a))

### Unknown

* Merge pull request #4 from mpazaryna/3-title-implement-fastapi-server-with-flexible-start-up-scripts

3 title implement fastapi server with flexible start up scripts ([`050147b`](https://github.com/mpazaryna/vidyabot/commit/050147b65b6dbfcd81be9ef68214d7f97928d74e))

* Merge pull request #2 from mpazaryna/1-implement-function-to-read-data-from-local-file

feat(api): Implement user data retrieval and improve project structure #1 ([`67a0492`](https://github.com/mpazaryna/vidyabot/commit/67a0492cd42e7edc2ebbd5a68edd5ca49107e59d))


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
