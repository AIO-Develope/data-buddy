import modules.data_logic as logic

def table(action, table, var1, var2):
    if action == "create":
        logic.create_table(table)
        return f"Successfully created table dataset named {table}"

    if action == "add_row":
        logic.add_row(table, var1)
        return f"Successfully added row {var1} to table {table}"
    
    if action == "add_value":
        logic.add_value(table, var1, var2)
        return f"Successfully added value {var1} to row {var2} inside table named {table}"
    
    if action == "delete":
        logic.delete_table(table)
        return f"Successfully deleted table dataset named {table}"
    
    if action == "list":
        tables = logic.list_tables()
        return f"Tables: {tables}"
    
    if action == "list_rows":
        rows = logic.list_rows(table)
        return f"Rows in {table}: {rows}"
    
    if action == "list_values":
        values = logic.list_values(table, var1)
        return f"Values in {var1} in {table}: {values}"

    # Add functions for renaming and removing rows and tables here
    if action == "remove_row":
        logic.remove_row(table, var1)
        return f"Successfully removed row {var1} from table {table}"
    
    if action == "rename_row":
        logic.rename_row(table, var1, var2)
        return f"Successfully renamed row {var1} to {var2} in table {table}"

    if action == "rename_table":
        logic.rename_table(table, var1)
        return f"Successfully renamed table {table} to {var1}"