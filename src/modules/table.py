import modules.data_logic as logic


def table(action, name, edit):
    if action == "create":
        logic.create_table(name)
