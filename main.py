import random 
import tkinter as tk
import turtle as turt

def shapes():
    pass
    
def flip_coin():
    count = 0
    heads_count = 0
    tails_count = 0

    print("-=-=-Coin Flipper-=-=-")

    while True:

        input("Press Enter to flip a coin")

        result = random.randint(1,2)

        if result == 1:
            print("")
            print("Result: Heads")
            print("")
            heads_count += 1
        else:
            print("")
            print("Result: Tails")
            print("")
            tails_count += 1
        count += 1

        print(f"------ That was flip #{count} ------")
        print(f"Total results: {heads_count} Heads and {tails_count} Tails")

        print("")
        print("Enter M to return to the main menu")
        print("Press Enter to flip another coin")
        exit_choice = input("Your choice: ")

        if exit_choice.lower() == "m":
            return
        
def calculate_interest():
    def simple_interest(rate,principal,time):
        print(f"After investing {principal} for {time} years with a rate of {rate}% per year:")
        result =(int(principal)*int(time)*(int(rate)/100))+int(principal)
        print(f"You will have ${result} ")
def roll_dice():
    pass

def main():
    pass

if __name__ == "__main__":
    main()
   