# FC-Filter-Gen-Tool

A minimal starter Python project using the click package for building command-line interfaces.

## Installation

Install the package in development mode:

```bash
pip install -e .
```

Or install from the repository:

```bash
pip install .
```

## Usage

After installation, you can use the `fc-filter-gen` command:

```bash
# Basic usage
fc-filter-gen

# Greet someone by name
fc-filter-gen --name John

# Greet multiple times
fc-filter-gen --name John --count 3
```

You can also run the module directly:

```bash
python -m fc_filter_gen.cli --help
```

## Development

The project uses:
- `click` - For creating beautiful command-line interfaces
- `pyproject.toml` - For project configuration and dependencies

## Project Structure

```
fc-filter-gen-tool/
├── fc_filter_gen/
│   ├── __init__.py
│   └── cli.py
├── pyproject.toml
└── README.md
```