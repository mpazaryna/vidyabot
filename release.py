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
