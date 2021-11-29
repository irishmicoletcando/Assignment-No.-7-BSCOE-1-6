# Program 2: Password validator
# Create a program that check if password is valid
# The password is valid if all criteria are met:
# a. Greater than 15 letters
# b. Have at least one capital letter
# c. Have at least one number
# d. Have at least one special char (!@#$%^&*()_+ etc)
# Ex.
# Input: P@ssw0rd+P@ssw0rd
# Output: Valid

# Tip: loop through each character of the input then process it letter by letter

def password_validate():

    lowercase = 0
    uppercase = 0
    number = 0
    special_character_number = 0
    special_character = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

    print("Your password must have at least one capital letter, one number, one special character, and greater than 15 letters.")
    user_password = input("Enter your password: ")

    password_char_count = len(user_password)
    if password_char_count > 15:
        for character in user_password:
            if character.islower():
                lowercase += 1
            if character.isupper():
                uppercase += 1
            if character.isdigit():
                number += 1
            if character in special_character:
                special_character_number += 1

    if lowercase >= 1 and uppercase >= 1 and number >= 1 and special_character_number >=1 and (lowercase+uppercase+number+special_character_number==password_char_count):
        print("Valid Password")

    else: 
        print("Invalid Password")


password_validate()