import random

MAX_LINES = 3
MAX_DEPOSIT = 100
ROWS = 3
COLS = 3

symbols_count = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}


symbol_values ={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def main():
    balance = deposit()
    while True :
        line = get_lines()
        while True : 
            bet = get_bet(balance)
            total = bet * line
            if balance >= total : 
                break
            print(f"Your total bet is ${total} , but you main balance is {balance}")
            print(f"You are ${total-balance} short!")

        print(f"Your total  bet ${total} , with {line} line(s)")
        colums = get_colums(ROWS , COLS , symbols_count)
        get_spin(colums)
        winnings , winning_line = get_winnings(symbol_values , line , colums , total)

        balance -= total 
        if winnings != 0:
            print("You won!!!")
            print(f"You won: ${winnings}")
            balance += winnings
            print(f"Your current balance ${balance}")
        elif balance == 0  : 
            print("You are out of balance")
            quit()
        else:
            print("No win this time!")
            print(f"Your current balance: ${balance}")

        should_play = input("Do you want to play (Press enter to continue or type q to quit): ").lower()
        if should_play == "q" :
            break
    print(f"You cahsed out!      BALANCE :${balance}")

def get_colums(rows , cols , symbols):
    all_symbol = []
    for symbol ,symbol_count in symbols.items() : 
        for _ in range(symbol_count) :
            all_symbol.append(symbol)

    colums = []

    for _ in range(cols):
        colum = []
        current_symbol = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            colum.append(value)
        colums.append(colum)
    return colums


def get_spin(colums) : 
    for row in range(len(colums[0])):
        for i , colum in enumerate(colums) :
            if i != len(colums) - 1 : 
                print(colum[row] , end =" | ")
            else :
                print(colum[row] , end="")
        print()

def get_winnings(values , lines , colums , bet ):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = colums[0][line]
        for col in colums :
            symbol_check = col[line]
            if symbol_check != symbol : 
                break
        else:
            winnings+=values[symbol] * bet
            winning_line.append(line + 1)
    return winnings , winning_line


def deposit():
    while True : 
        try: 
            amount = int(input(("Enter your amount : $")))
            if 1 <= amount <= MAX_DEPOSIT: 
                return amount
            print("Please Enter a valid amount!")
            print(f"The amount should be more then 0 and within {MAX_DEPOSIT}")
        except ValueError : 
            print("Error! please enter a valid number")


def get_bet(balance):
    while True: 
        try : 
            bet = int(input("How much you want to bet on  each line :$ "))
            if 1 <= bet <= balance : 
                return bet 
            print(f"The betting amount should in range of ($1-${balance})")
        except ValueError :
            print("Error! please enter valid amount")
              

def get_lines():
    while True:
        try:
            line = int(input(f"Enter the number of lines (1-{MAX_LINES}): "))
            if 1 <= line <= MAX_LINES : 
                return line
            print(f"Please enter a line between (1 - {MAX_LINES})")
            
        except ValueError: 
            print("Error ! Please enter a valid number!")


if __name__ == "__main__":
    main()
