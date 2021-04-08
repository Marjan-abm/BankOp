import random
database = {}
account = 100
#initialization 
def init():
    print("Welcome to bankPHP")
    AccountAvailability = int(input("Do you have account in our bank? 1(Yes) 2 (No) \n"))
    if AccountAvailability == 1 :
        login()
    elif AccountAvailability == 2 :
        print(register())
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
    accountNumber = generationAccountNumber()

    database[accountNumber] = [firstName, lastName,email,password]
    print("Your account has been created")
    print(f"Your account number is {accountNumber}")
    print("=========================================")
    print("Make sure to keep it safe")
    login()
# login with entering account number and password

def login():
    print("***** Login *****")
    accountNumberFromUser = int(input("Please enter your account number? \n"))
    passwordFromUser = input("Please enter your password \n")
    for accountNumber,userDetails in database.items():
        if accountNumber == accountNumberFromUser:
            if userDetails[3] == passwordFromUser:
                bankOperation(userDetails)
        else: 
            print("Invalid account number or password. please try again")
            login()
    
#bank operation 
def bankOperation(userDetails):
    print(f"Welcome : {userDetails[0]} {userDetails[1]}")
    selectedOptions = int(input("What would you like to do? (1) deposit (2) withdrawal (3) Logout (4) Exit \n"))
    if selectedOptions == 1 :
        deposit()
    elif selectedOptions == 2 :
        withdraw()
    elif selectedOptions == 3 :
        logout()
    elif selectedOptions == 4:
        exit()
    else:
        print("Invalid option selected")
        bankOperation(userDetails)

#withdraw operation
def withdraw():
    withdrawAmount = int(input(f"Your balance is { account } , How much do you want to withdraw? \n"))
    newAccount = account - withdrawAmount
    print(f'Your new balance is {newAccount}')

#Deposit operation
def deposit():
    depositAmount = int(input(f"Your balance is {account} How much would you like to deposit? \n"))
    newAccount = account + depositAmount
    print(f"Your new balance is {newAccount}")

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


