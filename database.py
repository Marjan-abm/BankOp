# create record
# update record
# read record
# delete record
# CRUD

# find user
import os
import validation
userDbPath = "C:/Users/marja/Desktop/reskillProject/BankOperation/DATA/userRecord/"
authPath = "C:/Users/marja/Desktop/reskillProject/BankOperation/Data/authSession/"

def createAuth(accountNumber,firstName,lastName,email,password,newBalance):
    try:
        f = open(authPath + str(accountNumber) + ".txt" , "x")
        userAuth = firstName + "," + lastName + ","+ email + "," + password + "," + str(newBalance)
        
        completionState = False
    except FileExistsError:
        doesFileContainData = read(authPath + str(accountNumber) + ".txt")
        if not doesFileContainData:
            delete(accountNumber)
        # print("user already exist")
        # delete(accountNumber)
        # delete the already created file and print out error, then return false
        # check content of file before deleting
    else:
        f.write(str(userData));
        completionState = True
    finally:
        f.close();
        return completionState

def create(accountNumber, firstName,lastName,email,password):
    # create a file 
    # name of the file would be accountNumber.txt
    # add the user details to the file
    # return true
    # if saving to file fails , then delete created file
    userData = firstName + "," + lastName + ","+ email + "," + password + "," + str(0)
    if doesAccountNumberExist(accountNumber):
        return False
    if doesEmailExist(email):
        print("user already exists")
        return False

    completionState = False
    try:
        f = open(userDbPath + str(accountNumber) + ".txt" , "x")
    except FileExistsError:
        doesFileContainData = read(userDbPath + str(accountNumber) + ".txt")
        if not doesFileContainData:
            delete(accountNumber)
        # print("user already exist")
        # delete(accountNumber)
        # delete the already created file and print out error, then return false
        # check content of file before deleting
    else:
        f.write(str(userData));
        completionState = True
    finally:
        f.close();
        return completionState
    

def read(accountNumber):
    # find user with account number
    # fetch content of the file
    isValidAccountNumber = validation.accountNumberValidation(accountNumber)
    try:
        if isValidAccountNumber:
            f = open(userDbPath + str(accountNumber) + ".txt" , "r")
        else:
            f = open(userDbPath + accountNumber , "r")
    except FileNotFoundError:
        print("user not found")
        
    except FileExistsError:
        print("user doesn't exist")
    
    except TypeError:
        print("Invalid account number format")
        
    else:
        return f.readline()
    return False        



def update(accountNumber):
    print("update user record")
    try:
        f = open(userDbPath + str(accountNumber) + ".txt" , "x")
        # userData = firstName + "," + lastName + ","+ email + "," + password + "," + str(newBalance)
        accountBalance = str(newBalance)
        f.write(newBalance)
        f.close()

    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return true

def delete(accountNumber):
    isDeleteSuccessful = False
    # find user with account number
    # delete the user record (file)
    # return True
    if os.path.exists(userDbPath + str(accountNumber) + ".txt"):
        try:
            os.remove(userDbPath + str(accountNumber) + ".txt")
            isDeleteSuccessful = True
        except FileNotFoundError:
            print("user not found")
        finally:
            return isDeleteSuccessful


def doesEmailExist(email):
    allUsers = os.listdir(userDbPath)
    for user in allUsers : 
        userList = str.split(read(user), ',')
        if email in userList:
            return True
    return False

def doesAccountNumberExist(accountNumber):
    allUsers = os.listdir(userDbPath)
    for user in allUsers:
        if user == str(accountNumber) + ".txt":
            return True
    return False

def authenticatedUser(accountNumber,password):
    if doesAccountNumberExist(accountNumber):
        user = str.split(read(accountNumber), ',')
        if password == user[3]:
            return user
    return False
