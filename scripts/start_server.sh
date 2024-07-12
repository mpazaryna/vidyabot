#!/bin/bash
# File: scripts/start_server.sh

# Get the directory of the script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Change to the project root directory
cd "$DIR/.."

# Unset Anaconda-related environment variables
unset CONDA_PREFIX
unset CONDA_DEFAULT_ENV
unset CONDA_PYTHON_EXE

# Get the path to the Poetry environment's Python
POETRY_PYTHON=$(poetry run which python)

# Activate the Poetry environment
source $(poetry env info --path)/bin/activate

# Start the server using the Poetry environment's Python
nohup $POETRY_PYTHON -m uvicorn api.src.main:app --host 0.0.0.0 --port 8000 --log-level info --no-access-log --log-file server.log > /dev/null 2>&1 &

# Save the PID
echo $! > server.pid

echo "Server started with PID $(cat server.pid). Logs are being written to server.log"