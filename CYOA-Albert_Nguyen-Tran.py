#CYOA - Who wants to be a millionaire
#Albert Nguyen-Tran
#March 12th, 2021


#import
import math
import random
import datetime
import time

#global
global start_time

#date time
def get_elapsed_time_seconds():
    global start_time
    
    current_time = datetime.datetime.now()
    elapsed_time = datetime.datetime(1, 1, 1) + abs(start_time - current_time)

    return elapsed_time.second

#clear screen
def clear_screen():
    title = "Who wants to be a millionaire 2021"
    print("\n"*3)
    print("-"*150)
    print(f'{title:^150}')
    print("-"*150)
    print("\n"*3)
    
#introduction
def introduction():

    print("Get ready, because you're about to play a game for the kind of life changing money that most of just dream about\n")
    time.sleep(2)
    print("This is Who Wants to be a Millionaire\n")
    time.sleep(0.5)

    global name
    name = input("Please welcome our first contestant: ")

    global money
    money = 0

    global blitzstore
    blitzstore = True

    global mathstore
    mathstore = True


    if name.isdigit():
        clear_screen()
        print("Please enter a string. Try again")
        clear_screen()
        time.sleep(0.5)
        introduction()

    else:
        clear_screen()
        time.sleep(0.5)
        which_gamemode()
        clear_screen()

#game mode choices
def which_gamemode():
    
    print(f'Hello {name}\nWhich game mode would you like to play?\nOr would you like to enter the store and check your balance?\n')
    print(f'1: Normal')
    print(f'2: Blitz')
    print(f'3: Math')
    print(f'4: Store')

    command = input("\nEnter your desired game mode: ").upper()

    global askafriend
    askafriend = False

    global asktheaudience
    asktheaudience = False
    
    global fiftyfifty
    fiftyfifty = False
    
    if command == '1':
        clear_screen()
        time.sleep(0.5)
        normal_gamemode()

    elif command == '2' and blitzstore == False:
        clear_screen()
        time.sleep(0.5)
        blitz_gamemode()

    elif command == '2' and blitzstore == True:
        clear_screen()
        time.sleep(0.5)
        print("You do not have access to this game! Buy it in the store")
        clear_screen()
        which_gamemode()
        
    elif command == '3' and mathstore == False:
        clear_screen()
        time.sleep(0.5)
        math_gamemode()

    elif command == '3' and mathstore == True:
        clear_screen()
        time.sleep(0.5)
        math_gamemode()
        print("You do not have access to this game! Buy it in the store")
        clear_screen()
        which_gamemode()
        
    elif command == '4':
        clear_screen()
        time.sleep(0.5)
        store()

    else:
        clear_screen()
        print("Sorry I do not understand, try again")
        clear_screen()
        time.sleep(0.5)
        which_gamemode()

#normal game mode
def normal_gamemode():
    
    global askafriend
    askafriend = True
    
    global asktheaudience
    asktheaudience = True
    
    global fiftyfifty
    fiftyfifty = True

    print("You will be asked 10 questions with increasing difficulty\n")
    time.sleep(1)
    print("The first question is worth $2000, each following question is worth twice the amount as the last\n")
    time.sleep(2)
    print("Press L to enter your lifelines menu. You can call a friend, ask the audience or 50/50\n")
    time.sleep(2.5)
    print("If you answer all 10 questions correctly without using any lifelines, you will win a bonus of $100,000\n")
    time.sleep(2)

    command = input("Are you ready to continue? yes or no: ").lower()

    if command == "yes":
        clear_screen()
        time.sleep(0.5)
        question_1()

    elif command == "no":
        clear_screen()
        print("Returning back in 5 seconds")
        clear_screen()
        time.sleep(5)
        normal_gamemode()

    else:
        clear_screen()
        print("Sorry I do not understand, try again\n")
        clear_screen()
        time.sleep(0.5)
        normal_gamemode()

#lifelines
def lifelines_menu():

    print("Welcome to the lifelines menu\n")
    time.sleep(0.5)

