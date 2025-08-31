"""Tests for CLI functionality."""

from typer.testing import CliRunner

from alpacasay.cli import app


class TestCLI:
    """Test CLI interface."""

    def test_basic_message(self):
        """Test basic message display."""
        runner = CliRunner()
        result = runner.invoke(app, ["Hello World!"])
        assert result.exit_code == 0
        assert "Hello World!" in result.stdout

    def test_safer_together_flag(self):
        """Test --safer-together flag."""
        runner = CliRunner()
        result = runner.invoke(app, ["--safer-together"])
        assert result.exit_code == 0
        assert "Safer, Together!" in result.stdout

    def test_alpaca_type_selection(self):
        """Test alpaca type selection."""
        runner = CliRunner()
        result = runner.invoke(app, ["--alpaca", "happy", "Hello!"])
        assert result.exit_code == 0
        assert "Hello!" in result.stdout

    def test_color_option(self):
        """Test color option."""
        runner = CliRunner()
        result = runner.invoke(app, ["--color", "red", "Hello!"])
        assert result.exit_code == 0
        assert "Hello!" in result.stdout

    def test_help_command(self):
        """Test help command."""
        runner = CliRunner()
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "Display messages with ASCII alpacas" in result.stdout

    def test_version_command(self):
        """Test version command."""
        runner = CliRunner()
        result = runner.invoke(app, ["--version"])
        assert result.exit_code == 0
        assert "alpacasay version 0.1.0" in result.stdout
