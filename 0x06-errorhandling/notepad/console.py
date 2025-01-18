#!/bin/env python3
"""An entry point of the note pad aplication"""

import cmd
from create import create
from update import update
from rename import rename

class Notepad(cmd.Cmd):
    """
    A class that implement notepad functionalities
    """ 
    prompt = "Notepad> "

    def emtyline(self):
            """A method emty line parsing """
            pass

    def precmd(self, line):
            """A method that handle imput in the terminal before executing"""
            print(line)
            command = line.strip().split(' ')
            return line
    
    def do_create(self, line):
         """
         a method that handle file create
         """
         pass
    
    def do_update(self, line):
        """
        a module that handle update
        """
        pass

    def do_rename(self, line):
         """
         a module that handles rename
         """
         pass
    
    def do_quit(self, line):
        """A method that handle quiting of the app"""
        return True

    def do_EOF(self, line):
        """A method that handles end of line"""
        return True


if __name__ == '__main__':
    Notepad() .cmdloop()            