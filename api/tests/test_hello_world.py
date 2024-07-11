from click.testing import CliRunner

from api import __version__
from api.src.cli.hello_world import hello_world


def test_hello_world():
    runner = CliRunner()
    result = runner.invoke(hello_world)
    assert result.exit_code == 0
    assert (
        result.output.strip()
        == f"Hello, World! Welcome to the vidyabot CLI v{__version__}."
    )
