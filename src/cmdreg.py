# cmdreg.py

# cmdreg.py

from message_handler.message_types import error, info, done
import shlex  # Import the shlex module for parsing quoted arguments

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

            # Use shlex to parse the arguments, preserving quoted sections
            args = shlex.split(args_str)

            expected_args = command_info["args"]

            # Create separate lists for required and optional args
            required_args = [arg for arg in expected_args if not arg.startswith("[")]
            optional_args = [arg[1:-1] for arg in expected_args if arg.startswith("[")]

            # Prepare the args to match the required and optional args
            prepared_args = []
            for i, arg in enumerate(args):
                if i < len(required_args):
                    prepared_args.append(arg)
                elif i < len(expected_args):
                    prepared_args.append(arg)
                else:
                    error(f"Too many arguments. Usage: {command_name} {' '.join(expected_args)}")
                    return

            # Check if all required args are provided
            if len(prepared_args) < len(required_args):
                error(f"Too few arguments. Usage: {command_name} {' '.join(expected_args)}")
                return

            # Set optional args to None if not provided
            for _ in range(len(prepared_args), len(expected_args)):
                prepared_args.append(None)

            try:
                result = function_to_call(*prepared_args)
                done(result)
            except Exception as e:
                error(f"Error executing command: {str(e)}")

        else:
            error(f"Command '{command_name}' not found. Use 'help' to see available commands.")

# Register the "test" command with its description and arguments
registry = CommandRegistry()
registry.register("test", "modules.test", "test", "this is a test Command", ["[arg]"])
registry.register("table", "modules.table", "table", "you can create, delete or edit data set tables", ["action", "[table]", "[var1]", "[var2]"])
