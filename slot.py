import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_value = {
    "A": 5,
    "b": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbol_count):
    all_symbols = []
    for symbol, count in symbol_count.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        column = random.sample(all_symbols, rows)
        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(ROWS):
        print(" | ".join(column[row] for column in columns))

def deposit():
    while True:
        amount = input("What would you like to deposit? £:")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

def get_number_of_lines():
    while True:
        lines = input("Enter number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? £:")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                return amount
            else:
                print(f"Amount must be between £{MIN_BET} - £{MAX_BET}.")
        else:
            print("Please enter a number.")

def main():
    balance = deposit()
    while True:
        print(f"Current balance is £{balance}")
        spin = input("Press enter to spin (q to quit): ")
        if spin == "q":
            break
        lines = get_number_of_lines()
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"Not enough balance. Your current balance is £{balance}.")
        else:
            balance -= total_bet
            slots = get_slot_machine_spin(ROWS, COLS, symbol_value)
            print_slot_machine(slots)
            winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
            balance += winnings
            print(f"You won £{winnings} on lines: {winning_lines if winning_lines else 'None'}")
    print(f"You left with £{balance}")

main()
