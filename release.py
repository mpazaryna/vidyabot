import os


def print_file_content(filepath):
    print(f"Content of {filepath}:")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            print(f.read())
    else:
        print(f"File {filepath} does not exist.")


def main():
    current_version = get_current_version()
    print(f"Current version: {current_version}")

    print_file_content("api/__init__.py")
    print_file_content("pyproject.toml")

    print("Running semantic-release...")
    result = run_command("semantic-release --verbose version --dry-run")
    if result is None:
        print("Failed to run semantic-release. Exiting.")
        sys.exit(1)
    print(result)

    print_file_content("api/__init__.py")
    print_file_content("pyproject.toml")

    new_version = get_current_version()
    print(f"New version: {new_version}")

    if new_version != current_version:
        print("Version would be updated (dry run).")
    else:
        print("No new version would be created (dry run).")

    print("Release process simulation completed!")
