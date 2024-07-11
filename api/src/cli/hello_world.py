import click

@click.command()
def hello_world():
    """Simple command that prints Hello World"""
    click.echo("Hello, World! Welcome to vidyabot CLI.")

if __name__ == "__main__":
    hello_world()