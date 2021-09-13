#!/bin/bash

# shellcheck disable=SC2093
#exec git init
# shellcheck disable=SC2093
exec git add -A
# shellcheck disable=SC2093
exec git commit -m "Auto-Commit"
# shellcheck disable=SC2093
#exec git remote add origin https://github.com/shreyakishore/git-auto-push-try.git
exec git push origin master
