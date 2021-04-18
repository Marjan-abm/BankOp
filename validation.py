def accountNumberValidation(accountNumber):
    #check if account number is not empty
    #if account number is 10 digits
    #if the account number is an integer 
    #for knowing the len of an integer we need to change it string , this calles casting
    if accountNumber:
        try:
            int(accountNumber)

            if len(str(accountNumber)) == 10:
                return True
            
        except ValueError:
            return False
        except TypeError:
            return False

    return False
