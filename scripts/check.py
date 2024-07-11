import subprocess
import sys


def run_command(command):
    process = subprocess.Popen(command, shell=True)
    process.wait()
    if process.returncode != 0:
        sys.exit(1)


def main():
    print("Running isort...")
    run_command("poetry run isort .")

    print("Running black...")
    run_command("poetry run black .")

    print("Running flake8...")
    run_command("poetry run flake8")

    print("Running tests...")
    run_command("poetry run pytest")

    print("All checks completed successfully!")


if __name__ == "__main__":
    main()
