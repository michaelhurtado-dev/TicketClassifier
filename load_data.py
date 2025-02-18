import pandas as pd
import json
import csv

def load_data(filepath):
    with open(filepath,'r',encoding= "utf-8") as f:
        try:
            data = json.load(f)
            print("JSON is valid")
        except json.JSONDecodeError as e:
            print(f"JSONDecodeError: {e}")
            # Print the part of the file where the error is
            f.seek(e.pos)
            print(f.read(100))
    tickets = data['records']
    return tickets
       

def write_data(filepath,data):
    with open (filepath,"w",encoding="utf-8") as f:
        json.dump(data,f,indent=4)

def json_to_csv(json_file, csv_file):
    """
    Convert JSON data to CSV format.
    
    Args:
        json_file (str): Path to the input JSON file.
        csv_file (str): Path to the output CSV file.
    """
    # Load JSON data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Open CSV file for writing
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write headers
        headers = data[0].keys()
        writer.writerow(headers)
        
        # Write data rows
        for entry in data:
            entry['tags'] = ', '.join([tag for sublist in entry['tags'] for tag in sublist])
            writer.writerow(entry.values())


        