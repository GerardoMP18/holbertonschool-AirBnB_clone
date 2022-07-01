#!/usr/bin/python3
"""creating the command interpreter"""

from models.base_model import BaseModel
import cmd
import json
import models


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
        print()

    def help_EOF(self):
        print("EOF command used to exit the program")

    def do_create(self, arg):
        """
        Function that is responsible for creating a new instance
        based on the class and saves it in a json file and prints
        the ID"""
        if arg == "":
            print("** class name missing **")
        elif arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_create = eval(arg)()
            new_create.save()
            print(new_create.id)

    if __name__ == '__main__':
        HBNBCommand().cmdloop()
