#!/usr/bin/python3
"""Command interpreter for the AirBnB clone project."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Handle EOF and quit the command interpreter."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
