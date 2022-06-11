<h1 align="center">pushpin</h1>

<p align="center">
<a href="https://raw.githubusercontent.com/nyanye/pushpin/main/docs/pushpin.png"><img src="https://raw.githubusercontent.com/nyanye/pushpin/main/docs/pushpin.png"></a><br>
  <a href="https://github.com/nyanye/pushpin/actions/workflows/ci.yml"><img src="https://github.com/nyanye/pushpin/actions/workflows/ci.yml/badge.svg"/></a>
  <a href="https://pypi.org/project/pushpin/"><img src="https://badge.fury.io/py/pushpin.svg" /></a>
  <a href="https://pypi.org/project/pushpin/"><img src="https://img.shields.io/pypi/dm/ansicolortags.svg" /></a>
</p>

<p align="center">
Git hooks for python 📌
</p>
<p align="center">
Pushpin improves your python commits and more.<br>
You can use it to run toolings like pytest, pylint, isort, black, etc<br>
whenever you commit or push. pushpin supports all Git hooks.<br>
It's basically <a href="https://typicode.github.io/husky/">husky</a> but for modern python toolings
</p>


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

