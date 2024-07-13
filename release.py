import argparse
import os
import subprocess
import sys

import toml


def get_version_from_toml():
    try:
        with open("pyproject.toml", "r") as f:
            pyproject_data = toml.load(f)
            return pyproject_data["tool"]["poetry"]["version"]
    except (FileNotFoundError, KeyError) as e:
        print(f"Error reading version from pyproject.toml: {e}")
        return None


def run_command(command):
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    return output.decode("utf-8").strip(), error.decode("utf-8").strip()


def print_file_content(filepath):
    print(f"Content of {filepath}:")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            print(f.read())
    else:
        print(f"File {filepath} does not exist.")


def main(dry_run=True):
    current_version = get_version_from_toml()
    if current_version is None:
        print("Failed to get current version. Exiting.")
        sys.exit(1)
    print(f"Current version from pyproject.toml: {current_version}")

    print_file_content("pyproject.toml")

    print("Running semantic-release...")
    if dry_run:
        print("Dry run: simulating semantic-release execution")
        result, error = "Dry run: Version would be determined based on commits", ""
    else:
        command = "semantic-release version --verbose"
        result, error = run_command(command)

    print("semantic-release output:", result)
    print("semantic-release error output:", error)

    combined_output = result + "\n" + error
    new_version = None
    if "The next version is:" in combined_output:
        print("semantic-release ran successfully.")
        for line in combined_output.split("\n"):
            if "The next version is:" in line:
                new_version = line.split(":")[1].strip().rstrip("! 🚀")
                print(f"New version detected by semantic-release: {new_version}")
                break
    else:
        print("semantic-release did not report a new version.")

    print("\nChecking pyproject.toml after semantic-release:")
    print_file_content("pyproject.toml")

    updated_version = get_version_from_toml()
    print(f"Updated version from pyproject.toml: {updated_version}")

    if updated_version != current_version:
        print(
            f"Version in pyproject.toml was updated from {current_version} to {updated_version}."
        )
    else:
        print("Version in pyproject.toml was not changed.")

    if new_version and new_version != updated_version:
        print(
            f"Warning: semantic-release reported version {new_version}, but pyproject.toml shows {updated_version}."
        )

    print("Release process completed!")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the release process.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without making changes",
    )
    args = parser.parse_args()

    main(dry_run=args.dry_run)
