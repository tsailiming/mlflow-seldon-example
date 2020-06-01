#!/bin/sh

mkdir -p /tmp/seldon
rm -rf /tmp/seldon/*

s2i build seldon registry.access.redhat.com/ubi8/python-36 registry.lab.ltsai.com/seldon-model:1.2 --as-dockerfile /tmp/seldon/Dockerfile -e MLFLOW_TRACKING_URI=$MLFLOW_TRACIKING_URI-e MLFLOW_RUN_ID=$MLFLOW_RUN_ID
buildah bud --build-arg AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID --build-arg AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY  --format=docker -t registry.lab.ltsai.com/seldon-model:1.2 /tmp/seldon
podman push registry.lab.ltsai.com/seldon-model:1.2 
