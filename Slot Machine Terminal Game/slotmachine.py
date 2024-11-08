import random
import time

# Symbol frequency and odds. Dictates probability and payouts for each symbol.
symbol_frequency = { 
                   'A': 2,
                   'B': 3,
                   'C': 4,
                   'D': 5
                   }

symbol_odds = {
                   'A': 5,  # Multiplier for symbol A
                   'B': 4,
                   'C': 3,
                   'D': 2
                   }

# Betting and slot configuration constants.
MAX_BETTING_LINES = 3
MIN_BETTING_LINES = 1
MAX_BET_AMOUNT = 100
MIN_BET_AMOUNT = 1

ROWS = 3
COLUMNS = 3

def intro():
    """Displays the introductory message to the player."""
    print("🎰 Welcome to the Slot Machine Game! 🎰")
    time.sleep(1)
    print("💰 Ready to test your luck and see if you can win big? 💸")
    time.sleep(1)
    print("🎉 Get started by depositing some money, and let's spin the reels! 🎉")
    time.sleep(2)
    print("Let's Play! 🚀\n")
    time.sleep(1)

def get_deposit():
    """Prompts the player for a valid deposit amount."""
    deposit = input('Enter the amount you would like to deposit: $')
    if deposit.isdigit() and int(deposit) > 0:
        return int(deposit)
    print('Invalid input. Please enter a positive number.')
    return get_deposit()

def get_betting_line_count():
    """Prompts the player to select the number of betting lines."""
    line_count = input(f"Enter the line-count you're betting on ({MIN_BETTING_LINES}-{MAX_BETTING_LINES}): ")
    if line_count.isdigit() and MIN_BETTING_LINES <= int(line_count) <= MAX_BETTING_LINES:
        return int(line_count)
    print(f'Invalid input. Please pick a number between {MIN_BETTING_LINES} and {MAX_BETTING_LINES}.')
    return get_betting_line_count()

def place_bet():
    """Prompts the player to place a bet per line."""
    bet_amount = input("How much would you like to wager per line? $")
    if bet_amount.isdigit() and MIN_BET_AMOUNT <= int(bet_amount) <= MAX_BET_AMOUNT:
        return int(bet_amount)
    print(f"Invalid amount. Bet must be between ${MIN_BET_AMOUNT} and ${MAX_BET_AMOUNT}.")
    return place_bet()

def calculate_winnings(columns, lines, bet, values):
    """Calculates total winnings based on matching symbols across lines."""
    total_winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(symbol == column[line] for column in columns):  # Check if all columns match
            total_winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return total_winnings, winning_lines

def spin_slot_machine(row, col, symbols):
    """Simulates the slot machine spin and generates random symbols."""
    total_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    columns = []
    for _ in range(col):
        column = [random.choice(total_symbols) for _ in range(row)]  # Generate each column
        columns.append(column)

    return columns

def slot_machine_display(columns):
    """Displays the slot machine spin result."""
    for row in range(len(columns[0])):
        print(" || ".join(column[row] for column in columns))  # Format and print each row
        time.sleep(1)

def spin_results(balance):
    """Handles the betting, spinning, and winnings calculation."""
    lines = get_betting_line_count()
    while True:
        bet = place_bet()
        total_bet = bet * lines
        if total_bet <= balance:
            break
        print(f"Insufficient funds. Current balance: ${balance}")

    print(f"Bet of ${total_bet} placed.\n")
    slots = spin_slot_machine(ROWS, COLUMNS, symbol_frequency)
    slot_machine_display(slots)

    winnings, winning_lines = calculate_winnings(slots, lines, bet, symbol_odds)
    print(f"You won ${winnings}.")
    time.sleep(1)
    print(f"Winning lines: {winning_lines}")

    return winnings - total_bet

def main():
    """Main game loop: start the game, manage balance, and handle quitting."""
    intro()
    balance = get_deposit()

    while True:
        print(f"Current balance: ${balance}")
        answer = input("Press enter to proceed. Type any key to quit.").lower()
        if answer != "":
            break
        
        result = spin_results(balance)
        print(f"\nResult: ${result}")
        balance += result
        
        if balance <= 0:
            print("Game over! Your balance is empty.")
            break

    print(f"Final balance: ${balance}")
    print("Thank you for playing! 🎉")

main()
