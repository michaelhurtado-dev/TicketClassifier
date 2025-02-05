#Author: Michael Hurtado
#02/04/2024

import re
import spacy
from spacy.language import Language

# Load the spaCy model
nlp = spacy.load("../en_core_web_md/en_core_web_md-3.7.1")

# Define patterns to be removed from the text
patterns = [
    r"Selected Issue: Other",
    r"Selected Issue: IRIS",
    r"Selected Issue:",
    r"selected issue:",
    r"selected issue",
    r"IRIS \(Integrated Rx Information System\) - IRIS \(Integrated Rx Information System\)",
    r"IRIS \(Integrated Rx Information System\)",
    r"IRIS (Integrated Rx Information System)",
    r"\(Integrated Rx Information System\)",
    r"INTEGRATED RX INFORMATION SYSTEM",
    r"IRIS",
    r"Iris",
    r"iris",
    r"MSA ORACLE EBS \(RXS\) - SPT   --   ",
    r"\(Prior Authorization System\)",
    r"Call Center Pilot:",
    r"\(\)",
    r"--",
    r"-",
    r"Informational"
    # Add more patterns as needed
]

def handle_contractions(text):
    """
    Replace contractions in the text with their full forms.
    
    Args:
        text (str): The input text.
        
    Returns:
        str: The text with contractions replaced.
    """
    if not isinstance(text, str):
        raise TypeError("Expected a string or bytes-like object")
    
    contractions = {
        "can't": "cannot",
        "won't": "will not",
        "n't": " not",
        "'re": " are",
        "'s": " is",
        "'d": " would",
        "'ll": " will",
        "'t": " not",
        "'ve": " have",
        "'m": " am"
    }
    
    for contraction, full_form in contractions.items():
        text = re.sub(contraction, full_form, text)
    
    return text

def preprocess_description(description, patterns):
    """
    Preprocess the description by removing specified patterns and normalizing the text.
    
    Args:
        description (str): The input description.
        patterns (list): A list of regex patterns to remove from the description.
        
    Returns:
        str: The preprocessed description.
    """
    frm_pattern = r"FRM[- ]\d{5}"
    ora_pattern = r"(?i)ORA[- ]\d{5}"
    loc_pattern = r"(?i)[a-z]{2}\d{3}"
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    selected_issue_pattern = r'Selected Issue: .* -'
    
    for pattern in patterns:
        description = re.sub(pattern, '', description)
    
    description = re.sub(frm_pattern, 'FRM ', description)
    description = re.sub(ora_pattern, 'ORA ', description)
    description = re.sub(loc_pattern, '', description)
    description = re.sub(email_pattern, '', description)
    description = re.sub(selected_issue_pattern, '', description)
    
    description = description.lower()
    
    return description

def split_into_phrases(text):
    """
    Split the text into phrases based on conjunctions and punctuation.
    
    Args:
        text (str): The input text.
        
    Returns:
        list: A list of phrases.
    """
    text = handle_contractions(text)
    text = preprocess_description(text, patterns)
    doc = nlp(text)
    phrases = []
    current_phrase = []
    
    for token in doc:
        if token.dep_ == 'cc' or token.dep_ == 'punct':
            if current_phrase:
                phrases.append(' '.join(current_phrase).strip())
            current_phrase = []
        else:
            current_phrase.append(token.text)
    
    if current_phrase:
        phrases.append(' '.join(current_phrase).strip())
    
    return phrases

def process(text):
    """
    Process the text to handle contractions, preprocess descriptions, and split into sentences.
    
    Args:
        text (str): The input text.
        
    Returns:
        list: A list of processed sentences.
    """
    processed_list = []
    text = handle_contractions(text)
    text = preprocess_description(text, patterns)
    doc = nlp(text)
    sentences = list(doc.sents)
    
    for sent in sentences:
        processed_list.append(sent.text)
    
    return processed_list
