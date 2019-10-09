#!/bin/sh -e
#
# Run black to format source files
#
if [ "$(uname -s)" = "Darwin" ]; then
    # If called through a symlink, this will point to the symlink
    THIS_SCRIPT_DIR="$( cd "$( dirname "${0}" )" && pwd )"
else
    THIS_SCRIPT_DIR=$(dirname $(readlink -f "${0}"))
fi
(
    # Run from project base
    cd ${THIS_SCRIPT_DIR}/..

    black --include .py$ src
)

