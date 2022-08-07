#!/bin/bash

function create-project() {
    
    project_name=$1
    project_type=$2
    cd /mnt/e/MasterProgrammer/$project_type
    mkdir $project_name
    cd $project_name
    touch README.md

    echo "#" $project_name > README.md

    if [ "$project_type" = "js" ]; then
        touch index.html style.css index.js
    elif [ "$project_type" = "html-css" ]; then
        touch index.html style.css
    else
        touch main.py
    fi

    git init
    git add *
    git commit -m "initial commit"

    code .
}
