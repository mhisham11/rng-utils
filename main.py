import tkinter as tk
import turtle as t
import random
import math 


def shapes():
    print("*****Shape Generator*****")
    print("")

    while True:
        invalid = False
        
        def draw_shape(length, sides):
            #apothem: the distance from the center of a polygon to the midpoint of one of its sides
            apothem = length / (2 * math.tan(math.pi / sides))
            t.clear()
            t.penup()
            t.goto(-length / 2, -apothem)
            t.setheading(0)
            t.pendown()
            angle = 360 / sides
            for x in range(sides):
                t.forward(length)
                t.left(angle)
        

        choice = input("Enter the regular shape you want to render: ")

        if choice.lower() == "circle":
            radius = int(input("Provide the radius for your circle: "))
            t.clear()
            t.penup()
            t.goto(0,0)
            t.setheading(270)
            t.forward(radius)
            t.pendown()
            t.setheading(0)
            t.circle(radius)

        elif choice.lower() == "rectangle":
            length = int(input("Enter the length of your rectangle : "))
            width = int(input("Enter the width of your rectangle : "))

            t.clear()
            t.penup()
            #centers the shape, by moving turtle to the bottom left
            t.goto(-length / 2, -width / 2)
            t.setheading(0)
            t.pendown()

            for x in range(2):
                t.forward(length)
                t.left(90)
                t.forward(width)
                t.left(90)
            

        else:
            length = int(input("Enter the desired side length : "))

            match choice.lower():
                case "square":
                    draw_shape(length, 4)
                case "triangle":
                    draw_shape(length, 3)
                case "pentagon":
                    draw_shape(length, 5) 
                case "hexagon":
                    draw_shape(length, 6)
                case "septagon" | "heptagon":
                    draw_shape(length, 7)
                case "octagon":
                    draw_shape(length, 8)
                case "nonagon":
                    draw_shape(length, 9)
                case "decagon":
                    draw_shape(length, 10)
                case _: 
                    invalid = True
                    print("Sorry, that is not a supported shape.")

        print("")
        print("Enter M to return to the main menu")
        print("Press Enter to generate another shape")
        exit_choice = input("Your choice:")

        if exit_choice.lower() == "m":
            return       
        

def flip_coin():
    count = 0
    headcount = 0
    tailcount = 0

    print("------- Coin Flipper -------")

    #main loop
    while True:
        
        reveal = input("Press Enter to flip a coin")

        result = random.randint(1,2)

        if result == 1:
            print(" ")
            print("Result: Heads")
            print(" ")
            headcount += 1
        else:
            print(" ")
            print ("Result: Tails")
            print(" ")
            tailcount += 1
        count += 1

        print(f"------- That was flip #{count} -------")
        print(f"Total results: {headcount} Heads and {tailcount} Tails")

        print("")
        print("Enter M to return to the main menu")
        print("Press Enter to flip another coin")
        exit_choice = input("Your choice: ")
       
        if exit_choice.lower() == "m":
            return       

def calculate_interest():
    print("---- Interest Calculator ----")

    #main loop
    while True:
        print("")
        principal = "none"
        time_period = "none"
        rate = "none"
        invalid = False

    #displays option selector
        print("Are you dealing with simple or compound interest?")
        print("")
        print("Simple Interest:   Enter S")
        print("Compound Interest: Enter C")
        interest_type=input("Your choice:")

        #checks if option is valid
        if not type(interest_type) == str:
            invalid = True

        if not invalid:

            #simple interest
            if interest_type.lower() == "s":
                #reprompts if input is not a digit
                while not principal.isdigit():
                    principal=(input("Please enter your principal amount: $ "))
                while not rate.isdigit():
                    rate=(input("Please enter your annual interest rate: %"))
                while not time_period.isdigit():
                    time_period=(input("How many years was your money deposited?: "))
                    final_amount=(int(principal)*int(time_period)*(int(rate)/100))+int(principal)

            #compound interest
            elif interest_type.lower() == "c":
                while not principal.isdigit():
                    principal = (input("Please enter your principal amount: $"))
                while not rate.isdigit():
                    rate = (input("Please enter your annual interest rate: %"))
                while not time_period.isdigit():
                    time_period = (input("How many years was your money deposited?: "))
                final_amount = int(principal) * ((int(rate)/100)+1) ** int(time_period)

            #deals with invalid choice at option selector
            elif interest_type.lower() != "s" and interest_type.lower() != "c":
                invalid = True

        #invalid error message
        if invalid:
            print("Please choose a valid option")
            
        #Displaying results
        elif not invalid:
            interest = final_amount - int(principal)
            print("---------------Result------------------")
            print(f"After {time_period} years with a rate of %{rate}: ")
            print(f"Your principle amount is: ${int(principal):.2f}")
            print(f"You now have ${final_amount:.2f}")
            print(f"You gained: ${interest:.2f}")

            print("")
            print("Enter M to return to the main menu")
            print("Press Enter to do another calculation")
            exit_choice = input("Your choice: ")
        
            if exit_choice.lower() == "m":
                return

def roll_dice():
    dice = {"1":"""
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬜️⬛️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
            "2":"""
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
            "3":"""
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬛️⬜️
    ⬜️⬛️⬜️⬜️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
            "4":"""
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
            "5":"""
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬛️⬜️⬜️
    ⬜️⬛️⬜️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",
            "6":"""
    ⬜️⬜️⬜️⬜️⬜️
    ⬜️⬛️⬛️⬛️⬜️
    ⬜️⬛️⬛️⬛️⬜️
    ⬜️⬛️⬛️⬛️⬜️
    ⬜️⬜️⬜️⬜️⬜️""",}

    print("")
    print("---- Dice Roller ----")
    print("")
    
    while True:
        print("")
        dice_total = 0

        dice_count = int(input("How many dice would you like to roll?: "))

        for i in range(dice_count):
            x = random.randint(1,6)
            dice_total += x
            print(dice[f"{x}"])

        print("")
        print(f"Sum of all dice:{dice_total}")  

        print("")
        print("Enter M to return to the main menu")
        print("Press Enter to roll dice again")
        exit_choice = input("Your choice: ")
        
        if exit_choice.lower() == "m":
            return
        
#MAIN MENU LOOP
def main():
    while True:
        print("----Multi Purpose Calculator Tool v2----")
        main_choice = input("""
        What would you like to do?

        -Generate Shapes:    Enter S
        -Flip a coin:        Enter F
        -Calculate Interest: Enter C
        -Roll a dice:        Enter D
        Enter Q to Quit

        Your choice: """)

        match main_choice.lower():
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
                print("")
                print("Sorry, that's not a valid choice")
                input("Press Enter to try again")
        

if __name__ == "__main__":
    main()
