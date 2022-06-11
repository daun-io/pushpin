"""defines commandline interface for pushpin with standard argparse"""
import argparse
import sys

from pushpin import commands


def parse_args():
    """provides helpful cli"""
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="cmd")
    install_parser = subparsers.add_parser(
        "install", help="pushpin install [directory] (default: .pushpin)"
    )
    install_parser.add_argument(
        "directory",
        help="installation directory (default: .pushpin)",
        default=".pushpin",
        nargs="?",
    )
    subparsers.add_parser("uninstall", help="pushpin uninstall")
    set_parser = subparsers.add_parser("set", help="pushpin set <file> [cmd]")
    githook_examples = [
        "pre-commit",
        "prepare-commit-msg",
        "commit-msg",
        "post-commit",
        "applypatch-msg",
        "pre-applypatch",
        "pre-rebase",
        "post-rewrite",
        "post-merge",
        "pre-push",
    ]
    command_examples = ["isort .", "black .", "pytest", "pylint --fail-under=8 ."]
    set_parser.add_argument(
        "file",
        help=f"available git hooks such as: {githook_examples}",
    )
    set_parser.add_argument(
        "hook_cmd", help=f"hook commands such as: {command_examples}", nargs="?"
    )
    add_parser = subparsers.add_parser("add", help="pushpin add <file> [cmd]")
    add_parser.add_argument(
        "file", help=f"available git hooks such as: {githook_examples}"
    )
    add_parser.add_argument(
        "hook_cmd", help=f"hook commands such as: {command_examples}", nargs="?"
    )
    args = parser.parse_args()
    if args.cmd is None:
        sys.stderr.write("error: too few arguments\n")
        parser.print_help()
        sys.exit(2)
    return args


def main():
    """entrypoint"""
    args = parse_args()
    command_map = {
        "install": commands.install,
        "uninstall": commands.uninstall,
        "set": commands.set_,
        "add": commands.add,
    }
    command = command_map[args.cmd]
    args = [args.__dict__[key] for key in args.__dict__ if key != "cmd"]
    command(*args)
