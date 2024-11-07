import random
import time

# Global variables representing the horses, initial distances, and odds for each horse

HORSES_RACING =  [
                 'Thunderhoof', 'Royal Stride', 'Storm Chaser', 
                 'Noble Steed', 'Midnight Runner', 'Neigh Slayer'
                 ]

HORSE_DISTANCE = { # Tracks each horse's progress in the race
                 'Thunderhoof': 0, 'Royal Stride': 0, 'Storm Chaser': 0,
                 'Noble Steed': 0, 'Midnight Runner': 0, 'Neigh Slayer': 0
                 }

HORSE_ODDS =     { # Odds for each horse, used to calculate payout
                 'Thunderhoof': 1.5, 'Royal Stride': 3.0, 'Storm Chaser': 2.5,
                 'Noble Steed': 3.5, 'Midnight Runner': 4.0, 'Neigh Slayer': 3.5
                 }

# Constants for the race and betting limits
RACECOURSE_DISTANCE = 50
MINIMUM_BET = 100
MAXIMUM_BET = 5000

def game_intro():
    """
    Introduces the game with a welcome message and race description.
    Uses a delay for dramatic effect.
    """
    print('\033[1mWelcome to the Ultimate Horse Race!🏇')
    time.sleep(1.25)
    print('''\033[0mGet ready for an exciting race where \033[1mspeed\033[0m, \033[1mstrategy\033[0m, and \033[1mluck\033[0m all come together!
          ''')
    time.sleep(3)
    print('''Will your horse take the lead, or will another surprise contender cross the finish line first?
Choose your favorite horse, place your bets, and let the race begin!
          ''')
    time.sleep(5.5)
    print('''Each horse is racing to the finish, and the race is about to start! Keep an eye on the positions.
Anything can happen as the horses charge ahead!
          ''')

def display_players_and_odds(horse_list, horse_odds):
    """
    Displays available horses and their respective odds.
    :param horse_list: List of horse names.
    :param horse_odds: Dictionary with horse names as keys and odds as values.
    """
    print('Here are your Horses:')
    time.sleep(2)
    for index, items in enumerate(horse_list):
        print(f'{index+1}) {items}')
        time.sleep(1)
    print('\nHere are your odds:')
    time.sleep(2)
    for horse, odds in horse_odds.items():
        print(f'{horse}: {odds}')
        time.sleep(1)

def bet_placing():
    """
    Prompts the player to place a bet within the allowed range.
    Ensures the player selects a valid horse for betting.
    :return: Tuple containing the bet amount and chosen horse.
    """
    bet = 0
    while bet < MINIMUM_BET or bet > MAXIMUM_BET:
        print(f'Place your bet within ${MINIMUM_BET} and ${MAXIMUM_BET}: ')
        bet = input()
        try:
            bet = float(bet)
            if bet < MINIMUM_BET or bet > MAXIMUM_BET:
                print(f'''Error: Bet must be between ${MINIMUM_BET} and ${MAXIMUM_BET}
                       ''')
        except ValueError:
            print('''Error: Please enter a valid number for your bet.
                  ''')
    horse = input('Which Horse will you be betting on? ')
    while horse not in HORSES_RACING:
        print('''Error: Choose from the official list of Horses
              ''')
        horse = input('Which Horse will you be betting on? ')
    print(f'''\033[1mExcellent!\033[0m
You have bet ${bet} on {horse}
           ''')
    return bet, horse

def show_horserace(course_distance, horse_distance):
    """
    Simulates the race by updating each horse's distance randomly.
    Displays each horse's progress and returns the winning horses.
    :param course_distance: Distance needed to finish the race.
    :param horse_distance: Dictionary tracking each horse's distance covered.
    :return: List of winning horses.
    """
    print('''Okay ladies and gentlemen. Pay attention to the live race update on the terminal.
The race is about to start on the count of 3
''')
    time.sleep(0.75)
    print('\033[1m3')
    time.sleep(1)
    print('\033[1m2')
    time.sleep(1)
    print('\033[1m1')
    time.sleep(1)
    print('\033[1mGO!')
    
    # Create a copy to avoid changing the initial distances
    copy_distance = horse_distance.copy()
    distance_covered = list(copy_distance.values())
    while max(distance_covered) < course_distance:
        for horse in copy_distance:
            copy_distance[horse] += random.randint(1,3)

        # Display each horse's progress visually
        for horse, distance in copy_distance.items():
            print(f'{horse:<15}: {"-" * distance}>')
        time.sleep(0.5)
        print(f'\n {"-" * 50}')
        distance_covered = list(copy_distance.values())
    
    # Identify winning horse(s) with maximum distance covered
    max_distance = max(distance_covered)
    winning_horses = []
    for horse, distance in copy_distance.items():
        if distance == max_distance:
            winning_horses.append(horse)
    return winning_horses

def show_winning_horse(winning_horses):
    """
    Announces the winning horse(s) at the end of the race.
    :param winning_horses: List of horses that reached the finish line first.
    """
    print('\033[1mWOW! What a race')
    time.sleep(1)
    print('The winning horse(s) are:')
    for horse in winning_horses:
        print(horse)
        time.sleep(1)
    return winning_horses

def start_game():
    """
    Starts the game by showing an intro, allowing the player to bet or watch.
    Executes the race and determines the outcome of the bet.
    """
    game_intro()
    display_players_and_odds(HORSES_RACING, HORSE_ODDS)
    print()

    choice = input('Would you like to bet? Type Yes to bet, and No to just watch the game. (Type Yes or No): ').lower()
    if choice == 'yes':
        bet, horse = bet_placing()
        winners = show_horserace(RACECOURSE_DISTANCE, HORSE_DISTANCE)
        show_winning_horse(winners)
        if horse in winners:
            print(f'\033[1mCONGRATULATIONS!!! {horse} WON THE RACE')
            odds = HORSE_ODDS[horse]
            payout = bet * odds
            print(f'You won ${payout}')
        else:
            print(f'''Unfortunately {horse} did not win, and you lost your money.
                  ''')
            time.sleep(1)
            print('''Hope you enjoyed the race though 😊😊😊
                  ''')
        restart_or_quit = input('''Click ENTER to restart, or any other key to end the game: 
''')
        return restart_or_quit
    elif choice == 'no':
        print('''You chose to watch the race without betting.
              ''')
        winners = show_horserace(RACECOURSE_DISTANCE, HORSE_DISTANCE)
        show_winning_horse(winners)
        print("Thanks for watching the race!")
        restart_or_quit = input('''Click ENTER to restart, or any other key to end the game: 
                                ''')
        return restart_or_quit
    else:
        print("Invalid input! Please try again.")
        return start_game()

def main():
    """
    Main function to keep the game running until the player chooses to quit.
    """
    while True:
        players_choice = start_game()
        if players_choice != '':
            break

main()

    


