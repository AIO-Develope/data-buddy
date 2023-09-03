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

    # Check if the file already exists
    if os.path.exists(table_path):
        raise FileExistsError(f'Table with name "{table_name}" already exists.')

    with open(table_path, 'w') as jsonfile:
        json.dump(table, jsonfile)


# Function to add a new row (name) to the table
def add_row(table_name, name):
    table_path = os.path.join(folder_path, f'{table_name}.json')

    with open(table_path, 'r') as jsonfile:
        table = json.load(jsonfile)

    if name not in table:
        table[name] = []

    with open(table_path, 'w') as jsonfile:
        json.dump(table, jsonfile)



# Function to add a value to a specific row (name) in the table
def add_value(table_name, row, value):
    table_path = os.path.join(folder_path, f'{table_name}.json')

    with open(table_path, 'r') as jsonfile:
        table = json.load(jsonfile)

    if row in table:
        table[row].append(value)

    with open(table_path, 'w') as jsonfile:
        json.dump(table, jsonfile)


# Function to delete a table (JSON file)
def delete_table(table_name):
    table_path = os.path.join(folder_path, f'{table_name}.json')
    
    if os.path.exists(table_path):
        os.remove(table_path)
        return True
    else:
        return False
    

# Function to list all table names
def list_tables():
    table_files = [file for file in os.listdir(folder_path) if file.endswith('.json')]
    table_names = [os.path.splitext(file)[0] for file in table_files]
    print(table_names)
    return table_names


# Function to list all rows for a specific table
def list_rows(table_name):
    table_path = os.path.join(folder_path, f'{table_name}.json')

    with open(table_path, 'r') as jsonfile:
        table = json.load(jsonfile)

    return list(table.keys())


# Function to list all values for a specific row in a table
def list_values(table_name, row_name):
    table_path = os.path.join(folder_path, f'{table_name}.json')

    with open(table_path, 'r') as jsonfile:
        table = json.load(jsonfile)

    values = table.get(row_name, [])
    # Format values as a comma-separated string
    values_str = ", ".join(map(str, values))
    return values_str