#Inventory Menu
    if askafriend == True:
        print("Press 1 to ask a friend (available)\n")

    elif askafriend == False:
        print("Press 1 to ask a friend (Not available)\n")

    if asktheaudience == True:
        print("Press 2 to ask the audience (available)\n")

    elif asktheaudience == False:
        print("Press 2 to ask the audience (Not available)\n")

    if fiftyfifty == True:
        print("Press 3 to fifty fifty (available)\n")
        print("Press 4 to return back to the question")

    elif fiftyfifty == False:
        print("Press 3 to fifty fifty (Not available)\n")
        print("Press 4 to return back to the question")

    command = input("What would you like to do? ")

#Lifelines for question 1
    if command == "1" and questioncounter == "1" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's A", "I think it's A", "I think it's A", "I think it's A", "I think it's A", "I think it's B", "I think it's C"])

    elif command == "2" and questioncounter == "1" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(70, 90, 1, 5, 1, 3, 1, 1)
        
    elif command == "3" and questioncounter == "1" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["A and B", "A and C", "A and D"])

    elif command == "4" and questioncounter == "1":
        clear_screen()
        time.sleep(0.5)
        question_1()

        
#Lifelines for question 2
    elif command == "1" and questioncounter == "2" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's C", "I think it's C", "I think it's C", "I think it's C", "I think it's A", "I think it's B", "I think it's C"])

    elif command == "2" and questioncounter == "2" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 2, 1, 2, 60, 85, 1, 10)
        
    elif command == "3" and questioncounter == "2" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["C and B", "A and C", "C and D"])

    elif command == "4" and questioncounter == "2":
        clear_screen()
        time.sleep(0.5)
        question_2()


#Lifelines for question 3
    elif command == "1" and questioncounter == "3" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's C", "I think it's C", "I think it's C", "I think it's C", "I think it's D", "I think it's B", "I think it's C"])

    elif command == "2" and questioncounter == "3" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 5, 1, 10, 50, 75, 1, 5)
        
    elif command == "3" and questioncounter == "3" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["C and B", "A and C", "C and D"])

    elif command == "4" and questioncounter == "3":
        clear_screen()
        time.sleep(0.5)
        question_3()


#Lifelines for question 4
    elif command == "1" and questioncounter == "4" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's D", "I think it's D", "I think it's D", "I think it's B", "I think it's C"])

    elif command == "2" and questioncounter == "4" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 5, 1, 5, 1, 15, 40, 70)
        
    elif command == "3" and questioncounter == "4" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["C and D", "A and D", "B and D"])

    elif command == "4" and questioncounter == "4":
        clear_screen()
        time.sleep(0.5)
        question_4()


#Lifelines for question 5
    elif command == "1" and questioncounter == "5" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's B", "I think it's B", "I think it's D", "I think it's B", "I think it's C"])

    elif command == "2" and questioncounter == "5" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 15, 30, 65, 1, 5, 1, 10)
        
    elif command == "3" and questioncounter == "5" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["C and D", "A and D", "B and D"])

    elif command == "4" and questioncounter == "5":
        clear_screen()
        time.sleep(0.5)
        question_5()
        

#Lifelines for question 6
    elif command == "1" and questioncounter == "6" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's A", "I think it's A", "I think it's A", "I think it's B", "I think it's C"])

    elif command == "2" and questioncounter == "6" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(20, 50, 1, 15, 1, 15, 1, 15)
        
    elif command == "3" and questioncounter == "6" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["A and D", "A and B", "A and C"])

    elif command == "4" and questioncounter == "6":
        clear_screen()
        time.sleep(0.5)
        question_6()


#Lifelines for question 7
    elif command == "1" and questioncounter == "7" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's D", "I think it's D", "I think it's B", "I think it's A"])

    elif command == "2" and questioncounter == "7" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 15, 1, 15, 1, 25, 12, 40)
        
    elif command == "3" and questioncounter == "7" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["A and D", "B and D", "C and D"])

    elif command == "4" and questioncounter == "7":
        clear_screen()
        time.sleep(0.5)
        question_7()

#Lifelines for question 8        
    elif command == "1" and questioncounter == "8" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's D", "I think it's D", "I think it's B", "I think it's A"])

    elif command == "2" and questioncounter == "8" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 20, 1, 25, 1, 15, 8, 35)
        
    elif command == "3" and questioncounter == "8" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["A and D", "B and D", "C and D"])

    elif command == "4" and questioncounter == "8":
        clear_screen()
        time.sleep(0.5)
        question_8()

