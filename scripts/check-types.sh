#!/bin/sh -e
#
# Run mypy to check type annotations
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

#    mypy --ignore-missing-imports src
    mypy src
)
