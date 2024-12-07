#define in capital letters so that number is constant througout the game
MAX_LINES = 3


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



#define the main function for its reusability 
def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines )


main()