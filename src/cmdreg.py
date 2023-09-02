# cmdreg.py

from message_handler.message_types import error, info, done

class CommandRegistry:
    def __init__(self):
        self.commands = {}

    def register(self, command_name, module, function, description, args=None):
        self.commands[command_name] = {
            "module": module,
            "function": function,
            "description": description,
            "args": args if args else [],
        }

    def get_description(self, command_name):
        if command_name in self.commands:
            return self.commands[command_name]["description"]
        else:
            return "Command not found."

    def execute(self, command_name, args_str):
        if command_name in self.commands:
            command_info = self.commands[command_name]
            module = __import__(command_info["module"], fromlist=[command_info["function"]])
            function_to_call = getattr(module, command_info["function"])

            args = args_str.split()
            expected_args = command_info["args"]

            if len(args) < len(expected_args):
                error(f"Too few arguments. Usage: {command_name} {' '.join(expected_args)}")
            elif len(args) > len(expected_args):
                error(f"Too many arguments. Usage: {command_name} {' '.join(expected_args)}")
            else:
                try:
                    result = function_to_call(*args)
                    done(result)
                except Exception as e:
                    error(f"Error executing command: {str(e)}")

        else:
            error(f"Command '{command_name}' not found. Use 'help' to see available commands.")

# Register the "test" command with its description and arguments
registry = CommandRegistry()
registry.register("test", "modules.test", "testdef", "Description for the 'test' command", ["myarg2"])
