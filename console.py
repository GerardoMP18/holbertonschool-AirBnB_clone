#!/usr/bin/python3
"""creating the command interpreter"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import json


class HBNBCommand(cmd.Cmd):
    """
    the console
    """
    prompt = "(hbnb) "

    __classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
        ]

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
        Methods that is responsible for creating a new instance
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

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        args = arg.split(" ")
        if arg == '':
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id_instance = storage.all()
            string = "{}.{}".format(args[0], args[1])
            if string not in id_instance:
                print("** no instance found **")
            else:
                print("{}".format(id_instance[string]))

    def do_destroy(self, arg):
        """removes an instance based on class
           name, ID and saves it to a json file"""
        args = arg.split(" ")
        if arg == '':
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            id_instance = storage.all()
            string = "{}.{}".format(args[0], args[1])
            if string not in id_instance:
                print("** no instance found **")
            else:
                del (id_instance[string])
                storage.save()

    def do_all(self, arg):
        """
        methods that prints all string representations
        of all instances based or not on class name
        """
        list = []
        all_directory = storage.all()
        if arg == "":
            for keys, values in all_directory.items():
                list.append(str(values))
            print(list)
        elif arg in self.__classes:
            for keys, values in all_directory.items():
                if values.__class__.__name__ == arg:
                    list.append(str(values))
            print(list)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """
        methods to update an instance based on class name and
        id by adding or updating the attribute that saves the
        change in the json file
        """
        args = arg.split(" ")
        if arg == '':
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            id_instance = storage.all()
            string = "{}.{}".format(args[0], args[1])
            if string not in id_instance:
                print("** no instance found **")
            elif len(args) == 2:
                print("** attribute name missing **")
            elif len(args) == 3:
                print("** value missing **")
            else:
                unmodifiable = ["id", "created_at", "updated_at"]
                if args[2] not in unmodifiable:
                    for key, value in id_instance.items():
                        setattr(value, args[2], eval(args[3]))
                        value.save()

    def do_count(self, arg):
        """Instance counter according to class"""
        args = arg.split(" ")
        if arg not in self.__classes:
            print("** class doesn't exist **")
        else:
            list_new = []
            list_dictionary = storage.all()
            for key, value in list_dictionary.items():
                if args[0] in key:
                    list_new.append(value)
            print(len(list_new))

    def default(self, arg):
        """
        cmd method to validate when it does not
        recognize the prefix of the command.
        """
        args = arg.split(".")
        if args[0] in self.__classes:
            if args[1] == "all()":
                nameClass = args[0]
                return self.do_all(nameClass)
            elif args[1] == "count()":
                nameClass = args[0]
                return self.do_count(nameClass)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
