#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the entry point of the command interpreter"""
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, arg):
        return True
    def do_quit(self, arg):
        return True
    def emptyline(self):
        pass
    def do_create(self, arg):
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")

    def do_show(self, arg):
if __name__ == '__main__':
    HBNBCommand().cmdloop()