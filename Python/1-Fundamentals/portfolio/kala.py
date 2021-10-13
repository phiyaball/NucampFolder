#!/usr/bin/python3

import time
import sys
import itertools
import threading


'''
Welcome to Kala. You've arrived in a location between space and time. 
'''
print("You've arrived in a void, where time and space doesn't exist. All you hear is nothingness, see nothingness.")

time.sleep(5)

done = False
# Animation for reigstration, found this on the internet and modified it for this app
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r.... ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True

done = True

print("\rSuddenly a voice calls out to you..")
time.sleep(2)
print("Who goes there?")
time.sleep(2)
# Figure out a way to incorperate the characters into a list of selectable characters, and move the selected characters out of the list into another list for a chosen character
while True: 
    print("\n 1. Chrona - Master of time \n 2. Beebo - A time worm \n 3. Roland Rolexo - the watch maker")
    char_select = input("\r Choose your character:")
    if char_select == '1':
        print("Hello Chrona of Swtitzerville, your peopple are born with the innate ability to tell time, you are able to transport yourself from any time period to the next but only at Random")
        time.sleep(10)
        continue
    if char_select == '2':
        print("Hello Bebbo, you are an ugly creature aren't you? \r your origin is unknown but it is said your species crawled out of Einstein's wormhole. Time worms have 3 lives")
        time.sleep(10)



#### The player arrives in the void, where space and time doesn't exist. Choose a character
## Prompt the user to press one to

#### Character 1, can return to the void at anytime, character 2, has a time bomb that can blow up an entire world(world would be shown blown for future chars)

