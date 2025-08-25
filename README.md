# Alpacasay 🦙
[![PyPI version](https://badge.fury.io/py/alpacasay.svg)](https://badge.fury.io/py/alpacasay/)
[![Python versions](https://img.shields.io/pypi/pyversions/alpacasay.svg)](https://pypi.org/project/alpacasay/)
[![Code Quality](https://github.com/mazzma12/alpacasay/workflows/Code%20Quality/badge.svg)](https://github.com/mazzma12/alpacasay/actions?query=workflow%3A"Code+Quality")
[![Documentation](https://github.com/mazzma12/alpacasay/workflows/Documentation/badge.svg)](https://mazzma12.github.io/alpacasay)

A fun CLI tool that displays messages with ASCII alpacas - like cowsay but with alpacas!

```
 ________________
< Safer, Together! >
 ----------------
        /|   /|
       ( :v:  )
        |(_)|
        --m--m--
```

## Features

- 🦙 **Three unique alpaca designs** - default, happy, and thinking
- 🌈 **Color support** - make your alpacas colorful
- 📏 **Customizable width** - control the speech bubble size
- 📁 **File input** - read messages from files
- 🔧 **Pipe support** - works with stdin
- 🛡️ **Special message** - built-in "Safer, Together!" message

## Installation

### From PyPI

```bash
pip install alpacasay
```

### Using Docker

```bash
# Quick run with Docker
docker run --rm -it ghcr.io/mazzma12/alpacasay:latest "Hello from Docker!"

# Build locally
docker build -t alpacasay .
docker run --rm alpacasay "Your message here"

# Using docker-compose
docker-compose up alpacasay
```

### From Source

```bash
git clone https://github.com/mazzma12/alpacasay.git
cd alpacasay
uv sync --dev
uv run alpacasay "Hello World!"
```

## Quick Start

```bash
# Basic usage
alpacasay "Hello World!"

# Happy alpaca with color
alpacasay --alpaca happy --color green "I'm happy!"

# Special CrowdSec message
alpacasay --safer-together

# From file
alpacasay --file message.txt

# From pipe
echo "Hello from pipe" | alpacasay
```

## Usage

```bash
alpacasay [OPTIONS] [MESSAGE]

Options:
  -a, --alpaca [default|happy|thinking]  Choose alpaca type
  -c, --color [red|green|blue|yellow|magenta|cyan|white]  Text color
  -w, --width INTEGER                    Maximum width of the speech bubble
  --safer-together                       Display the special "Safer, Together!" message
  -f, --file PATH                        Read message from file
  --version                              Show version and exit
  --help                                 Show this message and exit
```

## Examples

### Basic Examples

```bash
# Default alpaca
alpacasay "Hello World!"

# Happy alpaca with green text
alpacasay --alpaca happy --color green "Great job!"

# Thinking alpaca with custom width
alpacasay --alpaca thinking --width 30 "Let me think about this..."
```

### Integration Examples

**Git hook (.git/hooks/post-commit):**
```bash
#!/bin/bash
alpacasay --color cyan "Commit successful! 🎉"
```

**Build script:**
```bash
if npm test; then
    alpacasay --alpaca happy --color green "All tests passed!"
else
    alpacasay --color red "Tests failed!"
fi
```

**Daily motivation (.bashrc):**
```bash
alpacasay --alpaca happy "Have a great day!"
```

## Development

### Prerequisites

- Python 3.11+
- [UV](https://github.com/astral-sh/uv) (recommended) or pip

### Setup

```bash
git clone https://github.com/mazzma12/alpacasay.git
cd alpacasay
uv sync --dev
```

### VS Code Development

This project includes a VS Code task for development setup. To run it:

1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Type "Tasks: Run Task"
3. Select "Alpacasay Development Setup"

This will automatically:
- Install dependencies with `uv sync --dev`
- Format code with `uv run ruff format .`
- Run linting with `uv run ruff check .`
- Execute tests with `uv run pytest -v`
- Build the package with `uv build`
- Test the CLI with `uv run alpacasay --safer-together`

### Manual Commands

```bash
# Install dependencies
uv sync --dev

# Run tests
uv run pytest

# Linting and formatting
uv run ruff check .
uv run ruff format .

# Type checking
uv run pyright

# Build package
uv build

# Run locally
uv run alpacasay "Test message"
```

### Docker Development

```bash
# Build development image
docker build -t alpacasay:dev .

# Run with volume mount for development
docker run --rm -v $(pwd):/app alpacasay:dev "Development test"

# Build production image
docker build -f Dockerfile.production -t alpacasay:prod .
```

### Documentation

```bash
# Install docs dependencies
uv sync --group docs

# Serve documentation locally
uv run mkdocs serve

# Build documentation
uv run mkdocs build
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the classic `cowsay` utility
- ASCII art created with love for the alpaca community
- Built with modern Python tooling (uv, ruff, pytest, mkdocs)

## Links
- [Documentation](https://mazzma12.github.io/alpacasay)
- [PyPI Package](https://pypi.org/project/alpacasay/)
- [Source Code](https://github.com/mazzma12/alpacasay)
- [Issue Tracker](https://github.com/mazzma12/alpacasay/issues)
