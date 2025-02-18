# Author: Michael Hurtado
# 02/18/2024
import spacy
from transformers import AutoTokenizer, AutoModel
from spacy.language import Language
import torch
import sys
import os
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Add the categories module to the system path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'categories')))
from categories import categories

# Construct the path to the model
spacy_lang_path = os.path.join("en_core_web_md", "en_core_web_md-3.7.1")

# Load the spaCy model
nlp = spacy.load(spacy_lang_path)

# Load the local model for sentence transformers
model_path = os.path.join("sent-trans")

# Check if the path exists
if not os.path.exists(model_path):
    print(f"Error: The path '{model_path}' does not exist. Please place the externally downloaded 'sent-trans' file in the same 'TicketClassifier' directory")
    sys.exit(1)  # Exit the program with a non-zero status

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModel.from_pretrained(model_path)

from spacy.tokens import Doc

# Register the extension on the Doc object to store classification scores
if not Doc.has_extension("cats"):
    Doc.set_extension("cats", default={})

# Cache category embeddings to avoid repeated computations
category_embeddings = {}
for label, texts in categories.items():
    label_embeddings = []
    for text in texts:
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        label_embedding = outputs.last_hidden_state.mean(dim=1).detach().numpy()
        label_embeddings.append(label_embedding)
    category_embeddings[label] = np.mean(label_embeddings, axis=0)

@Language.component("classify_text")
def classify_text(doc):
    """
    Classify the text in the doc using a pre-trained model and cosine similarity.
    
    Args:
        doc (Doc): The spaCy Doc object containing the text to classify.
        
    Returns:
        Doc: The Doc object with classification scores added as an extension.
    """
    inputs = tokenizer(doc.text, return_tensors="pt")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).detach().numpy()
    
    # Simple cosine similarity for classification
    scores = {label: cosine_similarity(embeddings, label_embedding.reshape(1, -1)).flatten()[0]
              for label, label_embedding in category_embeddings.items()}

    doc._.cats = scores
    return doc

# Add the custom component to the spaCy pipeline
nlp.add_pipe("classify_text", last=True)

def classify(text):
    """
    Classify the input text and return the classification scores.
    
    Args:
        text (str): The input text to classify.
        
    Returns:
        dict: A dictionary of classification scores, rounded to three decimal places.
    """
    doc = nlp(text)
    sorted_scores = dict(sorted(doc._.cats.items(), key=lambda item: item[1], reverse=True))
    
    # Round the scores to the nearest tenth and convert to regular floats
    rounded_scores = {label: round(float(score), 3) for label, score in sorted_scores.items()}
    
    # Filter scores to include only those above a threshold
    filtered_scores = {label: score for label, score in rounded_scores.items() if score >= 0.5}
    
    if not filtered_scores:
        return "NA"

    return filtered_scores