#!/bin/sh
set -x -euo pipefail

docker_test() {
  local dirname
  dirname="$1"
  cd "$dirname"
  docker build .
  cd -
}

docker_test tips/python-functional
