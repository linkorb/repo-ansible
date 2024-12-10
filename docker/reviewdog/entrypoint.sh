#!/bin/bash

help=$(cat <<'EOQ'
all          - run checks for all files (DEFAULT)
fix          - automatically fix coding style when possible (WILL ATTEMPT TO FIX ALL FILES, NOT ONLY THOSE CHANGED)
pull-request - run checks for the latest changes (based on diff and pull request branch) - for CI use
...          - all other unknown arguments are passed to reviewdog
EOQ
)

fix=0
reviewdog_args='-filter-mode=nofilter'

for arg in "$@"; do
    if [ "$arg" = "help" ]; then
      echo "$help"; exit 0;
    elif [ "$arg" = "fix" ]; then
      fix=1
    elif [ "$arg" = "pull-request" ]; then
      reviewdog_args='-diff="git diff FETCH_HEAD" -reporter=github-pr-check'
    else
      reviewdog_args="$reviewdog_args $arg"
    fi
done

echo Running reviewdog $reviewdog_args
exec reviewdog $reviewdog_args
