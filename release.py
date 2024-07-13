import argparse
import configparser
import os
import subprocess
import sys
from importlib.metadata import PackageNotFoundError, version


def get_current_version():
    try:
        return version("vidyabot")
    except PackageNotFoundError:
        # If the package is not installed, fall back to reading from pyproject.toml
        try:
            config = configparser.ConfigParser()
            config.read("pyproject.toml")
            return config["tool.poetry"]["version"].strip('"')
        except (configparser.Error, KeyError):
            raise ValueError("Version not found in pyproject.toml or package metadata")


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
    try:
        current_version = get_current_version()
        print(f"Current version: {current_version}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    print_file_content("api/__init__.py")
    print_file_content("pyproject.toml")

    print("Running semantic-release...")
    if dry_run:
        print("Dry run: simulating semantic-release execution")
        result = "Dry run: Version would be determined based on commits"
        error = None
    else:
        command = "semantic-release version"
        result, error = run_command(command)

    print("Output:", result)
    print("Error output:", error)

    combined_output = result + "\n" + error
    if "The next version is:" in combined_output:
        print("semantic-release ran successfully.")
        # Extract the new version from the output
        for line in combined_output.split("\n"):
            if "The next version is:" in line:
                new_version = line.split(":")[1].strip().rstrip("! 🚀")
                print(f"New version detected: {new_version}")
    else:
        print("Failed to run semantic-release. Exiting.")
        sys.exit(1)

    print_file_content("api/__init__.py")
    print_file_content("pyproject.toml")

    try:
        package_version = get_current_version()
        print(f"Package version after release: {package_version}")

        if package_version != current_version:
            print("Version was updated.")
        else:
            print("No new version was created.")
    except ValueError as e:
        print(f"Error: {e}")

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
