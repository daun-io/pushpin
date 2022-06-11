# pushpin
Git hooks for python 📌

Pushpin improves your python commits and more.
You can use it to run toolings like pytest, pylint, isort, black, etc
whenever you commit or push. pushpin supports all Git hooks.

# Features
- It's basically [husky](https://typicode.github.io/husky/#/) but for pip and modern python toolings
- Zero dependencies and lightweight
- Powered by modern new Git feature (core.hooksPath)
- Follows python best practices
- User-friendly messages
- Optional install
- Supports
    - macOS, Linux and Windows
    - Git GUIs
    - Custom directories
    - Monorepos

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

