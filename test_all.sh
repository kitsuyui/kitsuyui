#!/usr/bin/env bash
set -x -euo pipefail

docker_test() {
  local dirname
  dirname="$1"
  cd "$dirname"
  docker build .
  cd -
}

docker_test tips/python-functional
docker_test tips/shellscript-editing-during-running
