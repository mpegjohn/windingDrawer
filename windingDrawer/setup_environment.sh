#!/bin/bash
set -e

REQS=requirements_common.txt

VENV=ve_system

virtualenv $VENV

source $VENV/bin/activate

pip install -r $REQS

