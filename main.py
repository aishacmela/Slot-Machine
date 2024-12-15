import random


#constants to define the rukes of the game 
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMN = 3

#defines the frequency of each symbol
symbol_count= {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_payout = {
    "A" : 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnngs(columns, lines, bet,payout):
    winnings = 0
    winning_lines = []
    for line in range(lines): #check the number of lines the player bet on
        symbol = columns[0][line] #get the first symbol in the row
        if all(col[line] == symbol for col in columns):
            winnings += payout[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

#sumilate slot spinning  by randomly generating grid of symbols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)  

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]  # Copy the symbol list for each column
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)  # Add the generated column to the result
    return columns


def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for col in columns: #for every column, print each row symbol
            print(col[row], end=" | ")
        print()



#gets deposit from the user
def deposit():
    while True:
        amount = input("How much would you like to deposit R: ")
        #check if the amount is a while number 
        if amount.isdigit():
            #convert the amount to int as it comes as string
            amount= int(amount)
            #break out of the loop if the number is greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")       
    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter a number of lines you want to bet on (1-" + str(MAX_LINES) + ")? ") 
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of line")
        else:
            print("Please enter a number")       
    return lines

def get_bet():
    while True:
        bet = input("How Much would you like to bet with R:")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}")
        else:
            print("Please enter a number")       
    return bet

#define the main function for its reusability 
def main():
    balance = deposit()
    while True:
        lines = get_number_of_lines()
        while True:
            bet = get_bet()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You do not have enough to bet that amount. Your current balance is R{balance}, but your total bet is R{total_bet}.")
            else:
                break

        print(f"You are betting R{bet} on {lines} lines. Total bet is R{total_bet}.")

        # Deduct the bet from the balance
        balance -= total_bet

        # Spin the slot machine
        slots = get_slot_machine_spin(ROWS, COLUMN, symbol_count)
        print_slot_machine(slots)

        #check winnings\
        winnings , winning_lines = check_winnngs(slots, lines, bet, symbol_payout)
        balance += winnings 

        #display results
        print(f"You won R{winnings}!")
        if winning_lines:
            print(f"You won on line: {', '.join(map(str, winning_lines))}")
        else:
            print("No winning lines this time")


        # Placeholder for win/loss logic
        print(f"Your balance is: R{balance}")

        if balance <= 0:
            print("You have run out of funds! Game Over.")
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

main()