def validateUsername(username):
    upper = False
    lower = False
    digit = False
    length = False
    
    if ( (len(username) >= 5) and (len(username) <= 15) ):
        length = True
    
    for char in username:
        if (char.isupper()):
            upper = True
        
        if (char.islower()):
            lower = True 
        
        if (char.isdigit()):
            digit = True
    
    if (upper and lower and digit and length):
        message = "Valid"
    else:
        message = "Not Valid"
        
    if (not upper):
        message += "\n\tno uppercase"
    
    if (not lower):
        message += "\n\tno lowercase"
    
    if (not digit):
        message += "\n\tno digit"
    
    if (not length):
        if (len(username) > 15):
             message += "\n\ttoo long"
        else:
            message += "\n\ttoo short"
    
    return message
    


print("Username Checker \nMust have:",
      "\n\t1 uppercase letter",
      "\n\t1 lowercase letter",
      "\n\t1 digit",
      "\n\tBetween 5 and 15 characters (inclusive) in length")
      
username = input("Enter Username: ")

validity = validateUsername(username)

print("Username is " + validity)

