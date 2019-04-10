print("Made by Aakash Saxena")
import time
loose=("The computer wins, you lose a life")
win=("You win Congrats!!! you get a life")
lives = 3
score = 0
draw = 0
comp_lives = 5
password_list=[]
while True:
    print("Please fill the columns below")
    username = input("Please enter your username\n")
    password = input("Please enter the password\n")
    searchfile = open("account setup.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("Access Granted")
            print("Please wait while loading")
            time.sleep(2.0)
    print("Below is a little description")
    print("___________________________")
    print("")
    print("You start with",lives,"lives and the computer starts with",comp_lives,"lives")
    print("If you win, you get a life")
    print("If you lose, you lose a life")
    print("If you draw, the lives remain the same")
    print("To check for the rules type 'rules'")
    print("To exit the game type 'exit'")
    print("The same rules are applied to the computer")
    print("Do not use capital letters in your choice")
    print("Good Luck!!!")
    print("___________________________")
    while True:
        rps = input("rock, paper, scissors? ")
        import random
        computer = ("rock","paper","scissors")
        computer = random.choice(computer)
        #rock if statements
        if rps=="rock" and computer=="paper":
            print("The computer chose",computer)
            print(loose)
            lives-=1
            comp_lives+=1
        
        if rps=="rock" and computer=="scisors":
            print("The computer chose",computer)
            print(win)
            score+=1
            lives+=1
            comp_lives-=1 
            
        #paper if statements
        if rps=="paper" and computer=="scissors":
            print("The computer chose",computer)
            print(loose)
            lives-=1
            comp_lives+=1
            
        if rps=="paper" and computer=="rock":
            print("The computer chose",computer)
            print(win)
            score+=1
            lives+=1
            comp_lives-=1
            
        #scissors if statements
        if rps=="scissors" and computer=="rock":
            print("The computer chose",computer)
            print(loose)
            lives-=1
            comp_lives+=1
            
        if rps=="scissors" and computer=="paper":
            print("The computer chose",computer)
            print(win)
            score+=1
            lives+=1
            comp_lives-=1

        #draw
        if rps=="rock" and computer=="rock":
            print("The computer chose",computer)
            draw+=1

        if rps=="paper" and computer=="paper":
            print("The computer chose",computer)
            draw+=1

        if rps=="scissors" and computer=="scissors":
            print("The computer chose",computer)
            draw+=1

        #for rules
        if rps=="rules":
            print("________________")
            print("")
            print("RULES")
            print("________________")
            print("Rock beats Scissors")
            print("Paper beats Rock")
            print("Scissors beats Paper")
        
        #Run out of lives
        if lives==0:
            print("You ran out of lives")
            print("YOU LOST!!!")
            print("Your score is",score)
            print("You drew",draw,"times")
            exit = ("Press enter to exit")
        
        if comp_lives==0:
            print("Computer ran out of lives")
            print("YAY!!! YOU WON!!!!")
            print("Your score is",score)
            print("You drew",draw,"times")
            exit = ("Press enter to exit")
            exit()
        
        #for exiting
        if rps=="exit":
            break