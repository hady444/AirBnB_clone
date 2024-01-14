#!/usr/bin/python3
"""console"""
import cmd, sys


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = "(hbnb) "

    def do_EOF(self, arg):
        """EOF command to exit the program with ctrl+d\n"""
        return True

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
