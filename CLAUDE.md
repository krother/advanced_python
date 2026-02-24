# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repo Is

A Sphinx-based coursebook for advanced Python programming techniques, published at [www.academis.eu/advanced_python](http://www.academis.eu/advanced_python). Content is written in `.rst` and `.md` files; Python files are teaching examples and exercises, not a deployable application.

## Building the Documentation

```bash
# Install dependencies
pip install -r requirements.txt

# Build HTML docs
make html

# The output goes to build/html/
```

## Running Tests

The `python_package/` directory contains a sample project (`Pac` game) used to demonstrate packaging, testing, and code quality tooling. Its `pyproject.toml` uses `uv`:

```bash
cd python_package

# Install dependencies
uv lock && uv sync

# Run all tests
uv run pytest

# Run tests with coverage and verbose output
uv run pytest -v -x -s --cov

# Run a single test file
uv run pytest testing/test_words.py
```

Tests in `testing/` and `solutions/space_game_with_classes/` can also be run with plain `pytest` if dependencies are installed.

## Code Quality Tools (only used in python_package/)

```bash
uv run black type_annotations.py       # Format code (line length 79)
uv run isort space_game.py             # Sort imports
uv run mypy type_annotations.py        # Type checking
uv run flake8                          # Style checks
uv run ruff check space_game.py        # Extra linting hints
```

## Repository Structure

```
index.rst / conf.py          Sphinx entry point and configuration (furo theme, myst_parser)
requirements.txt             Sphinx build dependencies only
Makefile                     Sphinx build (make html, make clean, etc.)

python_package/              Sample Python package used in packaging exercises
  pyproject.toml             Project config for "Pac" game (uv + hatchling build)
  pac_game.py                Main game source
  __main__.py                Package entry point

testing/                     Test examples: pytest, fixtures, parametrize, mocking
exercises/                   Standalone exercise files (no test runner config here)
solutions/                   Reference solutions, including space_game_with_classes/
challenges/                  Algorithm challenge descriptions and starter code
design_patterns/             Design pattern examples and their pyproject.toml
quality/                     Code checks, CI, packaging, versioning content
functions/                   Function-level Python examples (decorators, generators, etc.)
classes/                     OOP examples and exercises
concurrency/                 Threading, async, subprocess examples
error_handling/              Exception, logging, debugger examples
performance/                 Profiling and optimization examples
```

## Content Conventions

- Course chapters are `.rst` files (reStructuredText) or `.md` files (MyST Markdown).
- Downloadable files referenced in `.rst` with `:download:`` directives must exist in the same directory.
- Python examples are intentionally simple and self-contained — avoid adding complexity beyond what the chapter teaches.
- The `solutions/` directory holds reference implementations; `exercises/` holds starter/incomplete versions for students.
