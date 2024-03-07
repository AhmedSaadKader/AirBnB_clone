#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the entry point of the command interpreter
"""
import cmd
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter
    """

    prompt = "(hbnb)"
    def do_create(self, line):
        """create command
        """
        if not line:
            print("** class name missing **")
        elif line not in ['BaseModel']:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print(f'{new_model.id}')

    def help_create(self):
        """help for create command
        """
        print('\n'.join(['Usage: create [model]',
                        'Create a new instance of [model], \
saves it (to [file.json] and prints the [id])',
                            'Ex: create BaseModel'
                        ]))

    def do_show(self, line):
        """show command
        """
        args = line.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        model = args[0]
        if model not in ['BaseModel']:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print('** instance id missing **')
            return
        instance_id = args[1]
        all_objects = storage.all()
        for obj_id in all_objects.keys():
            pattern = f"\.{instance_id}$"
            if re.search(pattern, obj_id):
                obj = all_objects[obj_id]
                new_obj = BaseModel(**obj)
                print(new_obj)
                return
        print('** no instance found **')

    def help_show(self):
        """help for show command
        """
        print('\n'.join(['Usage: show <model> <id>',
                        'Prints the string representation of an instance \
based on the class nam and [id]',
                        'Ex: show BaseModel 1234-1234-1234'
                        ]))

    def do_destroy(self, arg):
        """destroy command
        """
        print('destroy')

    def help_destroy(self):
        """help for destroy command
        """
        print('\n'.join(['Usage: destroy <model> <id>',
                        'Deletes an instance based on the class name and id, \
(save the change into the JSON file [file.json])',
                        'Ex: destroy BaseModel 1234-1234-1234'
                        ]))

    def do_all(self, arg):
        """all command
        """
        all_objects = storage.all()
        for obj_id in all_objects.keys():
            obj = all_objects[obj_id]
            new_obj = BaseModel(**obj)
            print(new_obj)

    def help_all(self):
        """help for all command
        """
        print('\n'.join(['Usage: all <model>',
                        'Prints all string representation of all instances \
based or not on the class name',
                        'Ex: $ all BaseModel or $ all',
                        ]))

    def do_update(self, arg):
        """update command
        """
        print('update')

    def help_update(self):
        """help for update command
        """
        print('\n'.join(['Usage: update <class name> <id> <attribute name> "<attribute value>"',
                        'Updates an instance based on the class name and id by \
adding or updating attribute (save the change into the JSON file).',
                        'Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"',
                        ]))

    def do_EOF(self, arg):
        """exits the command
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
