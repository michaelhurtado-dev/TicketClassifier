
from load_data import load_data, write_data,json_to_csv
import json
import time
import argparse
from ticket_process import get_tags_from_phrase, update_ticket, text_too_big, process_ticket

def testing_mode():
    while True:
        user_input = input("Enter text (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        phrases = process(user_input)
        tags = get_tags_from_phrase(phrases, {})
        print(f"Tags: {tags}")

def main():
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
    parser = argparse.ArgumentParser(description="Process tickets or enter testing mode.")
    parser.add_argument('-t', '--test', action='store_true', help="Enter testing mode")
    args = parser.parse_args()

    if args.test:
        testing_mode()
    else:
        start_time = time.time()
        main()
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Time Elapsed: {elapsed_time}")
