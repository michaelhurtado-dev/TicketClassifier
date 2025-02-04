import pandas as pd
import json

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

        