#!/usr/bin/python3

from banking_pkg import account
import time
import itertools
import threading
import sys

# display a registration bar
def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

# Request initial registration info
print("          === Automated Teller Machine ===          ")
print("            ==     Registration   ==      ")
time.sleep(2)
name = input("\n Enter name to register:")
time.sleep(2)
pin = input("Enter PIN:")
time.sleep(2)
balance = 0

done = False
# Animation for reigstration, found this on the internet and modified it for this app
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rRegistering ' + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(5)
done = True

done = True

# Show balance and user name and PIN validation
print(f"\n\n\n {name} has been registered with a starting balance of ${balance}")
time.sleep(5)
print("\n\n Please log into your account")
while True:
    name_to_validate = input("\n Enter username:")
    time.sleep(2)
    pin_to_validate = input("\n Please enter PIN:")
    time.sleep(2)
    if name_to_validate == name and pin_to_validate == pin:
        print("Login successful")
        break
    else:
        print("Invalid login, please try again")
        continue

time.sleep(2)

while True:
    atm_menu(name)
    option = input("Choose an option: ")
    if option == "1":               # balance
        account.show_balance(balance)
    elif option == "2":             # deposit
        balance = account.deposit(balance)
        account.show_balance(balance)
    elif option == "3":             # withdraw
        balance = account.withdraw(balance)
        account.show_balance(balance)
    else:                           # logout
        account.logout(name)
        break