#Lifelines for question 9
    elif command == "1" and questioncounter == "9" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's B", "I think it's A", "I think it's C"])

    elif command == "2" and questioncounter == "9" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 20, 1, 30, 1, 25, 1, 20)
        
    elif command == "3" and questioncounter == "9" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["A and B", "B and D", "B and C"])
        
    elif command == "4" and questioncounter == "9":
        clear_screen()
        time.sleep(0.5)
        question_9()

#Lifelines for question 10
    elif command == "1" and questioncounter == "10" and askafriend == True:
        clear_screen()
        time.sleep(0.5)
        ask_a_friend(["I think it's A", "I think it's B", "I think it's C", "I think it's D"])

    elif command == "2" and questioncounter == "10" and asktheaudience == True:
        clear_screen()
        time.sleep(0.5)
        ask_the_audience(1, 25, 1, 20, 1, 25, 1, 20)
        
    elif command == "3" and questioncounter == "10" and fiftyfifty == True:
        clear_screen()
        time.sleep(0.5)
        fifty_fifty(["A and D", "A and B", "C and C"])

    elif command == "4" and questioncounter == "10":
        clear_screen()
        time.sleep(0.5)
        question_10()

    else:
        clear_screen()
        print("Sorry, try again")
        clear_screen()
        lifelines_menu()

#Default text
def lifelines_text():
    
    print("Use this information wisely")
    print("Please wait 5 seconds before returning to the question")
    clear_screen()
    time.sleep(5)

#Generic text 1
def generic_text1():

    clear_screen()
    print(f'\nThanks for playing, you now have ${money}. Returning to the menu')
    clear_screen()
    time.sleep(2)
    which_gamemode()

#Generic text 2
def generic_text2():

    clear_screen()
    print(f'Thats not an option, try again')
    clear_screen()
    time.sleep(0.5)

#Generic text 3
def generic_text3():
    
    clear_screen()
    time.sleep(0.5)
    lifelines_menu()

def generic_text4():

    clear_screen()
    print(f'\nYou took over 15 seconds to answer, you ended with ${money}. Returning to the menu')
    clear_screen()
    time.sleep(2)
    which_gamemode()
    
#Ask a friend lifeline
def ask_a_friend(option_list):
    
    randomChoice = random.choice(option_list)

    global askafriend
    askafriend = False
    
    print(randomChoice)
    lifelines_text()

#Ask the audience lifeline
def ask_the_audience(aLower, aUpper, bLower, bUpper, cLower, cUpper, dLower, dUpper):

    a = random.randint(aLower, aUpper)
    b = random.randint(bLower, bUpper)
    c = random.randint(cLower, cUpper)
    d = random.randint(dLower, dUpper)

    global asktheaudience
    asktheaudience = False

    print(f'The audience has decided: {a}% a, {b}% b, {c}% c and {d}% d and the rest are undecided')
    lifelines_text()

#Fifty fifty lifeline
def fifty_fifty(option_list):
    
    randomChoice = random.choice(option_list)

    global fiftyfifty
    fiftyfifty = False
    
    print(randomChoice)

    lifelines_text()

#Question 1
def question_1():

    global questioncounter
    questioncounter = "1"

    print("Question 1: What is the capital of the United States?\n")
    print("A: Washington, D.C.")
    print("B: Bejing")
    print("C: Washington State")
    print("D: Hawaii")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "A":
        clear_screen()
        global money
        money += 2000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_2()

    elif command == "B":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_1()

    else:
        generic_text2()
        question_1()

#Question 2
def question_2():

    global questioncounter
    questioncounter = "2"

    print("Question 2: How many sides does a heptagon have?\n")
    print("A: 9")
    print("B: 6")
    print("C: 7")
    print("D: 13")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "C":
        clear_screen()
        global money
        money += 2000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_3()

    elif command == "A":
        generic_text1()
        
    elif command == "B":
        generic_text1()

    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_2()

    else:
        generic_text2()
        question_2()
    
