#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the entry point of the command interpreter"""
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, arg):
        return True
    def do_Quit(self, arg):
        return True
    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()