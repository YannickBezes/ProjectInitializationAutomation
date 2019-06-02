#!/bin/bash

function create() {
    cd /media/sf_sandbox/Perso/ProjectInitializationAutomation
    python create.py $1
    cd /media/sf_sandbox/Perso/$1
    git init
    git remote add origin git@github.com:YannickBezes/$1.git
    touch README.md
    git add .
    git commit -m "Initial commit"
    git push -u origin master
    code .
}


function remove() {
    cd /media/sf_sandbox/Perso/ProjectInitializationAutomation
    python remove.py $1
    rm -Rf /media/sf_sandbox/Perso/$1
}