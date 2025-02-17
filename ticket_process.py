
from model.load_model import classify
from process_data.process_data import process, split_into_phrases

def get_tags_from_phrase(phrases, ticket):
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
    print(f"Ticket: {ticket['number']}")
    print(f"Desc: {ticket['description']}")
    print("....Starting process now...")

    proposed_tags = []

    text_too_big(ticket['description'])

    print("....Analyzing ticket's description....")

    phrases = process(ticket['description'])
    print(phrases)
    proposed_tags = get_tags_from_phrase(phrases, ticket)
    print(f"From Description: {ticket['description']}, {proposed_tags}\n")

    if not proposed_tags:
        print("Description attempt #1 FAILED...beginning attempt #2")
        new_phrases = split_into_phrases(ticket['description'])
        print(new_phrases)
        proposed_tags = get_tags_from_phrase(new_phrases, ticket)

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
