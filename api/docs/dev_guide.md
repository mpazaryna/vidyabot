# Development Guide for vidyabot

## Project Overview

vidyabot is an AI-powered knowledge assistant that combines ancient wisdom with modern technology. The project is structured as a monorepo, containing a Python API, a command-line interface (CLI), and potential future components like a web frontend and mobile application.

## Project Structure

```
vidyabot/
├── api/
│   ├── __init__.py
│   ├── src/
│   │   └── cli/
│   │       └── hello_world.py
│   └── tests/
│       └── test_hello_world.py
├── scripts/
│   └── check.py
├── pyproject.toml
├── README.md
└── release.py
```

## Development Workflow

1. Make code changes
2. Run formatting and linting checks
3. Run tests
4. Commit changes using conventional commit format
5. Push changes to GitHub
6. Run the release process when ready for a new version

## Feature Development Workflow

1. Create a GitHub Issue:
   - Go to the GitHub repository and create a new issue describing the feature.

2. Create a New Branch:
   ```
   git checkout main
   git pull origin main
   git checkout -b feature/issue_number-brief-description
   ```

3. Develop the Feature:
   - Make your changes, committing regularly with conventional commit messages.

4. Keep Your Branch Updated:
   ```
   git fetch origin
   git merge origin/main
   ```
   or
   ```
   git rebase origin/main
   ```

5. Run Tests and Checks:
   ```
   poetry run check
   ```

6. Push Your Branch and Create a Pull Request:
   ```
   git push origin feature/issue_number-brief-description
   ```
   Then, go to GitHub and create a new Pull Request.

7. Code Review:
   - Request reviews from team members or review it yourself.
   - Address any feedback by making new commits on your branch.

8. Merge the Pull Request:
   - Once approved and all checks pass, merge the PR on GitHub.
   - Use "Squash and merge" to keep the main branch history clean.

9. Delete the Branch:
   - After merging, delete the feature branch both on GitHub and locally:
     ```
     git checkout main
     git pull origin main
     git branch -d feature/issue_number-brief-description
     ```

Remember to always create a new branch for each feature or significant change. This keeps your work organized and makes it easier to manage multiple features in development simultaneously.

## Poetry Commands Cheat Sheet

Here's a quick reference for common Poetry commands used in this project:

### Environment Management
- Initialize a new project: `poetry init`
- Install dependencies: `poetry install`
- Add a new dependency: `poetry add <package_name>`
- Add a dev dependency: `poetry add --dev <package_name>`
- Update dependencies: `poetry update`
- Show installed packages: `poetry show`
- Activate virtual environment: `poetry shell`

### Running Commands
- Run a command in the virtual environment: `poetry run <command>`
- Run project-specific script: `poetry run check`

### Testing and Code Quality
- Run tests: `poetry run pytest`
- Run tests with coverage: `poetry run pytest --cov`
- Format code with Black: `poetry run black .`
- Sort imports with isort: `poetry run isort .`
- Lint code with flake8: `poetry run flake8`

### Project Management
- Build the project: `poetry build`
- Publish the project: `poetry publish`
- Show project information: `poetry about`
- Check validity of pyproject.toml: `poetry check`
- Export dependencies to requirements.txt: `poetry export -f requirements.txt --output requirements.txt`

### Version Management
- Show current version: `poetry version`
- Bump version: `poetry version <rule>` (where rule is major, minor, patch, etc.)

### Custom Commands
- Run all checks: `poetry run check`
- Perform a release: `poetry run python release.py`

## Release Process

1. Ensure all changes are committed and pushed
2. Run `poetry run python release.py`
3. The script will:
   - Determine the next version based on commit history
   - Update the version in the code
   - Generate or update the CHANGELOG.md
   - Create a new git tag
   - Push changes and tags to GitHub

## Best Practices

1. Follow the conventional commits specification for commit messages
2. Run the check script (`poetry run check`) before committing to ensure code quality
3. Keep the `pyproject.toml` file up to date with all dependencies
4. Regularly update dependencies to keep the project secure and up-to-date
5. Write tests for new functionality and ensure all tests pass before committing

## Dependency Management Workflow

1. Check for outdated packages:
   ```
   poetry show --outdated
   ```

2. Update all dependencies:
   ```
   poetry update
   ```
   Or update specific packages:
   ```
   poetry update package1 package2
   ```

3. Run tests and checks:
   ```
   poetry run check
   poetry run pytest
   ```

4. If everything passes, commit the changes:
   ```
   git add poetry.lock pyproject.toml
   git commit -m "build(deps): update dependencies

   - Update [list major package updates]
   - Run full test suite to ensure compatibility
   
   This commit keeps the project dependencies up-to-date and secure."
   ```

5. Push changes and monitor CI/CD pipeline:
   ```
   git push origin main
   ```

Remember to review changelogs for major updates and be cautious with breaking changes. Always test thoroughly after updating dependencies.
