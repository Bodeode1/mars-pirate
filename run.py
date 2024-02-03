
import time
from random import randint 
import os 
import pyfiglet
from colorama import init , Fore 

init(autoreset=True) 

def clear_terminal():

    '''
        Description : Clears the terminal. After calling this function,
            every item on the terminal will be wiped off
    '''
    os.system("cls" if os.name == "nt" else "clear")

def show_game_title():
    print(pyfiglet.figlet_format('PIRATE OF MARS'))
    print("You are going to destroy pirate aliens") 
    print("Aliens now terrorises passengers embarking on interplanetary travel")
    print("You are part of the space force tasked with safeguarding space travel")
    print("Select any of the number below to proceed") 
    print()
    
def show_game_instructions():
    print("You can play the game 5 times, and you need to kill 3 aliens to win")
    print("You kill an Alien when you fire your weapon at their cell of hiding")
    print("When you start the game, select a level:")
    print("1. Easy (Guess between 1 and 3)")
    print("2. Medium (Guess between 1 and 5)")
    print("3. Hard (Guess between 1 and 9)")
    print()

def collect_player_input(message : str):
    value = input(message)
    return value 

 

global total_play 

total_play = 0
scores = 0 
gameboard = [] 
maximum_trial = 5 
global play_game 
play_game = True 
play_or_go_home_message = Fore.GREEN + "Press y to play again or any character to return to home menu: " 
go_main_or_start_new_game = Fore.GREEN + "Press y to return to the main menu or press any other character to start a new game: "

class GameOverException(Exception):
    def __init__(self,message):
        pass 
        self.message = message 
    
def end_game_moderator(play_count: int, maximum_play: int):
    ''' Checks if to end a game based on the maximum play'''
    points = 0
    global play_game
    for score in gameboard:
        if score.get("point_earned") == 1:
            points += 1

    if play_count == maximum_play:
        print("Take a look at your game history")
        for score in gameboard:
            print(score)
            print()

        print(Fore.YELLOW + "You Got {0} point out of {1} trials".format(points, maximum_play))
        if points >= 3:
            print(Fore.GREEN + "Congratulations!!! You have won")
        else:
            print(Fore.RED + "The game is over. Unfortunately, you did not kill enough aliens. You lose")

        play_again = input(play_or_go_home_message)
        if play_again.lower() == 'y':
            clear_terminal()
            gameboard.clear()  # Clear game history for a new game
            boot_game() 
        else:
            main()

    return play_game



def record_score(alien_cell : int , player_shot : int , duration : int):
    ''' Records and store the game statistics '''

    gameboard.append({
        "time_to_play" : duration,
        "alien_position" : alien_cell , 
        "your_guess" : player_shot,
        "verdict" : "correct" if alien_cell == player_shot else "wrong" ,
        "point_earned" : 1 if alien_cell == player_shot else 0
    })
    return gameboard 


def check_guess(guess : int , alien_cell : int):
    if guess == alien_cell :
        print("Congratulations!!! You just killed an Alien")
    else:
        print("You are wrong. The Alien was at {}".format(alien_cell))

def show_game_history():
    print("Game History:")
    if not gameboard:
        print("No game history available.")
    else:
        for idx, score in enumerate(gameboard, start=1):
            print(f"Trial {idx}:")
            print(f"Time to play: {score['time_to_play']} seconds")
            print(f"Alien position: {score['alien_position']}")
            print(f"Your guess: {score['your_guess']}")
            print(f"Verdict: {score['verdict']}")
            print("-" * 30)

def start_game(level_range : int):
    '''Starts the game  ''' 
    while play_game:
        alien_position = randint(1, level_range)  
        try:
            first_shot = "Guess the alien cell, so a shot can be fired: " 
            another_shot = "Make another guess, let us shoot the alien: "

            shot_message = first_shot if not gameboard else another_shot

            player_guess = None
            invalid_num_msg = "Please enter a valid number between 1 and " + str(level_range)
            while player_guess not in range(1, level_range + 1):
                try:
                    player_guess = int(input(shot_message))
                    if player_guess not in range(1, level_range + 1):
                        print(Fore.RED + invalid_num_msg)
                except ValueError:
                    print(Fore.RED + invalid_num_msg )
                    
            guess_start_time = time.time() 

            record_score(alien_position, player_guess, guess_start_time)
            check_guess(player_guess, alien_position)

            end_game_moderator(len(gameboard), maximum_trial)
        except ValueError as _:
            print(Fore.RED + "Please, enter a number")
        except GameOverException as _ : 
            break

def boot_game():
    valid_levels = {'1': 3, '2': 5, '3': 9}

    while True:
        level_choice = input("Choose a level (1 for Easy, 2 for Medium, 3 for Hard): ")
        if level_choice in valid_levels:
            start_game(valid_levels[level_choice])
            break
        else:
            print(f'{Fore.RED} Invalid level choice. Please enter a valid number.')

def game_nav_handler(selected_nav , navigations):
    if selected_nav not in navigations:
        print(f'{Fore.RED} Please, select either  1 , 2 , or 3')
        main() 
    elif selected_nav == '1':
        clear_terminal()
        boot_game()

    elif selected_nav == '2':
        show_game_instructions()
        launch_main_menu() 
    elif selected_nav == '3':
        show_game_history()
        launch_main_menu() 

def game_home_display():
    left_text = '1. Play Pirates of Mars | '
    center_text = '2. Read Playing Instructions |'
    right_text = '3. Game History'
    print('-' * 100)
    print(f'{left_text : <20}{center_text : ^20}{right_text : ^20}')
    print('-' * 100)

def main():
    '''Launches the game board  '''

    clear_terminal() 
    show_game_title() 
    game_home_display()

    selected_nav = input('Select an option: ')
    navigations = ['1', '2', '3']
    game_nav_handler(selected_nav , navigations)
    
    
def launch_main_menu():
    launch = input(go_main_or_start_new_game)
    if launch.lower() == "y":
        main()
    else:
        clear_terminal()
        global total_play, scores, gameboard, play_game
        total_play = 0
        scores = 0
        gameboard = []
        play_game = True
        show_game_title()
        game_home_display()
        selected_nav = input('Select an option: ')
        navigations = ['1', '2', '3']
        game_nav_handler(selected_nav , navigations)


if __name__ == "__main__":
    main()
