# CHANGELOG

## v0.11.0 (2024-07-16)

### Feature

* feat: integrate LangChain service and resolve deprecation warnings

- Add LangChainService for text generation, summarization, and translation
- Create /generate_response endpoint in FastAPI app
- Update to langchain-openai and use RunnableSequence pattern
- Implement comprehensive logging to server.log
- Resolve OpenAI and LLMChain deprecation warnings ([`4a95e83`](https://github.com/mpazaryna/vidyabot/commit/4a95e8349369ed1954abe6cc634181d5fcde6b8d))

### Unknown

* Merge pull request #8 from mpazaryna/7-create-langchain_service-class

feat: integrate LangChain service and resolve deprecation warnings ([`384f159`](https://github.com/mpazaryna/vidyabot/commit/384f159e32e3996ede2d21b616718c56f10d5537))

## v0.10.0 (2024-07-13)

### Breaking

* feat: implement basic error handling in hello_world.py

- Add try-except block in hello_world function
- Return appropriate exit codes (0 for success, 1 for error)
- Update tests to cover error handling scenarios
- Add error handling information to README.md

This commit improves the reliability of the CLI by adding basic
error handling and reporting. It maintains existing functionality
while providing better feedback in case of unexpected errors.

BREAKING CHANGE: None ([`640c8f2`](https://github.com/mpazaryna/vidyabot/commit/640c8f29ff650caf7a8d35797949fd19cc76a688))

### Unknown

* Merge pull request #6 from mpazaryna/5-improve-error-handling

feat: implement basic error handling in hello_world.py ([`ad6cd1c`](https://github.com/mpazaryna/vidyabot/commit/ad6cd1cd35987a863c03ed18fd645bf715e4c773))

## v0.9.2 (2024-07-13)

### Fix

* fix: remove cruft code

These functions were created as part of testing the release process; they are cruft. ([`b8f5335`](https://github.com/mpazaryna/vidyabot/commit/b8f5335276cc74f68d78f16ca8def853f25b01cc))

## v0.9.1 (2024-07-13)

### Fix

* fix: update semantic-release and improve release script compatibility

- additional changes suggested by claude.ai ([`089345a`](https://github.com/mpazaryna/vidyabot/commit/089345a298aba66451f0afcd61b272acb8b5db91))

* fix: update script to force a release

- another cruft function to retest semantic release ([`0f24a48`](https://github.com/mpazaryna/vidyabot/commit/0f24a484a089d9fb000f13f0036bd0dd50cef561))

* fix: improve version change detection in release script

This commit updates the release script to better detect and report
version changes made by semantic-release. It now checks both the
semantic-release output and the pyproject.toml file for changes.&#34; ([`9cd7c0d`](https://github.com/mpazaryna/vidyabot/commit/9cd7c0d4d73fca99db606f1295082415a36bbd40))

## v0.9.0 (2024-07-13)

### Breaking

* fix: update versioning to use toml file only

This commit updates the semantic-release configuration to use only
the toml file for versioning. It also updates the release script
to read and report versions from the toml file correctly.

BREAKING CHANGE: The versioning system has been changed to rely
solely on the pyproject.toml file, which may affect how versions
are determined and updated. ([`5b7b2b1`](https://github.com/mpazaryna/vidyabot/commit/5b7b2b13477424474172bc742bf586ca3ed6234b))

### Feature

* feat: add force release helper function

slight modification to force new version on release. ([`30eb26e`](https://github.com/mpazaryna/vidyabot/commit/30eb26ee80b1cd06a97a5759bc7faaa7e7f1358b))

* feat: add force release helper function

This commit is intended to trigger a new minor version release.
The added function doesn&#39;t affect any actual functionality. ([`bf71032`](https://github.com/mpazaryna/vidyabot/commit/bf710327ce1e7cd96b1db75556907673cb6776f4))

### Fix

* fix: update with method to retest

- added a new method, previous commit did not trigger a release. ([`36dd72b`](https://github.com/mpazaryna/vidyabot/commit/36dd72b22acc0ebbd3a88a2d5df7916b37c3d120))

* fix: simplify and improve debugging in release script

- Removed references to api directory
- Focused solely on version in pyproject.toml
- Added more detailed semantic-release output
- Improved version change detection and reporting ([`70f433c`](https://github.com/mpazaryna/vidyabot/commit/70f433cc57628cc146c08d060eea5460faaec31d))

## v0.8.3 (2024-07-13)

### Fix

* fix: handle split output from semantic-release in release script

- Combined stdout and stderr when checking for successful release
- Extract new version number from semantic-release output
- Improved reporting of semantic-release output and errors
- Added check for package version update after release ([`faab93a`](https://github.com/mpazaryna/vidyabot/commit/faab93ac9be78f79d9a3dabd0479fe8fe5709825))

## v0.8.2 (2024-07-13)

### Fix

* fix: improve semantic-release output handling in release script

- Modified run_command function to capture both output and error streams
- Updated main function to correctly interpret semantic-release output
- Improved error reporting and success detection ([`408b1b0`](https://github.com/mpazaryna/vidyabot/commit/408b1b0f7aff777b4bf5ce321244f0301c60c4df))

## v0.8.1 (2024-07-13)

### Documentation

* docs: update conventional commit docs ([`af2b00a`](https://github.com/mpazaryna/vidyabot/commit/af2b00a87217de1fb211d4fed1c8bb0084b9afec))

* docs: add conventional commits cheat sheet

- Create CONVENTIONAL_COMMITS.md with quick reference guide
- Include commit types, structure, and best practices ([`c00b65a`](https://github.com/mpazaryna/vidyabot/commit/c00b65a54016c2d78e1f69414bd8d8f3fe449c4c))

### Fix

* fix: update release script and README for dry run functionality

- Modified release.py to handle semantic-release without --dry-run option
- Updated README.md to include instructions for running with dry run flag
- Improved error handling and simulation of dry run in release script ([`7b6c01c`](https://github.com/mpazaryna/vidyabot/commit/7b6c01c257d95ae99507b50ce467bacb1b49ddb4))

## v0.8.0 (2024-07-12)

### Feature

* feat: add test feature to verify semantic-release ([`c8110b2`](https://github.com/mpazaryna/vidyabot/commit/c8110b263cd661a028fb9b5b12c89cb36d9f4246))

## v0.7.0 (2024-07-12)

### Chore

* chore: align version references and update semantic-release config ([`8b4406e`](https://github.com/mpazaryna/vidyabot/commit/8b4406e7a456599152990c244dcbc846238fb0ed))

### Feature

* feat: add test feature to verify semantic-release

This commit is to verify that semantic-release creates a new minor version. ([`e278a30`](https://github.com/mpazaryna/vidyabot/commit/e278a30172b37ecbf221452bc35fa7326e36d21f))

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
