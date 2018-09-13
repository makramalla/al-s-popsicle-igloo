#!/bin/bash


virtualenv env
source env/bin/activate

# Install pyang
pip install pyang

# Set environment variable for pyang plugin usage
export PYBINDPLUGIN=`echo $PWD`
echo $PYBINDPLUGIN
