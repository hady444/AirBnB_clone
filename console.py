#!/usr/bin/python3
"""console"""
import cmd
from models.base_model import BaseModel
import models
import shlex

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "
    __classes = ["BaseModel", "User"]
    def do_EOF(self, arg):
        """EOF command to exit the program with ctrl+d"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        args = shlex.split(arg)
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0])()
            new_obj.save()
            print(new_obj.id)

    def do_show(self, arg):
        args = shlex.split(arg)
        length = len(args)
        if length < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        else:
            for key, obj in models.storage.all().items():
                if obj.id == args[1]:
                    print(obj)
                    return False
            print("** no instance found **")

    def do_destroy(self, arg):
        args = shlex.split(arg)
        length = len(args)
        if length < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        else:
            deletion = models.storage.all()
            for key, obj in deletion.items():
                if obj.id == args[1]:
                    del deletion[key]
                    models.storage.save()
                    return False
            print("** no instance found **")

    def do_all(self, arg):
        args = shlex.split(arg)
        length = len(args)
        if length < 1:
            all_lst = list(str(obj) for obj in models.storage.all().values())
            print(all_lst)
            return False
        else:
            if args[0] in HBNBCommand.__classes:
                all_lst = list(str(obj) for obj in models.storage.all().values() if obj.__class__.__name__ == args[0])
                print(all_lst)
                return False
            print("** class doesn't exist **")

    def do_update(self, arg):
        args = shlex.split(arg)
        length = len(args)
        dic = models.storage.all()
        if length < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        elif args[1] not in list(obj.id for obj in models.storage.all().values() if obj.__class__.__name__ == args[0]):
            print("** no instance found **")
        elif length < 3:
            print("** attribute name missing **")
        elif length < 4:
            print("** value missing **")
        else:
            if args[2] not in ['id', 'created_at', 'updated_at']:
                attr_v = args[3]
                try:
                    if args[3].isdigit():
                        attr_v = int(args[3])
                    elif float(args[3]):
                        attr_v = float(args[3])
                except ValueError:
                    pass
                for key, obj in dic.items():
                    if obj.id == args[1] and obj.__class__.__name__ == args[0]:
                        setattr(dic[key], args[2], attr_v)
                        models.storage.save()
                        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
