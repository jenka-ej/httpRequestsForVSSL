#!/bin/bash
cd httpScripts
. venv/bin/activate
flask --app hello run --host=0.0.0.0
