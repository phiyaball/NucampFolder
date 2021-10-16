"""
            ---------- Task One ----------
    - Declare a class and give it the name "User"
    - The __init__ method has parameters defined as
      (self, name, pin, password)
    - The attribute of the User class are defined as
       name, pin, and password
"""


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    """
            ---------- Task Two ----------
    The "User" class should have three methods:
        * change_name - changes the name of User
        * change_pin - changes the PIN code of User
        * change_password - changes the password of User
    """

    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_pw):
        self.password = new_pw


"""
            ---------- Task Three ----------
    - Declare a class and give it the name "BankUser"
    - "BankUser" class will inherit the "User" class
    - The __init__ method has parameters defined as
      (self, name, pin, password)
    - The super method has parameters defined as
      (name, pin, password)
    - The attributes of the "BankUser" is balance with
      a default value of zero.
"""


class BankUser(User):

    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    """
            ----------Task Four ----------
        The "BankUser" class should have three methods:
            * show_balance- prints the balance of the User
            * withdraw - withdrawing money decreases the account balance
            * deposit - depositing money increases the account balance
    """

    def show_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    """
            ----------Task Five ----------
        Create two more methods for the BankUser class:
            * transfer_money
                - Transfers money to another User if
                - correct PIN is given for transferring User
            * request_money
                - Will ask for the PIN of the User being requested for money.
                - If credentials are correct,
                    - Will ask for and validate the password of the User requesting money as well,
                    - Then complete the transfer, removing money from one account and adding the same amount to the other.
    """

    def transfer_money(self, user, amount):
        print("You are transferring $" + str(amount), "to", user.name)
        print("Authentication required")
        pincode = int(input("Enter your PIN: "))
        if pincode != self.pin:
            print("Invalid PIN. Transaction canceled.")
            return False
        print("Transfer authorized")
        print("Transferring $" + str(amount) + " to " + user.name)
        self.balance -= amount
        user.balance += amount

        return True

    def request_money(self, user, amount):
        print("You are requesting $" +
              str(amount), "from", user.name)
        print("User authentication is required...")

        pin = int(input("Enter " + user.name + "'s PIN: "))
        if pin != user.pin:
            print("Invalid PIN. Transaction canceled.")
            return False

        password = input("Enter your password: ")
        if password != self.password:
            print("Invalid password. Transaction canceled.")
            return False

        print("Request authorized")
        print(user.name + " sent $" + str(amount))

        user.balance -= amount
        self.balance += amount

        return True


""" Driver Code for Task One """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
''' Output: Bob 1234 password '''

""" Driver Code for Task Two """
# user1 = User("Bob", 1234, "password")
# print(user1.name, user1.pin, user1.password)
# user1.change_name("Bobby")
# user1.change_pin(4321)
# user1.change_password("newpassword")
# print(user1.name, user1.pin, user1.password)
''' Output: Bobby 4321 newpassword '''

""" Driver Code for Task Three """
# bankuser1 = BankUser("Bob", 1234, "password")
# print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)
''' Output: Bob 1234 password 0'''

""" Driver Code for Task Four """
bankuser1 = BankUser("Bob", 1234, "password")
bankuser1.show_balance()
bankuser1.deposit(1000.0)
bankuser1.show_balance()
bankuser1.withdraw(500.0)
bankuser1.show_balance()
''' Output:
        Alice has an account balance of: 0
        Alice has an account balance of: 1000.0
        Alice has an account balance of: 500.0
'''

""" Driver Code for Task Five """
# bankuser1 = BankUser("Bob", 1234, "password")
# bankuser2 = BankUser("Alice", 5678, "alicepassword")
# bankuser2.deposit(5000)
# bankuser2.show_balance()
# bankuser1.show_balance()
# print()

# transferred = bankuser2.transfer_money(bankuser1, 500)
# bankuser2.show_balance()
# bankuser1.show_balance()
# print()

# if transferred:
#     bankuser2.request_money(bankuser1, 250)
#     bankuser2.show_balance()
#     bankuser1.show_balance()

''' Output:
        Alice has an account balance of: 5000
        Bob has an account balance of: 0     

        You are transferring $500 to Bob
        Authentication required
        Enter your PIN: 5678
        Transfer authorized
        Transferring $500 to Bob
        Alice has an account balance of: 4500
        Bob has an account balance of: 500   

        You are requesting $250 from Bob     
        User authentication is required...
        Enter Bob's PIN: 1234
        Enter your password: alicepassword
        Request authorized
        Bob sent $250
        Alice has an account balance of: 4750
        Bob has an account balance of: 250
'''
