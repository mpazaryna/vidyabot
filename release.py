import subprocess
import sys


def run_command(command):
    print(f"Executing: {command}")
    full_command = f"poetry run {command}"
    process = subprocess.Popen(
        full_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    if process.returncode != 0:
        print(f"Error: {error.decode('utf-8')}")
        return None
    return output.decode("utf-8").strip()


def get_current_version():
    with open("api/__init__.py", "r") as f:
        for line in f:
            if line.startswith("__version__"):
                return line.split("=")[1].strip().strip("\"'")
    return None


def main():
    # Check current version
    current_version = get_current_version()
    print(f"Current version: {current_version}")

    # Run semantic-release
    print("Running semantic-release...")
    result = run_command("semantic-release version")
    if result is None:
        print("Failed to run semantic-release. Exiting.")
        sys.exit(1)
    print(result)

    # Check new version
    new_version = get_current_version()
    print(f"New version: {new_version}")

    if new_version != current_version:
        # Push changes and tags
        print("Pushing changes and tags...")
        push_result = run_command("git push --follow-tags origin main")
        print(push_result)
    else:
        print("No new version created. Skipping push.")

    print("Release process completed!")


if __name__ == "__main__":
    main()
