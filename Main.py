import random
#Constant Values
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLUMNS = 3
Random_Symbols = { "A":2, "B":4, "C":6, "D":8} #amount of random symbols that will be in each colum on the slot machine
Random_Values = { "A":5, "B":4, "C":3, "D":2} #the value that each symbol holds for winnings in the slot machine


#Check_Winnings() check for maching rows in the slot machine
def Check_Winnings(columns, bet, values, lines):
    winnings = 0
    winning_lines = []
    for line in range(lines): #checks which line we are iterating
        symbol = columns[0][line] #assign that value on that line to symbols
        for column in columns:
            symbol_to_check = column[line] #checks to see if the symbols are equal to one another
            if symbol != symbol_to_check: 
                break
        else:
            winnings += values[symbol] * bet 
            winning_lines.append(line + 1) #adds winnings to a list then is returned by the function
    return winnings, winning_lines


#Random_Column_Generator() generates a list from a dictionary of symbols, and randomly creates each column from symbol list
def Random_Column_Generator(cols, rows, symbols): #pass arguments rows, colums, and symbols to function
    all_symbols = []
    for symbol, symbol_count in symbols.items(): #getting the key and value (A:2,..) in symbol and symbol_count
        for _ in range(symbol_count): #traversing how many values in symbol
            all_symbols.append(symbol)
    columns = [] 
    for _ in range(cols): #gets integer value from the range in each cols
        column = []
        current_symbols = all_symbols[:] #copies and creates new list from all_symbols -- not connected to same object
        for _ in range(rows):
            value = random.choice(current_symbols) #randomly selects value from full list
            current_symbols.remove(value) #removes value from list so it cant select it again
            column.append(value)
        columns.append(column)
    return columns


#Print_Slots() prints the rows as colums so we can see the randomly generated slot machine
def Print_Slots(columns):
    for row in range(COLUMNS): #gets full list of columns
        for i,column in enumerate(columns): #enumerate() keeps track of number of iterations we take through said columns
            if i != len(columns) - 1:
                print(column[row], end=" | ") #ends line print at specified pipe
            else:
                print(column[row], end="")
        print()
    return 


# Deposit() Function gets cash bet value from the user
def Deposit():
    while True: #loop until entered value is correct
        amount = input("Please enter deposit amount: $ ")
        if amount.isdigit():
            truAmount = int(amount) #int() converts object to a integer
            if truAmount > 0:
                break
            else:
                print("Please enter a value greater than zero")
        else:
            print("Please enter a numerical value greater than zero")
        #print("please enter a numerical value")
    return (truAmount)


# Number_Of_Lines() Gets the number of lines from the user that he/she would like to vet on
def Number_Of_Lines():
    while True: #loop until entered value is correct
        lines = input("Please enter number of lines you wish to bet on (1-" + str(MAX_LINES) +"): ") #MAX_LINES = 3 converted to str() type
        if lines.isdigit():
            truLines = int(lines) #int() converts object to a integer
            if 1 <= truLines <= MAX_LINES :
                break
            else:
                print("Invalid value entered." )
        else:
            print("Please enter a numerical value. ")
        #print("please enter a numerical value")
    return (truLines)


#Bet_Amount() function gets amount of bet for each line the user wants to bet on
def Bet_Amount(depositAmt,LineCount): #pases aruments deposit amount and line count
    while True:
        amount = input(f"Please enter a value between ${MIN_BET} - ${MAX_BET}: ") # f at the beginning of a print() function lets any object
        if amount.isdigit():                                                      # between two curly brackets automatically convert to a string
            truAmount = int(amount)                                               # type and print
            if MIN_BET <= truAmount <= MAX_BET : #checks if amount entered is between min & max amount
                truAmountCheck = truAmount * LineCount
                if truAmountCheck <= depositAmt : #checks to make sure user doesnt bet more than deposit amount
                    print(f"you have bet ${truAmount} on {LineCount} lines, for a total of ${truAmountCheck}")
                    break
                else:
                    print(f"the value you wish to bet is greater than your intitial deposit (${depositAmt})")
            else:
                print("Invalid value entered.")
        else:
            print("Please enter a numerical value.")
    return truAmount, truAmountCheck


#CheckBalance() function has main executables and functions
def CheckBalance(depositAmt, winnings, truBetAmount, balance, check_dep):
    if check_dep == True:
        balance = depositAmt + (winnings - truBetAmount)
        check_dep = False
        return balance
    else:
     return (balance + (winnings - truBetAmount))



def main():
    depositAmt = Deposit()
    balance = 0
    check_dep = True
    while True:
        lineCount = Number_Of_Lines()
        betAmount, truBetAmount = Bet_Amount(depositAmt,lineCount)
        slots = Random_Column_Generator(COLUMNS, ROWS, Random_Symbols)
        Print_Slots(slots)
        winnings, winning_lines = Check_Winnings(slots, betAmount, Random_Values, lineCount)
        print(f"you won ${winnings}!")
        print(f"your winning lines: ", *winning_lines)
        balance = CheckBalance(depositAmt, winnings, truBetAmount, balance, check_dep)
        print(f"your remaining balance is: ${balance}")
        spin = input("Press enter to spin again ('q' to quit): ")
        if spin == 'q':
            break

main()