#Question 3
def question_3():

    global questioncounter
    questioncounter = "3"

    print("Question 3: What is Elon Musk's spacecraft company called?\n")
    print("A: Blue Origin")
    print("B: NASA")
    print("C: SpaceX")
    print("D: Boeing")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "C":
        clear_screen()
        global money
        money += 4000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_4()

    elif command == "A":
        generic_text1()

    elif command == "B":
        generic_text1()

    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_3()

    else:
        generic_text2()
        question_3()

#Question 4
def question_4():

    global questioncounter
    questioncounter = "4"

    print("Question 4: What month is St. Patricks Day in?\n")
    print("A: January")
    print("B: August")
    print("C: April")
    print("D: March")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "D":
        clear_screen()
        global money
        money += 8000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_5()

    elif command == "A":
        generic_text1()

    elif command == "B":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_4()

    else:
        generic_text2()
        question_4()

#Question 5
def question_5():

    global questioncounter
    questioncounter = "5"

    print("Question 5: Who is the most recent actor of Captain America\n")
    print("A: Robert Downey Jr.")
    print("B: Chris Evans")
    print("C: Christopher Nolan")
    print("D: Chris Pratt")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "B":
        clear_screen()
        global money
        money += 16000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_6()

    elif command == "A":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_5()

    else:
        generic_text2()
        question_5()

#Question 6
def question_6():

    global questioncounter
    questioncounter = "6"

    print("Question 6: What bodily organ produces the sticky liquid known as bile?\n")
    print("A: Gall Bladder")
    print("B: Kidney")
    print("C: Small intestines")
    print("D: Liver")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "A":
        clear_screen()
        global money
        money += 32000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_7()

    elif command == "B":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_6()

    else:
        generic_text2()
        question_6()

#Question 7
def question_7():

    global questioncounter
    questioncounter = "7"

    print("Question 7: Where is Roger Federer from?\n")
    print("A: Sweden")
    print("B: Italy")
    print("C: Croatia")
    print("D: Switzerland")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "D":
        clear_screen()
        global money
        money += 64000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_8()

    elif command == "B":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "A":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_7()

    else:
        generic_text2()
        question_7()

#Question 8
def question_8():

    global questioncounter
    questioncounter = "8"

    print("Question 8: Which of the following schools have the lowest acceptance rate?\n")
    print("A: Stanford University")
    print("B: India Institute of Technology")
    print("C: Oxford University")
    print("D: Tsinghua University")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()


    if command == "D":
        clear_screen()
        global money
        money += 128000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_9()

    elif command == "B":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "A":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_8()

    else:
        generic_text2()
        question_8()

#Question 9
def question_9():

    global questioncounter
    questioncounter = "9"

    print("Question 9: What comes after a planetary nebule?\n")
    print("A: Black Hole")
    print("B: White Dwarf")
    print("C: Neutron Star")
    print("D: Red Giant")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "B":
        clear_screen()
        global money
        money += 256000
        print(f'Spot on, you now have ${money}')
        time.sleep(0.5)
        question_10()

    elif command == "A":
        generic_text1()

    elif command == "C":
        generic_text1()
        
    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_9()

    else:
        generic_text2()
        question_9()

#Question 10
def question_10():

    global questioncounter
    questioncounter = "10"

    print("Question 10: What insect shorted out an early supercomputer and inspired the term computer bug? \n")
    print("A: Moth")
    print("B: Roach")
    print("C: Fly")
    print("D: Japanese Beetle")
    print("L: Lifelines Menu")
    
    command = input("Please enter your answer: ").upper()

    if command == "A":
        clear_screen()
        global money
        money += 512000
        print(f'Congratulations, you beat the game!')
        time.sleep(0.5)
        beat_the_game()

    elif command == "B":
        generic_text1()

    elif command == "C":
        generic_text1()

    elif command == "D":
        generic_text1()

    elif command == "L":
        generic_text3()
        question_10()

    else:
        generic_text2()
        question_10()

#beat the game (normal)
def beat_the_game():

    if askafriend == True and asktheaudience == True and fiftyfifty == True:
        global money
        money += 100000
        print(f'You won $1024000 + the $100000 bonus = ${money}!\n')
        print(f'Returning to the menu in 5 seconds')
        time.sleep(5)
        clear_screen()
        which_gamemode()

    else:
        print(f'You won ${money}')
        print(f'Returning to the menu in 5 seconds')
        time.sleep(5)
        clear_screen()
        which_gamemode()

