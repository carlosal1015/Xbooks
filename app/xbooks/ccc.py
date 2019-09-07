#!/usr/bin/env python

from colorama import init as initcolor
initcolor(autoreset=True)
from colorama import Fore, Back

def stderr(txt):
    print(Back.LIGHTRED_EX+"|STDERR|", Fore.LIGHTRED_EX+'> '+str(txt))

def success(txt):
    print(Back.GREEN+"|Success|", Fore.GREEN+'> '+txt)

def fail(txt):
    print(Back.RED+"|Failure|", Fore.RED+'> '+txt)

def alert(txt):
    print(Back.YELLOW+"|Alert|", Fore.YELLOW+'> '+txt)

def note(txt):
    print(Back.CYAN+"|Note|", Fore.CYAN+'> '+txt)

def greet(txt):
    print(Back.MAGENTA+"|Greetings|", Fore.MAGENTA+'> '+txt)

def logo(txt):
    print(Back.WHITE+Fore.BLACK+'|'+txt+'|')

def blue(tag, txt):
    print(Back.BLUE+'|'+tag+'|', Fore.BLUE+'> '+txt)

def green(tag, txt):
    print(Back.GREEN+'|'+tag+'|', Fore.GREEN+'> '+txt)

def yellow(tag, txt):
    print(Back.YELLOW+'|'+tag+'|', Fore.YELLOW+'> '+txt)

def red(tag, txt):
    print(Back.RED+'|'+tag+'|', Fore.RED+'> '+txt)

def cyan(tag, txt):
    print(Back.CYAN+'|'+tag+'|', Fore.CYAN+'> '+txt)

def magenta(tag, txt):
    print(Back.MAGENTA+'|'+tag+'|', Fore.MAGENTA+'> '+txt)

def white(tag, txt):
    print('|'+tag+'|','> '+txt)
    # print(Fore.BLACK+Back.WHITE+'|'+tag+'|', Fore.WHITE+'> '+txt)

def test():
    success("this is success")
    fail("this is failure")
    alert("this is alert")
    note("this is note")
    greet("this is greetings")
    logo("Xbooks")
    blue("tag", "this is tag")

__all__ = ['success', 'fail', 'alert', 'note', 'greet', 'logo', 'blue', 'green', 'yellow', 'red', 'cyan', 'magenta']

if __name__ == "__main__":
    test()