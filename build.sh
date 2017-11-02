#!/bin/sh

docker build --no-cache -t dana/compile-rules . && docker push dana/compile-rules:latest
