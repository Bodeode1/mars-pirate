
import time   
from random import randint
import os  
import pyfiglet
from colorama import init , Fore

init(autoreset=True) #Initialize colorama

def clear_terminal():
    """
    Clears the contents of the terminal screen.

    """
    os_name = os.name  #Retrieves the name of the operating system
   
    if os_name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def show_game_title():
    """
    This Function displays the game title and provides introductory text to the player

    """

    print(pyfiglet.figlet_format('PIRATE OF MARS'))
    time.sleep(2)
    print("You are going to destroy pirate aliens.")
    print("Aliens now terrorize passengers embarking on interplanetary travel.")
    print("You are part of the space force tasked with safeguarding space travel.")
    print("Select any of the number below to proceed.")
    print()
