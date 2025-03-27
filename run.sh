#!/bin/zsh
ARG=$1
FOLDER="example_$ARG"
if [ ! -d "$FOLDER" ]; then
  echo "Folder '$FOLDER' doesn't exist."
  exit 1
fi
cd "$FOLDER" || exit 1
python serialize.py
python -m pickletools tsukimi.pickle
python deserialize.py