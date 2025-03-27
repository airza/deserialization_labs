#!/bin/bash

LAB_NUM=$1
LAB_DIR="lab_${LAB_NUM}"

if [ ! -d "$LAB_DIR" ]; then
    echo "Directory $LAB_DIR does not exist!"
    exit 1
fi

docker build -t "lab_${LAB_NUM}" "$LAB_DIR"
docker run --rm -p 0.0.0.0:7777:7777 --name "lab_${LAB_NUM}" "lab_${LAB_NUM}"