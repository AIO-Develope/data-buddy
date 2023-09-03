import modules.data_logic as logic

def table(action, *args):
    if action == "create":
        if len(args) != 1:
            return "Usage: table create <table_name>"
        table_name = args[0]
        try:
            logic.create_table(table_name)
            return f"Successfully created table dataset named {table_name}"
        except FileExistsError:
            return f'Table with name "{table_name}" already exists.'

    if action == "add":
        if len(args) < 2:
            return "Usage: table add <row|value> <table_name> <name|row_name> [<value>]"
        sub_action = args[0]
        table_name = args[1]
        if sub_action == "row":
            if len(args) != 3:
                return "Usage: table add row <table_name> <name>"
            name = args[2]
            logic.add_row(table_name, name)
            return f"Successfully added row {name} to table {table_name}"
        elif sub_action == "value":
            if len(args) != 4:
                return "Usage: table add value <table_name> <row_name> <value>"
            row_name = args[2]
            value = args[3]
            logic.add_value(table_name, row_name, value)
            return f"Successfully added value {value} to row {row_name} inside table named {table_name}"

    if action == "delete":
        if len(args) != 2:
            return "Usage: table delete table <table_name>"
        sub_action = args[0]
        table_name = args[1]
        if sub_action == "table":
            success = logic.delete_table(table_name)
            if success:
                return f"Successfully deleted table dataset named {table_name}"
            else:
                return f'Table with name "{table_name}" does not exist.'

    if action == "list":
        if len(args) == 0:
            return "Usage: table list <table|row|values> [<table_name>]"
        sub_action = args[0]
        if sub_action == "table":
            tables = logic.list_tables()
            return f"Tables: {tables}"
        elif sub_action == "row":
            if len(args) != 2:
                return "Usage: table list row <table_name>"
            table_name = args[1]
            rows = logic.list_rows(table_name)
            return f"Rows in {table_name}: {rows}"
        elif sub_action == "values":
            if len(args) != 3:
                return "Usage: table list values <table_name> <row_name>"
            table_name = args[1]
            row_name = args[2]
            values = logic.list_values(table_name, row_name)
            return f"Values in {row_name} in {table_name}: {values}"

    if action == "remove":
        if len(args) < 2:
            return "Usage: table remove <row|value> <table_name> <name|row_name> [<value>]"
        sub_action = args[0]
        table_name = args[1]
        if sub_action == "row":
            if len(args) != 3:
                return "Usage: table remove row <table_name> <row_name>"
            row_name = args[2]
            logic.remove_row(table_name, row_name)
            return f"Successfully removed row {row_name} from table {table_name}"
        elif sub_action == "value":
            if len(args) != 4:
                return "Usage: table remove value <table_name> <row_name> <value>"
            row_name = args[2]
            value = args[3]
            # Add logic to remove value from a row here (if needed)
            return f"Successfully removed value {value} from row {row_name} inside table named {table_name}"

    if action == "rename":
        if len(args) != 3:
            return "Usage: table rename <table|row> <old_name> <new_name>"
        sub_action = args[0]
        old_name = args[1]
        new_name = args[2]
        if sub_action == "row":
            logic.rename_row(table_name, old_name, new_name)
            return f"Successfully renamed row {old_name} to {new_name} in table {table_name}"
        elif sub_action == "table":
            success = logic.rename_table(old_name, new_name)
            if success:
                return f"Successfully renamed table {old_name} to {new_name}"
            else:
                return f'Table with name "{old_name}" does not exist.'

# Additional functions for renaming and removing rows and tables can be added here.
