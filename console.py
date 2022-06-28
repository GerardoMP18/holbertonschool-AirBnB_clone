#!/usr/bin/python3
"""creating the command interpreter"""

from models.base_model import BaseModel
import cmd
import json


class HBNBCommand(cmd.Cmd):
    """
    the console
    """
    prompt = "(hbnb) "

    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
        ]
    __commands = ['all', 'count', 'create', 'destroy', 'show']

    def emptyline(self):
        pass

    def do_quit(self, arg): 
        raise SystemExit

    def do_EOF(self, arg):
        raise SystemExit

    def help_quit(self):
        print("Quit command used to exit the program")

    def help_EOF(self):
        print("EOF command used to exit the program")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
