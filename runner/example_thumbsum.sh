#!/bin/bash

#pyCharm will run in project root directory. Check if we are here and if so then change to directory
if [ -d "./runner" ]; then
  echo "Changing into services directory"
  cd ./runner
fi


PYTHON_CMD=python3
if [ E${EXTPYTHONCMD} != "E" ]; then
  PYTHON_CMD=${EXTPYTHONCMD}
fi

if [ ! -d ./example_basedir ]; then
  mkdir ./example_basedir
fi

export CDRUNNER_GLOBCONFIGFILE="$(pwd)/example_globalConfig.yml"

echo "AA"
echo $(pwd)

${PYTHON_CMD} ./src/cd_runner.py ./example_thumbsum.yml "$@"

