import click

from api import __version__


@click.command()
def hello_world():
    """Simple command that prints Hello World message with version"""
    message = f"Hello, World! Welcome to the vidyabot CLI v{__version__}."
    click.echo(message)
    click.echo("Thank you for using vidyabot!")


if __name__ == "__main__":
    hello_world()