#blitz game mode
def blitz_gamemode():
    
    print("You will be asked 5 questions\n")
    time.sleep(1)
    print("The first question is worth $20000, each following question is worth twice the amount as the last\n")
    time.sleep(2)
    print("Here's the catch. You only have 15 seconds to answer each question\n")
    time.sleep(2)

    command = input("Are you ready to continue? yes or no: ").lower()

    if command == "yes":
        clear_screen()
        time.sleep(0.5)
        question_1b()

    elif command == "no":
        clear_screen()
        print("Returning back in 5 seconds")
        clear_screen()
        time.sleep(5)
        blitz_gamemode()

    else:
        clear_screen()
        print("Sorry I do not understand, try again\n")
        clear_screen()
        time.sleep(0.5)
        blitz_gamemode()

def question_1b():

    print("Question 1: The Earth is approximately how many miles away from the sun?")
    print("A: 9.3 million")
    print("B: 193 million")
    print("C: 39 million")
    print("D: 93 million\n")

    
    print("You have 15 seconds starting now")
    
    global start_time
    start_time = datetime.datetime.now()
    
    command = input("Please enter your answer: ").upper()
    seconds_used = get_elapsed_time_seconds()
    
    if command == "D" and seconds_used <= 15:
        clear_screen()
        global money
        money += 20000
        print(f'Spot on, you now have ${money}!')
        time.sleep(0.5)
        question_2b()

    elif command == "D" and seconds_used > 15:
        generic_text4()

    elif command == "B":
        generic_text4()

    elif command == "C":
        generic_text4()

    elif command == "A":
        generic_text4()
        
    else:
        generic_text2()
        question_1b()

def question_2b():

    print("Question 2: Before the American colonies switched to the Gregorian calendar\nOn what date did their new year start?")
    print("A: March 25")
    print("B: July 1")
    print("C: December 1")
    print("D: September 25\n")

    
    print("You have 15 seconds starting now")
    
    global start_time
    start_time = datetime.datetime.now()
    
    command = input("Please enter your answer: ").upper()
    seconds_used = get_elapsed_time_seconds()
    
    if command == "A" and seconds_used <= 15:
        clear_screen()
        global money
        money += 40000
        print(f'Spot on, you now have ${money}!')
        time.sleep(0.5)
        question_3b()

    elif command == "A" and seconds_used > 15:
        generic_text4()
        
    elif command == "B":
        generic_text4()

    elif command == "C":
        generic_text4()

    elif command == "D":
        generic_text4()
        
    else:
        generic_text2()
        question_2b()

def question_3b():

    print("Question 3: Which of the following men does not have a chemical element named after him?")
    print("A: Albert Einstein")
    print("B: Niels Bohr")
    print("C: Isaac Newton")
    print("D: Albert Einstein\n")

    
    print("You have 15 seconds starting now")
    
    global start_time
    start_time = datetime.datetime.now()
    
    command = input("Please enter your answer: ").upper()
    seconds_used = get_elapsed_time_seconds()
    
    if command == "C" and seconds_used <= 15:
        clear_screen()
        global money
        money += 80000
        print(f'Spot on, you now have ${money}!')
        time.sleep(0.5)
        question_4b()

    elif command == "C" and seconds_used > 15:
        generic_text4()
        
    elif command == "B":
        generic_text4()

    elif command == "D":
        generic_text4()

    elif command == "A":
        generic_text4()
        
    else:
        generic_text2()
        question_3b()

def question_4b():

    print("Question 4: According to the United Nations, in what year was the world's population half of its present total?")
    print("A: 1950")
    print("B: 1960")
    print("C: 1970")
    print("D: 1940\n")

    
    print("You have 15 seconds starting now")
    
    global start_time
    start_time = datetime.datetime.now()
    
    command = input("Please enter your answer: ").upper()
    seconds_used = get_elapsed_time_seconds()
    
    if command == "B" and seconds_used <= 15:
        clear_screen()
        global money
        money += 160000
        print(f'Spot on, you now have ${money}!')
        time.sleep(0.5)
        question_5b()

    elif command == "B" and seconds_used > 15:
        generic_text4()
        
    elif command == "D":
        generic_text4()

    elif command == "C":
        generic_text4()

    elif command == "A":
        generic_text4()
        
    else:
        generic_text2()
        question_4b()

