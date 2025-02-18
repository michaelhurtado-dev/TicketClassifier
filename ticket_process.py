
from model.load_model import classify
from process_data.process_data import process, split_into_phrases



def get_tags_from_phrase(phrases):
    tags = []
    for phrase in phrases:
        if phrase.strip() != '':
            description_classification = classify(phrase)
            print(f"Phrase: {phrase}: {description_classification}")
            first_element = next(iter(description_classification))
            if first_element != "N":
                tags.append(first_element)
    return tags

def update_ticket(ticket):
    updated_ticket = {
        "number": ticket['number'],
        "description": ticket['description'],
        "short_description": ticket['short_description'],
        "u_error_symptoms": ticket['u_error_symptoms'],
        "sys_created_on": ticket['sys_created_on'],
        "tags": []
    }
    return updated_ticket

def text_too_big(text):
    return len(text.split()) > 512


def process_ticket(ticket):
    # List of fields which the algo will use to predict categories
    relevant_fields = ['description', 'short_description']

    # Set to which this algo will append its categorization predictions
    proposed_tags = set()
    # Variable to store the text that has already been processed
    processed_texts = set()

    print(f"\n****Processing Ticket: {ticket['number']}****")

    # Iterate through the specified relevant_fields list
    for field in relevant_fields:
        print(f"\n...Checking {field}...")
        # Get raw text from the field of the ticket
        raw_text = ticket[field]

         # Check if the text has already been processed
        if raw_text in processed_texts:
            print(f"...Skipping {field} as it is a duplicate...")
            continue

        # Add the text to the set of processed texts
        processed_texts.add(raw_text)

        # Check whether the raw_text is too large
        text_too_big(raw_text)


        # Split raw_text into phrases and get the tags
        phrases = process(raw_text)
        proposed_tags.update(get_tags_from_phrase(phrases))

        # If no tags are collected then break up the raw_text further and repeat again
        if not proposed_tags:
            print("...Breaking raw text up for better results...")
            smaller_phrases = split_into_phrases(raw_text)
            proposed_tags.update(get_tags_from_phrase(smaller_phrases))

    if proposed_tags:
        print(f"Predicted: {list(proposed_tags)}")
    else:
        print(f"Predicted: ?")

    return list(proposed_tags) if proposed_tags else "?"

