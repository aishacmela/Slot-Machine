import random


#define in capital letters so that number is constant througout the game
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMN = 3

symbol_count= {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols= []
    #items is to give us all the values stored ina dictionary
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbols)
    
    #define columns list
    column = []
    #generate column for each column we have
    for _ in range(cols):
        #pick random values for wach colum and row we will have
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(all_symbols)
            current_symbols.remove(value)
            column.apppend(value)
        
        columns.append(column)
    return columns

def print_slot_machine(columns)

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
        bet = input("How Mich would you like to bet with R:")
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
    lines = get_number_of_lines()
    while True:
        
        bet = get_bet()
        total_bet = bet * lines
        if  total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is R{balance} and you are betting R{total_bet} ")
        else:
            break
    
    print(f"You are betting {bet} on {lines} lines. The Total bet is {total_bet}")


main()