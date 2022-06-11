import os
import shutil
import subprocess

log = lambda msg: print(f"pushpin - {msg}")
git = lambda *args: subprocess.run(["git"] + [*args])


def _validate_directory(directory: str = ".pushpin"):
    # Ensure that we're not trying to install outside of cwd
    if not os.path.abspath(
        os.path.join(os.path.abspath(os.getcwd()), os.path.abspath("directory"))
    ).startswith(os.getcwd()):
        raise FileNotFoundError("not allowed")

    # Ensure that cwd is git top level
    if not os.path.exists(".git"):
        raise FileNotFoundError(".git can't be found")


def install(directory: str = ".pushpin"):
    if "PUSHPIN" in os.environ:
        if os.environ["PUSHPIN"] == "0":
            log("PUSHPIN environ variable is set to 0, skipping install")
            return

    # Ensure that we're inside a git repository
    # If git command is not found, status is null and we should return.
    # That's why status value needs to be checked explicitly.
    if git("rev-parse").returncode != 0:
        return

    _validate_directory()
    try:
        # Create .pushpin/_
        os.makedirs(os.path.join(directory, "_"), exist_ok=True)

        # Create .pushpin/_/.gitignore
        with open(os.path.join(directory, "_/.gitignore"), "w") as f:
            f.write("*")

        # Copy pushpin.sh to .pushpin/_/pushpin.sh
        shutil.copy(
            os.path.abspath(os.path.join(os.path.dirname(__file__), "pushpin.sh.py")),
            os.path.abspath(os.path.join(directory, "_/pushpin.sh")),
        )

        # Configure repo
        if git("config", "core.hooksPath", directory).returncode != 0:
            raise RuntimeError(f"`git config core.hooksPath {directory}` failed")
    except Exception as e:
        log("Git hooks failed to install")
        raise e

    log("Git hooks installed")


def set(file: str, cmd: str):
    dirname = os.path.dirname(file)
    if not os.path.exists(dirname):
        raise FileNotFoundError(
            f"can't create hook, {dirname} directory doesn't exist (try running pushpin install)"
        )

    # 0o777 - 0o022 (default umask) = 0o755 permissions
    opener = lambda path, flags: os.open(path, flags, 0o777)
    os.umask(0)

    # Create .pushpin/_/.gitignore
    with open(file, "w", opener=opener) as f:
        f.write("#!/usr/bin/env sh\n")
        f.write('. "$(dirname -- "$0")/_/pushpin.sh\n')
        f.write(cmd + "\n")

    log(f"created {file}")


def add(file: str, cmd: str):
    if os.path.exists(file):
        with open(file, "a") as f:
            f.write(cmd + "\n")
        log(f"updated {file}")
        return
    set(file, cmd)


def uninstall():
    git("config", "--unset", "core.hooksPath")
    log("Git hooks uninstalled")
