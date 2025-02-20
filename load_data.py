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

import json
import csv

def json_to_csv(json_file_path, csv_file_path):
    # Read the JSON data from the file
    with open(json_file_path, 'r') as jsonfile:
        json_data = json.load(jsonfile)
    
    # Extract all unique keys from the JSON data
    keys = set()
    for record in json_data:
        keys.update(record.keys())
    
    # Convert the set of keys to a list, ensuring 'tags' is at the end
    keys = list(keys)
    if 'tags' in keys:
        keys.remove('tags')
        keys.append('tags')
    
    # Open the CSV file for writing
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        
        # Write the header row
        csv_writer.writerow(keys)
        
        # Write the data rows
        for record in json_data:
            row = []
            for key in keys:
                value = record.get(key, "")
                if isinstance(value, list):
                     value = ", ".join([", ".join(sublist) if isinstance(sublist, list) else str(sublist) for sublist in value])
                elif isinstance(value, str):
                    value = value.replace("\r\n", " ").replace("\n", " ")
                row.append(value)
            csv_writer.writerow(row)




        