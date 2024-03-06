#!/usr/bin/env python3
"""Module for class HBNBCommand that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """contains the entry point of the command interpreter
    """

    prompt = "(hbnb)"
    def do_create(self, arg):
        """create command
        """
        print('create')

    def help_create(self):
        """help for create command
        """
        print('\n'.join([ 'create [person]',
                           'Create a new BaseModel',
                           ]))

    def do_show(self, arg):
        """show command
        """
        print('show')

    def help_show(self):
        """help for show command
        """
        print('\n'.join([ 'show [person]',
                           'show a new BaseModel',
                           ]))

    def do_destroy(self, arg):
        """destroy command
        """
        print('destroy')

    def help_destroy(self):
        """help for destroy command
        """
        print('\n'.join([ 'destroy [person]',
                           'destroy a new BaseModel',
                           ]))

    def do_all(self, arg):
        """all command
        """
        print('all')

    def help_all(self):
        """help for all command
        """
        print('\n'.join([ 'all [person]',
                           'all a new BaseModel',
                           ]))

    def do_update(self, arg):
        """update command
        """
        print('update')

    def help_update(self):
        """help for update command
        """
        print('\n'.join([ 'update [person]',
                           'update a new BaseModel',
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
