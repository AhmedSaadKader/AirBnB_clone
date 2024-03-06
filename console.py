#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter
    """

    prompt = "(hbnb)"

    def do_EOF(self, arg):
        """exits the command

        Returns:
            True: End cmd
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
