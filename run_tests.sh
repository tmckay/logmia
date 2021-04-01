#!/bin/sh

docker build --tag logmia .
docker run logmia
