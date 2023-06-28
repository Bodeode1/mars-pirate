
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

def show_game_instructions():
    """
    This function displays the instructions of the game

    """

    print("To start the game, press y to start and n to stop.")
    print("You can play the game 5 times, and you need to kill 3 aliens to win.")
    print("You kill an alien when you fire your weapon at their hiding cell.")
    print("The cells are numbered from 1 to 9(10 not inclusive).")
    print("For example, if you need to kill an alien at cell 4, you will enter 4 when prompted")

def collect_player_input(message:"str"):
    """
    This function collects input from a player or user.

    Parameters:
        message (str): The message to display as a prompt to the player/user.

    Returns:
        str: The value entered by the player/user.
    """
    
    value_entered =input(message)
    return value_entered


# Define a global variable to keep track of the total number of plays
global total_play

#Initialize the total_play variable to 0
total_play = 0

scores = 0

#Initialize an empty list to represent the gameboard
gameboard = []

#Set the maximum_trial variable to 5
maximum_trial = 5

global play_game
play_game = True

