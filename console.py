#!/usr/bin/python3
"""console"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    intro = None
    prompt = "(hbnb) "
    file = None

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
