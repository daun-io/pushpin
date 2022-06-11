# pushpin
Git hooks for python 📌

[![CI](https://github.com/nyanye/pushpin/actions/workflows/ci.yml/badge.svg)](https://github.com/nyanye/pushpin/actions/workflows/ci.yml)
[![PyPI download month](https://img.shields.io/pypi/dm/ansicolortags.svg)](https://pypi.python.org/pypi/pushpin/)
[![PyPI version fury.io](https://badgen.net/pypi/v/pushpin/)](https://pypi.com/project/pushpin)

Pushpin improves your python commits and more.
You can use it to run toolings like pytest, pylint, isort, black, etc
whenever you commit or push. pushpin supports all Git hooks.

# Install

```bash
# For poetry users
poetry add -D pushpin

# For traditional pip users
pip install pushpin
```

# Usage

```bash
# prepare your repo
pushpin install

# add a hook
pushpin add .pushpin/pre-commit "pytest"
```

## Recommended Hooks

```bash
# pylint - strictly manage your code quality
pushpin add .pushpin/pre-commit "pylint --fail-under=8 ."

# isort - sort your import orders
pushpin add .pushpin/pre-commit "isort ."

# black - get some uncompromising styles
pushpin add .pushpin/pre-commit "black ."
```

# Used by

pushpin will be used by these awesome python projects.

- list yours.

