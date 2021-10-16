#!/usr/bin/python3

import threading
import time
import itertools
import sys

done = False
# Animation for reigstration, found this on the internet and modified it for this app
def animate():
    global done
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\r.' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def animate_t(seconds):
    global done
    done = False
    t = threading.Thread(target=animate)
    t.start()
    time.sleep(seconds)
    done = True

'''
t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True
'''