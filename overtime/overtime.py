#!/usr/bin/python3

from emoji import emojize
from dialog import doing_here, door_appears, greetings, outlaw2, this_place, who_are_you, arrive_frontier, bartender, pianist, outlaw
from animation import animate_t
import time
from threading import Thread
import itertools
import names
from frontier_questions import quiz

greetings()

player_input = input("Enter your name: ")
print("")
time.sleep(2)
print("I don't like it...")
print("")
print("I'm going to call you:")
print("")
time.sleep(2)
player_name = (names.get_full_name())
print(player_name)
time.sleep(2)
global new_name
print("")
print("So what was your name again? ")
time.sleep(2)
new_name = input("Enter your new name:(Exactly shown or else!!)")
if new_name != player_name:
    print("I don't know you, you're dead to me!")
    animate_t(5)
    print("         \n\n GAME OVER!!!!!          ")
    exit()

questions_asked = []
print("")
time.sleep(2)
print("That's what I thought, \n Hello, " + new_name)
while True:
    if len(questions_asked) == 3:
        break
    print("")
    time.sleep(2)
    if "1" not in questions_asked:
        print ("1. Who are you?")
    if "2" not in questions_asked:
        print("2. What am I doing here?")
    if "3" not in questions_asked:
        print("3. What is this place?")
    ask_question = input("\n (Choose 1-3): ")
    if ask_question in questions_asked:
        print("You already asked that!")
        continue
    if ask_question in ["1", "2", "3"]:
        questions_asked.append(ask_question)
    if ask_question == "1":
        who_are_you()
    elif ask_question == "2":
        doing_here()
    elif ask_question == "3":
        this_place()
# print a gazillion doors
door_appears()
print("")
a_string = ":door:"
for line in range(3):
  result = a_string * 80
  print(emojize(result))

# not so fast user input, not my code, modified it a bit
answer = None
def check():
    time.sleep(1)
    if answer != None:
        return
    print("Too Slow!")
    time.sleep(1)
    print("Hit Enter to open a random door")
Thread(target = check).start()

answer = input("Pick a door (1-100): ")
animate_t(3)

arrive_frontier()

questions_asked2 = []
while True:
    if len(questions_asked2) == 3:
        break
    print("")
    time.sleep(2)
    if "1" not in questions_asked2:
        print ("1. Talk to the bartender")
    if "2" not in questions_asked2:
        print("2. Talk to the painist")
    if "3" not in questions_asked2:
        print("3. Talk to the outlaw")
    ask_question = input("\n (Choose 1-3): ")
    if ask_question in questions_asked2:
        print("You already asked that!")
        continue
    if ask_question in ["1", "2", "3"]:
        questions_asked2.append(ask_question)
    if ask_question == "1":
        bartender()
        print(emojize(":wine_glass:"))
    elif ask_question == "2":
        pianist()
    elif ask_question == "3":
        print("Howdy " + new_name)
        outlaw()
print("")
print("\n The outlaw grabs your shoulder as you try to walk away")
outlaw2()
animate_t(5)

# https://github.com/mindninjaX/Python-Projects-for-Beginners/blob/master/Quiz%20Game/Quiz%20Game.py - not my code

def check_ans(question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the answer provided by user is correct.
    Converts all answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[question]['answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for question_id, ques_answer in quiz.items():
        for key in ques_answer:
            print(key + ':', ques_answer[key])

print("")
print("")
# python project.py
while True:
    score = 0
    for question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[question]['question'])
            answer = input("Enter Answer (To move to the next question, type 'skip') : ")
            if answer == "skip":
                break
            check = check_ans(question, answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

print(f"Your final score is {score}!\n\n")
print("Want to know the correct answers? Please see them below! ;)\n")
print_dictionary()
print("Thanks for playing! 💜")