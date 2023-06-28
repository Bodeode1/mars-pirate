
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

class GameOverException(Exception):
    def __init__(self, message):
        pass 
        self.message = message 

def end_game_moderator(play_count: int, maximum_play: int):
    """
    Checks if the game should be ended based on the maximum number of plays.

    Parameters:
        play_count (int): The current play count.
        maximum_play (int): The maximum number of plays allowed.

    """
    points = 0 
    global play_game
    for score in gameboard:
        if score.get("point_earned") == 1:
            points = points + 1
    if play_count == maximum_play:
        print("Take a look at your game history") 
        for score in gameboard:
            print(score)
            print() 

        print(Fore.YELLOW + "You Got {0} point out of {1} trials".format(points, maximum_play))
        if points >= 3:
            print("You have won") 
            print("Do you want to finish the game play?")
        else:
            print(Fore.RED + "The game is over. Unfortunately you did not kill enough alien. You lose")
        play_game = False

    return play_game

def record_score(alien_cell: int, player_shot: int, duration: int):
    """
    Records and stores the game statistics

    Parameters:
        alien_cell (int): The position of the alien.
        player_shot (int): The player's guess.
        duration (int): The time taken for the guess.

    Returns:
        gameboard (list): Updated gameboard containing the game statistics.
    
    """

    gameboard.append({
        "time_to_play": duration,
        "alien_position": alien_cell,
        "your_guess": player_shot,
        "verdict": "correct" if alien_cell == player_shot else "wrong",
        "point_earned": 1 if alien_cell == player_shot else 0
    })
    return gameboard


def check_guess(guess: int, alien_cell: int):
    """
    Checks the player's guess against the alien cell and prints the result.

    Parameters:
        guess (int): The player's guess.
        alien_cell (int): The position of the alien.
    """
    if guess == alien_cell:
        print("Congratulations!!! You just killed an Alien")
    else:
        print("You are wrong. The Alien was at {}".format(alien_cell))


def play_game():
    """
    Starts the game loop.
    
    """
    while play_game:
        alien_position = randint(1, 5)
        try:
            first_shot = "Guess the alien cell, so a shot can be fired: "
            another_shot = "Make another guess, let us shoot the alien: "

            shot_message = first_shot if len(gameboard) == 0 else another_shot

            guess_start_time = time.time()
            player_guess = int(input(shot_message))

            guess_end_time = time.time()

            time_taken_to_guess = guess_end_time - guess_start_time

            record_score(alien_position, player_guess, time_taken_to_guess)
            check_guess(player_guess, alien_position)

            end_game_moderator(len(gameboard), maximum_trial)
        except ValueError as _:
            print(Fore.RED + "Please enter a number")
        except GameOverException as _:
            break


