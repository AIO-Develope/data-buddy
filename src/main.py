from cmdreg import registry  # Import the 'registry' object from cmdreg.py
from message_handler.message_types import error, done

# main.py

from cmdreg import registry

def main():
    while True:
        user_input = input("Buddy >> ").strip().lower()

        if user_input == "exit":
            break

        if user_input == "help":
            print("Available commands:")
            for command_name, command_info in registry.commands.items():
                print(f"{command_name}: {command_info['description']}")
            continue

        command_parts = user_input.split()
        command_name = command_parts[0]
        args_str = " ".join(command_parts[1:])  # Join the remaining parts as the arguments
        registry.execute(command_name, args_str)

        # The message handling is now done in cmdreg.py, so no need to handle it here.

if __name__ == "__main__":
    main()
