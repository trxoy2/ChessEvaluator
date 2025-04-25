#!/bin/bash

set -e  # Exit immediately if a command fails
set -o pipefail  # Catch errors in piped commands

install_dependencies() {
    if [[ -f "requirements.txt" ]]; then
        echo "----------------Installing dependencies..."
        pip install -r requirements.txt --no-warn-script-location
    fi
}

run_step() {
    local step_name=$1
    local script_path=$2

    echo "----------------Running $step_name..."
    python -u "$script_path"

    if [ $? -ne 0 ]; then
        echo "$step_name failed. Aborting pipeline."
        exit 1
    fi
}

main() {
    install_dependencies
    
    run_step "Extract_Load" "./src/extract_load.py"
    run_step "Transform" "./src/transform.py"
    run_step "Queries" "./src/run_queries.py"

    echo "ELT Pipeline completed successfully."
}

main "$@"



# This Bash script automates the execution of an ELT (Extract, Load, Transform) pipeline.
# It ensures that dependencies are installed, executes each step in sequence, and handles errors gracefully.
#
# 1. **Dependency Installation**: 
#    - If a `requirements.txt` file exists, it installs the necessary Python packages.
#
# 2. **Pipeline Execution**: 
#    - Runs each step of the ELT process in order:
#      - `extract_load.py`: Extracts data from a CSV and loads it into a database.
#      - `transform.py`: Cleans, validates, and enriches the data.
#      - `run_queries.py`: Executes analytical queries on the transformed data.
#
# 3. **Error Handling**: 
#    - The script stops execution if any step fails, preventing further processing of potentially invalid data.
#    - The `set -e` flag ensures that the script exits immediately on any error.
#    - The `set -o pipefail` flag ensures errors in piped commands are caught.
#
# 4. **Logging**:
#    - Provides clear console messages to indicate progress and failures.
#
# Once all steps complete successfully, a message confirms the pipeline's success.
