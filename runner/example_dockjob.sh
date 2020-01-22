#!/bin/bash

PYTHON_CMD=python3
if [ E${EXTPYTHONCMD} != "E" ]; then
  PYTHON_CMD=${EXTPYTHONCMD}
fi

export CDRUNNER_GLOBCONFIGFILE="$(pwd)/example_globalConfig.yml"

${PYTHON_CMD} ./src/cd_runner.py ./example_dockjob.yml

