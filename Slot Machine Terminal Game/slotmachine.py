import random
import time

# Symbol frequency and odds for the slot machine
symbol_frequency = { 
                   'A': 2,
                   'B': 4,
                   'C': 6,
                   'D': 8
                   }

symbol_odds = {
                   'A': 5,
                   'B': 4,
                   'C': 3,
                   'D': 2
                   }

# Constants for betting and slot configuration
MAX_BETTING_LINES = 3 
MIN_BETTING_LINES = 1
MAX_BET_AMOUNT = 100 
MIN_BET_AMOUNT = 1  

ROWS = 3 
COLUMNS = 3

def intro():
    """Displays introductory message to the player."""
    print("🎰 Welcome to the Slot Machine Game! 🎰")
    time.sleep(1)
    print("💰 Ready to test your luck and see if you can win big? 💸")
    time.sleep(1)
    print("🎉 Get started by depositing some money, and let's spin the reels! 🎉")
    time.sleep(2)
    print("Let's Play! 🚀\n")
    time.sleep(1)

def get_deposit():
    """Prompts the player to deposit money and validates the input."""
    deposit = input('Enter the amount you would like to deposit: $')
    if deposit.isdigit():
        deposit = int(deposit)
        if deposit > 0:
            return deposit
        else:
            print('The deposit must be greater than zero.')
            return get_deposit()
    else:
        print('Input should be a valid number.')
        return get_deposit()

def get_betting_line_count():
    """Prompts the player to select the number of betting lines."""
    line_count = input(f"Enter the line-count you're betting on ({MIN_BETTING_LINES}-{MAX_BETTING_LINES}): ")
    if line_count.isdigit():
        line_count = int(line_count)
        if MIN_BETTING_LINES <= line_count <= MAX_BETTING_LINES:
            return line_count
        else:
            print(f'Invalid input. Please pick a number between {MIN_BETTING_LINES} and {MAX_BETTING_LINES}.')
            return get_betting_line_count()
    else:
        print('Invalid entry. Please enter a valid numeric value.')
        return get_betting_line_count()

def place_bet():
    """Prompts the player to place a valid bet per line."""
    bet_amount = input("How much would you like to wager per line? $")
    if bet_amount.isdigit():
        bet_amount = int(bet_amount)
        if MIN_BET_AMOUNT <= bet_amount <= MAX_BET_AMOUNT:
            return bet_amount
        else:
            print(f"Your bet must be between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}.")
            return place_bet()  
    else:
        print("Please input a valid number.")
        return place_bet()

def calculate_winnings(columns, lines, bet, values):
    """Calculates the total winnings based on the columns, bet, and symbol odds."""
    total_winnings = 0
    winning_lines = [] 
    for line in range(lines):
        symbol = columns[0][line]  
        for column in columns:
            if symbol != column[line]:
                break
        else:
            total_winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return total_winnings, winning_lines

def spin_slot_machine(row, col, symbols):
    """Simulates the slot machine spin and generates random symbols."""
    total_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = []
    for _ in range(col):
        column = []
        updated_symbols = total_symbols[:]
        for _ in range(row):
            value = random.choice(updated_symbols)
            updated_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def slot_machine_display(columns):
    """Displays the result of the slot machine spin."""
    for row in range(len(columns[0])):
        print(" || ".join(column[row] for column in columns))

def spin_machine(balance):
    """Handles the betting, spinning, and winnings calculation."""
    lines = get_betting_line_count()
    
    while True:
        bet = place_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    
    print(f"Your bet of ${total_bet} has been placed.")
    slots = spin_slot_machine(ROWS, COLUMNS, symbol_frequency)
    slot_machine_display(slots)
    
    winnings, winning_lines = calculate_winnings(slots, lines, bet, symbol_odds)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", winning_lines)
    
    return winnings - total_bet

def main():
    """Main game loop that starts the game, manages balance, and handles quitting."""
    intro()
    balance = get_deposit()
    
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (Quit to quit).").lower()
        
        if answer == "quit":
            break
        
        result = spin_machine(balance)
        print(f"Result: ${result}")
        balance += result
        
        if balance <= 0:
            print("Your balance is empty. Game over!")
            break

    print(f"You left with ${balance}")
    print("Thank you for playing! 🎉")

main()

