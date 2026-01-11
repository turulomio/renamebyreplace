# RenameByReplace (https://github.com/turulomio/renamebyreplace/)

[![Tests](https://github.com/turulomio/renamebyreplace/actions/workflows/tests.yml/badge.svg)](https://github.com/turulomio/renamebyreplace/actions/workflows/tests.yml)

Rename files searching substrings in filenames.

## Description

`renamebyreplace` is a Python utility that allows you to bulk rename files by searching for a specific substring and replacing it with another. It is designed to be safe by default, offering a preview of changes before applying them.

## Installation

### From Gentoo

If you use Gentoo you can find a ebuild in https://github.com/turulomio/myportage/tree/master/app-admin/renamebyreplace


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
<img src="https://raw.githubusercontent.com/turulomio/renamebyreplace/master/doc/command.gif?raw=true" width="100%"></img>

You can see this animated gif to learn how to use it:

<img src="https://raw.githubusercontent.com/turulomio/renamebyreplace/master/doc/howto.gif?raw=true" width="100%"></img>


## Development

This project uses `poethepoet` for task management.

- **Run Tests & Coverage**: `poe coverage`
- **Update Translations**: `poe translate`
- **Release**: `poe release`
