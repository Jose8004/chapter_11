import string

"""
Practice Question 4: Password Validator
Task:
Create a function validate_password that checks 
if a password is strong. A strong password has 
at least 8 characters, contains both uppercase 
and lowercase letters, at least one digit, and 
at least one special character (e.g., !@#$%^&*). 
The function should return True if the password 
is strong, and False otherwise. Store this function 
in a module called password_validator.py.
"""

def validate_password(password):
    
    uppercase = False
    lowercase = False
    digit = False
    special_character = False
    length = False

    flag = True
    while flag:
        if len(password) >= 8:
            length = True
        if len(password) == 0:
            return password
        for character in password:
            if character in string.punctuation:
                special_character = True
            if character.isdigit():
                digit = True
            if character.isupper():
                uppercase = True
            if character.islower():
                lowercase = True
            print("One iteration")
        flag = False

        print(f"upper is: {uppercase}, lowercase is: {lowercase},")
        print(f"digit is: {digit}, special character is: {special_character}, ")
        print(f"length is: {length}")

    if uppercase and lowercase and digit and special_character and length:
        return True
    else:
        return False
