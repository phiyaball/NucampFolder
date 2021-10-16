#!/usr/bin/python3

import time
from animation import animate_t
from emoji import emojize

#greeting message
def greetings():
    print(emojize(":zzz:, :zzz:, :zzz:"))
    animate_t(2)
    print("\n You've woken up to what seems like an empty room, void of anything physical, with nothing but a humming noise")
    time.sleep(1)
    print("Suddenly a voice calls out to you")
    time.sleep(1)
    print("\n who goes there?!")

