#!/usr/bin/bash

# This is the script to run after all modifications to "Basics_filled.md" are complete

# Make sure that the "common" submodule is added
# Check if the submodule folder "common" is present
if [ ! -d "common" ]; then
  echo "common submodule doesn't exist. Adding now..."
  git submodule add git@github.com:DurhamARC-Training/common-tools-for-teaching.git common
fi

# Make sure it's up-to-date
echo "Updating common submodule..."
git submodule update --init --recursive

# Execute "filter_md.py" which reads the Markdown file with solutions and produces the Markdown file without solutions
python common/filter_md.py Intermediate_full.md Intermediate.md

# Convert both Markdown files into Jupyter notebooks
jupytext --to notebook Intermediate_full.md
jupytext --to notebook Intermediate.md

