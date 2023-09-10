#!/usr/bin/python3

"""Defines the HBnB console"""

import cmd
import models
from models.base_model import BaseModel
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from datetime import datetime
from shlex import shlex
"""entry point for hbnb console"""


class HBNBCommand(cmd.Cmd):
    """ hbnb shell """
    prompt = '(hbnb) '
    classes = {'BaseModel': BaseModel, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review,
               'User': User}

    def emptyline(self):
        """empty line"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF to exit the program
        """
        return True

    def do_create(self, arg):  # creates a new object or record
        """Creates a new instance of BaseModel, saves it and prints the id"""
        args = arg.split()  # splits a string into a list of substrings
        if len(args) == 0:  # means no class name was provided
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            new_object = eval(f"{args[0]}")()  # creates an instance
            print(new_object.id)  # prints id attribute of the class

    def do_show(self, arg):  # displays information about an object
        """Show instance based on id"""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[f"{args[0]}.{args[1]}"])

    def do_destroy(self, arg):
        """destroy instance based on id
        deletes or removes an existing object or record
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            del storage.all()[f"{args[0]}.{args[1]}"]
        storage.save()[f"{args[0]}.{args[1]}"]

    def do_all(self, arg):
        """Prints all instances based or not on the class name
        """
        args = arg.split()
        if len(args) == 0:
            print([str(value) for value in storage.all().values()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            key = f"{args[0]}.{args[1]}"
            print([str(v) for k, v in storage.all()[key].items()] if k.startswith(args[0]))

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
