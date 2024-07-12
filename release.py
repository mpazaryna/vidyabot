import subprocess
import sys


def run_command(command):
    print(f"Executing: {command}")
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    if error:
        print(f"Error: {error.decode('utf-8')}")
    return output.decode("utf-8").strip()


def main():
    # Check current version
    current_version = run_command("semantic-release print-version --current")
    print(f"Current version: {current_version}")

    # Run semantic-release
    print("Running semantic-release...")
    result = run_command("semantic-release version --verbose")
    print(result)

    # Check new version
    new_version = run_command("semantic-release print-version --current")
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