def question_5b():

    print("Question 5: How many days make up a non-leap year in the islamic calendar?")
    print("A: 365")
    print("B: 400")
    print("C: 354")
    print("D: 376\n")

    
    print("You have 15 seconds starting now")
    
    global start_time
    start_time = datetime.datetime.now()
    
    command = input("Please enter your answer: ").upper()
    seconds_used = get_elapsed_time_seconds()
    
    if command == "C" and seconds_used <= 15:
        clear_screen()
        global money
        money += 20000
        print(f'Spot on, you now have ${money}!')
        time.sleep(0.5)
        beat_the_game()

    elif command == "C" and seconds_used > 15:
        generic_text4()
        
    elif command == "B":
        generic_text4()

    elif command == "D":
        generic_text4()

    elif command == "A":
        generic_text4()
        
    else:
        generic_text2()
        question_5b()
        
#math game mode
def math_gamemode():
    
    print("You will be asked a question\n")
    time.sleep(1)
    print("This question is worth $50000 if answered correctly \n")
    time.sleep(2)
    print("Here's the catch. You only have 15 seconds to answer each question\n")
    time.sleep(2)

    command = input("Are you ready to continue? yes or no: ").lower()

    if command == "yes":
        clear_screen()
        time.sleep(0.5)
        question_m()

    elif command == "no":
        clear_screen()
        print("Returning back in 5 seconds")
        clear_screen()
        time.sleep(5)
        math_gamemode()

    else:
        clear_screen()
        print("Sorry I do not understand, try again\n")
        clear_screen()
        time.sleep(0.5)
        blitz_gamemode()

#question math
def question_m():
    
#balance
def balance():
    
    print(f'Your balance: ${money}\n')

#store
def store():
    
    print("Welcome to the store!")
    balance()
    
    global blitzstore
    global mathstore
    global money
     
    if blitzstore == True:
        print("1 --> Blitz game mode: $1,000,000")

    elif blitzstore == False:
        print("1 --> Blitz game mode: You already have it!")

    if mathstore == True:
        print("2 --> Math game mode: $2,000,000")
        print("3 --> Return back to the menu\n")
        
    elif mathstore == False:
        print("2 --> Math game mode: You already have it!")
        print("3 --> Return back to the menu\n")
    

    command = input("What would you like to do? ")
    
    if command == "1" and money >= 1000000 and blitzstore == True:
        blitzstore = False
        money = money - 1000000
        clear_screen()
        print("Cool! Returning to the store in 5 seconds\n")
        print("Return back to the menu if you would like to play your new game!")
        time.sleep(5)
        clear_screen()
        store()
        
    elif command == "1" and blitzstore == False:
        clear_screen()
        print("Silly, you already have it! Returning to the store in 5 seconds")
        time.sleep(5)
        clear_screen()
        store()

    elif command == "1" and money < 1000000:
        clear_screen()
        print("You don't have enough money! Returning to the store in 5 seconds")
        time.sleep(5)
        clear_screen()
        store()

    if command == "2" and money >= 2000000 and mathstore == True:
        mathstore = False
        money = money - 2000000
        clear_screen()
        print("Cool! Returning to the store in 5 seconds\n")
        print("Return back to the menu if you would like to play your new game!")
        time.sleep(5)
        clear_screen()
        store()
        
    elif command == "2" and mathstore == False:
        clear_screen()
        print("Silly, you already have it! Returning to the store in 5 seconds")
        time.sleep(5)
        clear_screen()
        store()
        
    elif command == "2" and money < 2000000:
        clear_screen()
        print("You don't have enough money! Returning to the store in 5 seconds")
        time.sleep(5)
        clear_screen()
        store()

    if command == "3":
        clear_screen()
        print("Returning back to the menu in 5 seconds")
        time.sleep(5)
        clear_screen()
        which_gamemode()
        
    else:
        clear_screen()
        print("Sorry please try again")
        time.sleep(0.5)
        clear_screen()
        store()

introduction()




