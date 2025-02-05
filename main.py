#Author: Michael Hurtado
#02/04/2024
from model.load_model import classify, classify_text
from process_data.process_data import process, split_into_phrases
from load_data import load_data, write_data,json_to_csv
import json
import time

def get_tags_from_phrase(phrases, ticket):
    """
    Get tags from the given phrases using the classify function.
    
    Args:
        phrases (list): List of phrases to classify.
        ticket (dict): The ticket data.
        
    Returns:
        list: List of tags.
    """
    tags = []
    for phrase in phrases:
        if phrase.strip() != '':
            description_classification = classify(phrase)
            print(f" {phrase}: {description_classification}")
            first_element = next(iter(description_classification))
            if first_element != "N":
                tags.append(first_element)
    return tags

def update_ticket(ticket):
    """
    Update the ticket with the necessary fields and an empty tags list.
    
    Args:
        ticket (dict): The original ticket data.
        
    Returns:
        dict: The updated ticket data.
    """
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
    """
    Check if the text is too big to process.
    
    Args:
        text (str): The input text.
        
    Returns:
        bool: True if the text is too big, False otherwise.
    """
    return len(text.split()) > 512

def process_ticket(ticket):
    """
    Process the ticket to extract and classify tags from its description and short description.
    
    Args:
        ticket (dict): The ticket data.
        
    Returns:
        list: List of proposed tags.
    """
    print(f"Ticket: {ticket['number']}")
    print(f"Desc: {ticket['description']}")
    print("....Starting process now...")

    proposed_tags = []

    # Check if description is too large
    text_too_big(ticket['description'])

    print("....Analyzing ticket's description....")

    # Analyze 'Description'
    phrases = process(ticket['description'])
    print(phrases)
    proposed_tags = get_tags_from_phrase(phrases, ticket)
    print(f"From Description: {ticket['description']}, {proposed_tags}\n")

    # Check if description analysis is null
    if not proposed_tags:
        print("Description attempt #1 FAILED...beginning attempt #2")
        new_phrases = split_into_phrases(ticket['description'])
        print(new_phrases)
        proposed_tags = get_tags_from_phrase(new_phrases, ticket)

    # If 'description' labeled as null, 'user login' or 'nonsense' after second attempt then analyze 'action'
    if not proposed_tags or proposed_tags in [['User Login'], ['nonsense'], ['Image Viewer']]:
        if proposed_tags == ['User Login']:
            print("Description attempt #2 is general...analyzing 'action' for more potential details ")
        elif proposed_tags == ['nonsense']:
            proposed_tags = []
        else:
            print("Description attempt #2 FAILED...beginning action attempt #1 now ")

        phrases = process(ticket['short_description'])
        print(phrases)
        proposed_tags += get_tags_from_phrase(phrases, ticket)
        print(f"From Action: {ticket['short_description']}, {proposed_tags}\n")

    if not proposed_tags:
        print("Action attempt #1 FAILED...beginning attempt #2")
        new_phrases = split_into_phrases(ticket['short_description'])
        proposed_tags += get_tags_from_phrase(new_phrases, ticket)
        print(f"Action attempt #2: {ticket['short_description']}, {proposed_tags}\n")

    return proposed_tags if proposed_tags else "?"



def main():
    """
    Main function to load tickets, process them, and write the results.
    """
    tickets = load_data("data/data.json")
    results = []
    ticket_counter = 0

    for ticket in tickets:
        ticket_counter += 1
        tags = []
        updated_ticket = update_ticket(ticket)
        tags = process_ticket(ticket)
        print(updated_ticket['tags'])
        if not tags:
            updated_ticket['tags'].append("?")
        else:
            updated_ticket['tags'].append(list(set(tags)))
        results.append(updated_ticket)
        write_data("./results.json", results)
        print(f"Tags: {tags}")
        print("------------------\n")
        print(f"# Tickets processed: {ticket_counter}")

    json_to_csv('results.json','results.csv')

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time Elapsed: {elapsed_time}")
