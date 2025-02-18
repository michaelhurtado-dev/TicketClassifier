#!/bin/bash

# Install Python dependencies
pip3 install -r requirements.txt

# Download the spaCy model
python3 -m spacy download en_core_web_md
python3 -m spacy download en_core_web_lg 

