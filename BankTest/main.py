import time
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


all_accounts = {}


def A():
    firstName = input("What is your first name?  > ")
    lastName = input("What is your last name?  > ")
    age = input("What is your age?  > ")
    balance = input("How much would you like to deposit? > ")
    account_number = len(all_accounts) + 1
    user_account = {
        "FirstName": firstName,
        "lastName": lastName,
        "age": age,
        "balance": balance
    }
    all_accounts[account_number] = user_account
    print(all_accounts)
    time.sleep(3)
    clear()


def wrongInput():
    print("That is the wrong input, try again.")
    time.sleep(3)
    clear()


def C():
    accountsNumber = int(input('Enter your account number > '))
    balance = all_accounts[accountsNumber]['balance']
    print(f"Your balance is {balance} dollars.")
    time.sleep(3)
    clear()


def W():
    accountsNumber = int(input('Enter your account number > '))
    withdrawAmount = input("How much would you like to withdraw? > ")
    balance = all_accounts[accountsNumber]['balance'] - int(withdrawAmount)
    if withdrawAmount >= 0:
        print(f"You took out {withdrawAmount} dollars. \nNew Total: {withdrawAmount}")
        all_accounts[accountsNumber]['balance'] = withdrawAmount
        time.sleep(2)
        clear()
    elif withdrawAmount < 0:
        print("You don't have enough money :(. Earn more pls.")
        time.sleep(2)
        clear()


def D():
    accountsNumber = int(input('Enter your account number > '))
    depositAmount = input("How much would you like to deposit?  > ")
    balance = all_accounts[accountsNumber]['balance']
    deposit = balance + int(depositAmount)
    print(f"New Total: {deposit}")
    all_accounts[accountsNumber]['balance'] = deposit


while True:

    print("___________________________________________________________________________")
    print("")
    print("Hello, Welcome to Ethan's Bank Service!")
    print("Type A to add an account, W to withdraw, C to check balance, and D to deposit money")
    print("")
    print("___________________________________________________________________________")
    print("")

    choice = input("> ")
    if choice == "C":
        C()
        continue

    elif choice == "W":
        W()
        continue

    elif choice == "A":
        A()

        continue

    elif choice == "D":
        D()
        continue

    else:
        wrongInput()
        continue
