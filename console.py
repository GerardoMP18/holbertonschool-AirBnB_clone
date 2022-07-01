#!/usr/bin/python3
"""creating the command interpreter"""

from models.base_model import BaseModel
from models import storage
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

    def do_show(self, arg):
        """Prints the string representation of an instance based 
        on the class name and id"""
        args = arg.split(" ")
        if arg == '':
            print("** class name missing **")
        elif args[0] not in self.__classes:
                print("** class doesn't exist **")
        elif len(args) < 2:
                print("** instance id missing **")
        else:
            id_instance = models.storage.all()
            string = "{}.{}".format(args[0],args[1])
            if string not in id_instance:
                print("** no instance found **")
            else:
                print("{}".format(id_instance[string]))

    def do_all(self, arg):
        """Prints all string representation of 
        all instances based or not on the class name"""
        try:
            list = []
            argu = arg.split()

            if argu and argu[0] not in self.__classes:
                print("** class doesn't exist **")

            for key, value in storage.all().items():
                if (not argu or argu[0] is None or
                        argu[0] == type(value).__name__):
                    list.append(str(value))

            print(list)
        except Exception as exception:
            print(exception.argu[0])

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
