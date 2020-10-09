#!/bin/sh

cd "$(dirname "$0")"

version=$(cat VERSION)

# Just remove the -v volume allocation to serve static files from docker image
docker run -ti --rm -p 4000:4000 -v "$PWD":/myapp/ --name tagtog_doc tagtog-doc:"$version" $@
