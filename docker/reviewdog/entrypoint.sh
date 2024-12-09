#!/bin/bash

help=$(cat <<'EOQ'
all - run checks for all files (DEFAULT)

fix - automatically fix coding style when possible (WILL ATTEMPT TO FIX ALL FILES, NOT ONLY THOSE CHANGED)

pull-request - run checks for the latest changes (based on diff and pull request branch) - for CI use
EOQ
)

fix=0
reviewdog_args="-filter-mode=nofilter"

for arg in "$@"; do
    if [ "$arg" = "help" ]; then
      echo "$help"; exit 0;
    fi

    if [ "$arg" = "fix" ]; then
      fix=1
    fi

    if [ "$arg" = "pull-request" ]; then
      reviewdog_args="-diff='git diff FETCH_HEAD' -reporter=github-pr-check"
    fi
done

exec reviewdog "$reviewdog_args"
