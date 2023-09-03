import os
import json



folder_path = 'src/data'

# Ensure the folder exists; create it if it doesn't
if not os.path.exists(folder_path):
    os.makedirs(folder_path)


# Function to create a new table (JSON file)
def create_table(table_name):
    table = {}  # Initialize an empty table
    table_path = os.path.join(folder_path, f'{table_name}.json')
    
    with open(table_path, 'w') as jsonfile:
        json.dump(table, jsonfile)
    
    return table

# Function to add a new row (name) to the table
def add_row(table, name):
    if name not in table:
        table[name] = {}

# Function to add a value to a specific row (name) and column (key) in the table
def add_value(table, name, key, value):
    if name in table:
        table[name][key] = value

# Function to delete a table (JSON file)
def delete_table(folder_path, table_name):
    table_path = os.path.join(folder_path, f'{table_name}.json')
    
    if os.path.exists(table_path):
        os.remove(table_path)
        return True
    else:
        return False

