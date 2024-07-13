# File: api/src/cli/hello_world.py

import sys

import click

from api import __version__


@click.command()
def hello_world():
    """Simple command that prints Hello World message with version"""
    try:
        if __version__ == "0.0.0":  # This is just an example condition
            raise ValueError("Invalid version")
        message = f"Hello, World! Welcome to the vidyabot CLI v{__version__}."
        click.echo(message)
        click.echo("Thank you for using vidyabot!")
        return 0
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}", err=True)
        return 1


if __name__ == "__main__":
    sys.exit(hello_world())


def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to vidyabot."
