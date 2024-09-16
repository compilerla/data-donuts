#!/usr/bin/env bash
set -eu

git config --global --add safe.directory /home/compiler/site

# initialize hook environments
pre-commit install --install-hooks --overwrite

# manage commit-msg hooks
pre-commit install --hook-type commit-msg
