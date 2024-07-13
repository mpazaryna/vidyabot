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


def main(dry_run=True):
    current_version = get_version_from_toml()
    if current_version is None:
        print("Failed to get current version. Exiting.")
        sys.exit(1)
    print(f"Current version from pyproject.toml: {current_version}")

    print("Running semantic-release...")
    command = "semantic-release version"
    if dry_run:
        print("Dry run: simulating semantic-release execution")
    else:
        output, error = run_command(command)
        print("semantic-release output:", output)
        if error:
            print("semantic-release error output:", error)

        # Check if semantic-release reported a new version
        new_version_line = next(
            (line for line in output.split("\n") if "The next version is:" in line),
            None,
        )
        if new_version_line:
            reported_new_version = new_version_line.split(":")[1].strip().rstrip("! 🚀")
            print(f"semantic-release reported new version: {reported_new_version}")
        else:
            print("semantic-release did not report a new version.")

    new_version = get_version_from_toml()
    print(f"New version from pyproject.toml: {new_version}")

    if new_version != current_version:
        print(
            f"Version in pyproject.toml was updated from {current_version} to {new_version}."
        )
    else:
        print("Version in pyproject.toml was not changed.")

    print("Release process completed!")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run the release process.")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Perform a dry run without making changes",
    )
    args = parser.parse_args()

    main(dry_run=args.dry_run)
