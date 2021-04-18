import random
import database
import validation
from getpass import getpass

# database = {
#     3059805780 : ["Ayla","Anita","ayla@gmail.com","password",200]
# }
# account = 100
#initialization 
def init():
    print("Welcome to bankPHP")
    AccountAvailability = int(input("Do you have account in our bank? 1(Yes) 2 (No) \n"))
    if AccountAvailability == 1 :
        login()
    elif AccountAvailability == 2 :
        register()
    else: 
        print("You've entered an invalid number, try again ")
        init()

#registration with entering first name,last name ,email,password
def register():
    print("******* Register *******")
    email = input("please enter your email address \n")
    firstName = input("please enter your first name \n")
    lastName = input("please enter your last name \n")
    password = input("Create a password for yourself \n")
    # balance = int(input("How much do you want to put in as your first balance? \n"))

    accountNumber = generationAccountNumber()
   
    isUserCreated = database.create(accountNumber,firstName,lastName,email,password)

    if isUserCreated:
        # using database module to create new user record
        print("Your account has been created")
        print(f"Your account number is {accountNumber}")
        print("=========================================")
        print("Make sure to keep it safe")
        login()
# login with entering account number and password
    else:
        print("Something went wrong, Please try againg")
        register()

def login():
    print("***** Login *****")
    # print(database)
    accountNumberFromUser = input("Please enter your account number? \n")

    isValidAccountNumber = validation.accountNumberValidation(accountNumberFromUser)
    if isValidAccountNumber:

        # passwordFromUser = input("Please enter your password \n")
        password = getpass("What is your password?\n")
        user = database.authenticatedUser(accountNumberFromUser,password)
        newAuth = database.createAuth(accountNumber,newBalance)
        if user:
            bankOperation(user)
        # for accountNumber,userDetails in database.items():
        #     if accountNumber == int(accountNumberFromUser):
        #         if userDetails[3] == passwordFromUser:
        #             bankOperation(userDetails)
        # print("Invalid account number or password. please try again")
        # login()
    else:
        print("Account number Invalid: check that you have up to 10 digits and only integers")
        init()


#bank operation 
def bankOperation(user):
    print(f"Welcome : {user[0]} {user[1]}")
    selectedOptions = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    if selectedOptions == 1 :
        depositOperation()
    elif selectedOptions == 2 :
        withdrawOperation()
    elif selectedOptions == 3 :
        logout()
    elif selectedOptions == 4:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(user)

#withdraw operation
def withdrawOperation():
    print("withdrawal")
    # get current balance
    # get amount to withdraw
    # check if current balance > withdraw balance
    # deduct withdraw amount from current balance
    # display current balance
    withdrawAmount = int(input(f"Your balance is { user[4] } , How much do you want to withdraw? \n"))
    if user[4] > withdrawAmount:
        newBalance = user[4] - withdrawAmount
        update(accountNumber)
    else:
        print("Sorry, you don't have enough money.")
    print(f'Your new balance is {newBalance}')

#Deposit operation
def depositOperation():
    print("deposit operation")
    # get current balance
    # get amount to deposit
    # add deposited amount to current balance
    # display current balance
    depositAmount = int(input(f"Your balance is {user[4]} How much would you like to deposit? \n"))
    newBalance = user[4] + depositAmount
    print(f"Your new balance is {newBalance}")
    update(newBalance)

def setCurrentBalance(user):
    return user[4]
#for logging out of the function
def logout():
    login()
def exit():
    print("Thank you!")

# generating account number
def generationAccountNumber():
    return random.randrange(1111111111,9999999999)
#Actual Banking system
init()


