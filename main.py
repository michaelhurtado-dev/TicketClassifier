
from load_data import load_data, write_data,json_to_csv
import json
import time
import argparse
from process_data.process_data import process, split_into_phrases
from ticket_process import get_tags_from_phrase, update_ticket, text_too_big, process_ticket

def testing_mode():
    """
    Function to test user input processing and tag extraction.
    """
    mode = input("Select mode (1 for sentence, 2 for full ticket), or type 'exit' to quit: ")
    
    while True:
        if mode == 'exit':
            break
        try:
            if mode == '1':
                user_input = input("Enter text (or type 'exit' to quit): ")
                if user_input.lower() == 'exit':
                    break
                phrases = process(user_input)
                tags = get_tags_from_phrase(phrases)
            elif mode == '2':
                desc_input = input("Enter description of ticket (or type 'exit' to quit): ")
                if desc_input.lower() == 'exit':
                    break
                short_desc_input = input("Enter short_description of ticket (or type 'exit' to quit): ")
                if short_desc_input.lower() == 'exit':
                    break
                test_ticket = {
                    'number': 'INC123456',
                    'description': desc_input,
                    'short_description': short_desc_input
                }
              
                
                start_time = time.time()
                process_ticket(test_ticket)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Time Elapsed V1: {elapsed_time}")
        
            else:
                print("Invalid mode selected.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

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
