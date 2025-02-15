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