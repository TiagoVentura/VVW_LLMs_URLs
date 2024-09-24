#!/bin/bash

# Path to the Conda initialization script
source /Users/tb186/anaconda3/etc/profile.d/conda.sh

# Activate the Conda environment
conda activate china_project

# change working directory
cd /Users/tb186/Dropbox/artigos/VVW_LLMs_urls

# Run the Python script
python3 /Users/tb186/Dropbox/artigos/VVW_LLMs_urls/code/scrap_newsapi.py

# Deactivate the environment
conda deactivate


