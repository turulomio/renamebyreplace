# RenameByReplace

[![Tests](https://github.com/turulomio/renamebyreplace/actions/workflows/tests.yml/badge.svg)](https://github.com/turulomio/renamebyreplace/actions/workflows/tests.yml)

Rename files searching substrings in filenames.

## Description

`renamebyreplace` is a Python utility that allows you to bulk rename files by searching for a specific substring and replacing it with another. It is designed to be safe by default, offering a preview of changes before applying them.

## Installation

### From PyPI

```bash
pip install renamebyreplace
```

### From Source

This project uses Poetry (version 2.0+) for dependency management.

```bash
git clone https://github.com/turulomio/renamebyreplace/
cd renamebyreplace
poetry install
```

## Usage

The basic syntax requires a search string and a replacement string:

```bash
renamebyreplace --search "old_text" --replace "new_text"
```

By default, this runs in **dry-run** mode, printing the changes that would occur without modifying the file system.

To apply the changes, use the `--write` flag:

```bash
renamebyreplace --search "old_text" --replace "new_text" --write
```

## Development

This project uses `poethepoet` for task management.

- **Run Tests & Coverage**: `poe coverage`
- **Update Translations**: `poe translate`
- **Release**: `poe release`

## License

This project is licensed under the GPL-3 License.

## Authors

* Turulomio <turulomio@yahoo.es>