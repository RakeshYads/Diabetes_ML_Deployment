#!/bin/bash

# Building packages and uploading them to a Gemfury repository
GEMFURY_URL=$GEMFURY_PUSH_URL #need to define the url

set -e #any script command fails, exit the script

DIRS="$@"  #get all the arguments. Check "$@" vs "$*". Also without colon.
echo "$DIRS"
BASE_DIR=$(pwd)  #get the present working directory. It's environmnet dependent. Not $PWD.
SETUP="setup.py"

warn() {
    echo "$@" 1>&2  #It redirects stddout to stderr. 1 = stdout and 2 = stderr. So this will
    #output the message to stderr.
}

die() {
    warn "$@"
    exit 1
    #exit code 0 - Success
    #exit code 1 - General errors, Miscellaneous errors
    #exit code 2 - Misuse of shell builtins(according to bash documentation)
}

build() {
    DIR="${1/%\//}" #escape characters
    echo "Checking directory $DIR"
    cd "$BASE_DIR/$DIR"
    [ ! -e $SETUP ] && warn "No $SETUP file, skipping" && return  #Checking whether the file exists or not
    PACKAGE_NAME=$(python $SETUP --fullname) # $() vs ${} - It is used for value substitution by executing the command
    #In python terminal, it gives the output with name + version from setup.py file. It's a python command.
    echo "Package $PACKAGE_NAME"
    python "$SETUP" sdist bdist_wheel || die "Building package $PACKAGE_NAME failed"
    for X in $(ls dist)
    do
        curl -F package=@"dist/$X" "$GEMFURY_URL" || die "Uploading package $PACKAGE_NAME failed on file dist/$X"
    done
}

if [ -n "$DIRS" ]; then   #-n signifies not zero length
    for dir in $DIRS; do
        build $dir
    done
else
    ls -d */ | while read dir; do #-d is a directory  /* - gives all directories
    # | - pipe is used to pass output of one command as input to other
        build $dir
    done
fi