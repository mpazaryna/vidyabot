import click

from api import __version__


@click.command()
def hello_world():
    """Simple command that prints Hello World message with version"""
    message = f"Hello, World! Welcome to vidyabot CLI v{__version__}."
    click.echo(message)


if __name__ == "__main__":
    hello_world()
