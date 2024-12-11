#!/bin/bash

# TODO add this feature at a later time, to make it convenient to quickly fix reported coding style errors
#fix          - automatically fix coding style when possible (WILL ATTEMPT TO FIX ALL FILES, NOT ONLY THOSE CHANGED)

help=$(cat <<'EOQ'
all          - run checks for all files (DEFAULT)
pull-request - run checks for the latest changes (based on diff and pull request branch) - for CI use
bash         - run bash instead
...          - all other unknown arguments are passed to reviewdog
EOQ
)

fix=0
cmd="reviewdog"
reviewdog_args=('-filter-mode=nofilter')

for arg in "$@"; do
    if [ "$arg" = "help" ]; then
      echo "$help"; exit 0;
    elif [ "$arg" = "fix" ]; then
      fix=1
    elif [ "$arg" = "bash" ]; then
      cmd=bash
      reviewdog_args=()
    elif [ "$arg" = "pull-request" ]; then
      reviewdog_args=("-diff=git diff FETCH_HEAD")
      reviewdog_args+=("-reporter=local")
    else
      reviewdog_args+=("$arg")
    fi
done

git config --global --add safe.directory /app
echo $cmd "${reviewdog_args[@]}" >&2
exec $cmd "${reviewdog_args[@]}"
