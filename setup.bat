@echo off

:: Install Python dependencies
pip install -r requirements.txt

:: Download the spaCy models
python -m spacy download en_core_web_md

echo Setup complete!
pause