#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the entry point of the command interpreter"""
import cmd
import re
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
        """shows command"""
        argument = arg.split()
        object_dictinory = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        instance_id = argument[1]
        new_obj = self.get_obj(instance_id, model)
        if new_obj:
            print(new_obj)
        else:
            print('** no instance found **')
if __name__ == '__main__':
    HBNBCommand().cmdloop()