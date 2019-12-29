#!/bin/sh -e
#
# Reset the python env: Remove all packages and reinstall from requirements
#
# Use to provide a clean environment or on updated requirements
#
if [ "$(uname -s)" = "Darwin" ]; then
    # If called through a symlink, this will point to the symlink
    THIS_SCRIPT_DIR="$( cd "$( dirname "${0}" )" && pwd )"
else
    THIS_SCRIPT_DIR=$(dirname $(readlink -f "${0}"))
fi
(
    # Work in repo root
    cd ${THIS_SCRIPT_DIR}/..

    pip freeze | xargs pip uninstall -y
    pip install -r requirements-dev.txt
)
