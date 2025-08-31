"""
Alpacasay - A fun CLI tool that displays messages with ASCII alpacas - like cowsay but with alpacas!

Like cowsay, but with alpacas!
"""

from alpacasay.alpacas import ALPACAS, AlpacaType
from alpacasay.cli import app
from alpacasay.formatter import format_message

__all__ = ["ALPACAS", "AlpacaType", "format_message", "app"]
