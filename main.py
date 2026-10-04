import turtle as t
import random
import math 

def get_number(prompt, num_type=int):
    """Safely retrieves numeric input from the user to prevent ValueError crashes."""
    while True:
        try:
            return num_type(input(prompt))
        except ValueError:
            print(f"Invalid input. Please enter a valid number.")

def shapes():
    print("*****Shape Generator*****\n")

    while True:
        def draw_shape(length, sides):
            # apothem: the distance from the center of a polygon to the midpoint of one of its sides
            apothem = length / (2 * math.tan(math.pi / sides))
            t.clear()
            t.penup()
            t.goto(-length / 2, -apothem)
            t.setheading(0)
            t.pendown()
            angle = 360 / sides
            for _ in range(sides):
                t.forward(length)
                t.left(angle)
        
        choice = input("Enter the regular shape you want to render: ").strip().lower()
        
        valid_polygons = {
            "square": 4, "triangle": 3, "pentagon": 5, "hexagon": 6, 
            "septagon": 7, "heptagon": 7, "octagon": 8, "nonagon": 9, "decagon": 10
        }

        if choice == "circle":
            radius = get_number("Provide the radius for your circle: ", int)
            t.clear()
            t.penup()
            t.goto(0,0)
            t.setheading(270)
            t.forward(radius)
            t.pendown()
            t.setheading(0)
            t.circle(radius)

        elif choice == "rectangle":
            length = get_number("Enter the length of your rectangle: ", int)
            width = get_number("Enter the width of your rectangle: ", int)

            t.clear()
            t.penup()
            t.goto(-length / 2, -width / 2)
            t.setheading(0)
            t.pendown()

            for _ in range(2):
                t.forward(length)
                t.left(90)
                t.forward(width)
                t.left(90)
                
        elif choice in valid_polygons:
            length = get_number("Enter the desired side length: ", int)
            draw_shape(length, valid_polygons[choice])
            
        else:
            print("Sorry, that is not a supported shape.")

        print("\nEnter M to return to the main menu")
        print("Press Enter to generate another shape")
        exit_choice = input("Your choice: ")

        if exit_choice.strip().lower() == "m":
            return       
        
def flip_coin():
    count = 0
    headcount = 0
    tailcount = 0

    print("------- Coin Flipper -------")

    while True:
        input("Press Enter to flip a coin")
        result = random.randint(1, 2)

        if result == 1:
            print("\nResult: Heads\n")
            headcount += 1
        else:
            print("\nResult: Tails\n")
            tailcount += 1
            
        count += 1

        print(f"------- That was flip #{count} -------")
        print(f"Total results: {headcount} Heads and {tailcount} Tails")

        print("\nEnter M to return to the main menu")
        print("Press Enter to flip another coin")
        exit_choice = input("Your choice: ")
       
        if exit_choice.strip().lower() == "m":
            return       

def calculate_interest():
    print("---- Interest Calculator ----")

    while True:
        print("\nAre you dealing with simple or compound interest?")
        print("Simple Interest:   Enter S")
        print("Compound Interest: Enter C")
        interest_type = input("Your choice: ").strip().lower()

        if interest_type not in ('s', 'c'):
            print("Please choose a valid option")
            continue

        # Float allows for realistic decimals in currency and interest rates
        principal = get_number("Please enter your principal amount: $ ", float)
        rate = get_number("Please enter your annual interest rate: % ", float)
        time_period = get_number("How many years was your money deposited?: ", float)

        if interest_type == "s":
            final_amount = (principal * time_period * (rate / 100)) + principal
        else:
            final_amount = principal * ((rate / 100) + 1) ** time_period

        interest = final_amount - principal
        
        print("---------------Result------------------")
        print(f"After {time_period:g} years with a rate of {rate:g}%: ")
        print(f"Your principal amount is: ${principal:.2f}")
        print(f"You now have ${final_amount:.2f}")
        print(f"You gained: ${interest:.2f}")

        print("\nEnter M to return to the main menu")
        print("Press Enter to do another calculation")
        exit_choice = input("Your choice: ")
    
        if exit_choice.strip().lower() == "m":
            return

def roll_dice():
    dice = {
        "1": """
    ⬜️⬜️⬜️⬜️⬜️️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬜️⬛️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️️
    ⬜️⬜️⬜️⬜️⬜️""",
        "2": """
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
        "3": """
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬜️️⬜️
    ⬜️⬜️⬛️⬜️⬜️
    ⬜️⬜️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️️⬜️""",
        "4": """
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
        "5": """
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬛️️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
        "6": """
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️"""
    }

    print("\n---- Dice Roller ----\n")
    
    while True:
        dice_total = 0
        dice_count = get_number("\nHow many dice would you like to roll?: ", int)

        for _ in range(dice_count):
            x = random.randint(1, 6)
            dice_total += x
            print(dice[str(x)])

        print(f"\nSum of all dice: {dice_total}")  

        print("\nEnter M to return to the main menu")
        print("Press Enter to roll dice again")
        exit_choice = input("Your choice: ")
        
        if exit_choice.strip().lower() == "m":
            return
        
def main():
    while True:
        print("\n----Multi Purpose Calculator Tool v2----")
        main_choice = input("""
        What would you like to do?

        -Generate Shapes:    Enter S
        -Flip a coin:        Enter F
        -Calculate Interest: Enter C
        -Roll a dice:        Enter D
        Enter Q to Quit

        Your choice: """).strip().lower()

        match main_choice:
            case "s":
                shapes()
            case "f":
                flip_coin()
            case "c":
                calculate_interest()
            case "d":
                roll_dice()
            case "q":
                break
            case _:
                print("\nSorry, that's not a valid choice")
                input("Press Enter to try again")
        
if __name__ == "__main__":
    main()