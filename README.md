# vidyabot

## Description

vidyabot is an AI-powered knowledge assistant that combines ancient wisdom with modern technology. The name "vidyabot" merges the Sanskrit word "vidya" (meaning knowledge) with "bot," encapsulating the essence of an intelligent system designed to assist with information processing and knowledge synthesis.

This project aims to create a versatile AI toolkit that leverages cutting-edge language models and machine learning techniques to provide intelligent assistance across various domains.

## Features

- Integrates with multiple AI services including OpenAI, Claude.ai, and Groq
- Utilizes LangChain for advanced language model interactions
- Provides a command-line interface for easy interaction
- Designed with extensibility in mind for future web and mobile applications

## Installation

To set up vidyabot, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/your-username/vidyabot.git
   cd vidyabot
   ```

2. Install Poetry (if not already installed):
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:
   ```
   poetry install
   ```

## Usage

[Provide basic usage instructions here once the CLI is implemented]

## Development

This project uses Poetry for dependency management and packaging. To set up the development environment:

1. Install dependencies:
   ```
   poetry install
   ```

2. Run tests:
   ```
   poetry run pytest
   ```

3. Format code:
   ```
   poetry run black .
   poetry run isort .
   ```

4. Lint code:
   ```
   poetry run flake8
   ```

## Project Origin and AI Assistance

The concept for vidyabot emerged from a collaborative brainstorming session with an AI assistant. The project structure, naming, and initial setup were all developed through this interaction. The AI assistant played a crucial role in suggesting the project name, combining the Sanskrit term for knowledge with a modern tech suffix, and in outlining the initial project structure and configuration.

The AI assistant, while instrumental in the project's conception and initial setup, is not a sentient entity and does not have ongoing involvement in the project. It served as a tool to facilitate the creative process and provide technical guidance based on best practices and the specific requirements discussed during the project's initialization.

## Contributing

[Add contributing guidelines here]

## License

[Add license information here]

## Version History

This project uses semantic versioning. As of July 2024, we performed a manual synchronization to align the internal `__version__` with the GitHub releases. From this point forward, versioning is managed automatically through our release process.

## Contact

[Add your contact information here]

---

This project is in active development. Features, documentation, and usage instructions will be updated as the project evolves.

## Changelog and Release Process

We use `python-semantic-release` to automatically generate changelogs and manage releases. Follow these steps to set up and use the release process:

1. Add `python-semantic-release` as a dev dependency:
   ```
   poetry add --dev python-semantic-release
   ```

2. Create a `pyproject.toml` file in the root of your project (if not already present) and add the following configuration:
   ```toml
   [tool.semantic_release]
   version_variable = "vidyabot/__init__.py:__version__"
   branch = "main"
   changelog_file = "CHANGELOG.md"
   build_command = "poetry build"
   dist_path = "dist/"
   upload_to_pypi = false
   upload_to_release = true
   ```

3. Ensure your `vidyabot/__init__.py` file contains a `__version__` variable:
   ```python
   __version__ = "0.1.0"
   ```

4. Create a `release.py` script in the root of your project:
   ```python
   import subprocess

   def run_command(command):
       process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
       output, error = process.communicate()
       if error:
           print(f"Error: {error}")
       return output.decode('utf-8').strip()

   def main():
       # Run semantic-release
       print("Running semantic-release...")
       result = run_command("semantic-release version")
       print(result)

       # Push changes and tags
       print("Pushing changes and tags...")
       run_command("git push --follow-tags origin main")

       print("Release process completed!")

   if __name__ == "__main__":
       main()
   ```

5. To perform a release, run:
   ```
   poetry run semantic-release --verbose version
   ```
6. To perform a dry run release, run:
   ```
   poetry run python release.py --dry-run
   ```

This script will:
- Determine the next version based on your commits
- Update the version in your code
- Generate or update the CHANGELOG.md file
- Create a new commit with these changes
- Create a new git tag for the release
- Push the changes and tags to your repository

Remember to follow the conventional commit format in your day-to-day development to ensure accurate changelog generation.


## Error Handling

The vidyabot CLI now includes basic error handling. Unexpected errors are caught, reported, and the application will exit with an appropriate status code.


## Asynchronous Implementation

This project has recently undergone significant changes to implement asynchronous programming throughout the application. This shift was necessary to improve performance, scalability, and to properly handle the integration of multiple Language Learning Models (LLMs), specifically OpenAI and Google's Gemini.

### Why Asynchronous?

The decision to move to an asynchronous architecture was driven by several factors:

1. **Multiple LLM Support**: With the integration of both OpenAI and Gemini, our application needs to handle potentially long-running API calls to these services. Asynchronous programming allows us to manage these operations more efficiently, preventing blocking calls that could slow down the entire application.

2. **Improved Scalability**: As the number of concurrent users increases, asynchronous handling of requests becomes crucial. It allows our FastAPI application to handle many simultaneous connections without dedicating a thread to each one, which is particularly important when dealing with I/O-bound operations like API calls to LLMs.

3. **Better Resource Utilization**: Asynchronous code allows for better utilization of system resources. While waiting for responses from external services (like OpenAI or Gemini), the application can process other tasks, leading to improved overall performance.

4. **Consistency with Modern Python Practices**: Many modern Python libraries, including those for AI and machine learning, are moving towards async implementations. Our shift aligns with this trend, making it easier to integrate with other cutting-edge tools and libraries in the future.

### Implementation Details

The asynchronous implementation touches several key areas of our application:

- **FastAPI Routes**: All our API endpoints are now asynchronous, allowing for non-blocking handling of requests.
- **LangChainService**: The core service that interacts with LLMs has been updated to work asynchronously, ensuring that long-running LLM operations don't block other parts of the application.
- **Testing**: Our test suite has been updated to use `pytest-asyncio`, allowing us to properly test asynchronous code paths.

### Challenges and Solutions

Implementing asynchronous programming introduced some challenges, particularly around managing shared resources and ensuring proper initialization of services. We addressed these by:

- Implementing careful error handling and logging to catch and diagnose issues in asynchronous code.
- Updating our dependency injection system in FastAPI to properly handle asynchronous service initialization.
- Revising our testing strategy to account for the asynchronous nature of our application, ensuring thorough coverage of all code paths.

### Benefits Realized

The move to asynchronous programming has already yielded several benefits:

- Improved response times, especially under high load.
- Better handling of concurrent requests to different LLMs.
- Increased overall application stability and scalability.
- A more future-proof codebase that's ready to integrate with other async-first services and libraries.

As we continue to develop and expand this project, the asynchronous foundation we've laid will be crucial in ensuring that we can meet growing demands and integrate new features efficiently.