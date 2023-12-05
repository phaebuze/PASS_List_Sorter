# Phaedra's PASS Session
# Dec. 04, 2023
# Password validation

def validatePassword(password):
    upper = False
    lower = False
    digit = False
    length = False
    
    if (len(password) >= 8):
        length = True
    
    for char in password:
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
        message += "\n\ttoo short"
    
    return message
    


print("Password Checker \nMust have:",
      "\n\t1 uppercase letter",
      "\n\t1 lowercase letter",
      "\n\t1 digit",
      "\n\t8 characters in length")
      
password = input("Enter password: ")

validity = validatePassword(password)

print("Password is " + validity)




