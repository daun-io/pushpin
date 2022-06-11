#!/usr/bin/env sh
# pylint: disable-all
# type: ignore
if [ -z "$pushpin_skip_init" ]; then
  debug () {
    if [ "$PUSHPIN_DEBUG" = "1" ]; then
      echo "pushpin (debug) - $1"
    fi
  }

  readonly hook_name="$(basename -- "$0")"
  debug "starting $hook_name..."

  if [ "$PUSHPIN" = "0" ]; then
    debug "PUSHPIN env variable is set to 0, skipping hook"
    exit 0
  fi

  if [ -f ~/.pushpinrc ]; then
    debug "sourcing ~/.pushpinrc"
    . ~/.pushpinrc
  fi

  readonly pushpin_skip_init=1
  export pushpin_skip_init
  sh -e "$0" "$@"
  exitCode="$?"

  if [ $exitCode != 0 ]; then
    echo "pushpin - $hook_name hook exited with code $exitCode (error)"
  fi

  if [ $exitCode = 127 ]; then
    echo "pushpin - command not found in PATH=$PATH"
  fi

  exit $exitCode
fi