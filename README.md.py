# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'
# Prompt user for input and Re-assign these
# name = input('what new name would you like?')
# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
#Section 2 - Calculate in what year was the person born? and responde back.
# print something like: 'You said you we're 28 hence you were born in 1991!'

print("What is your name?")#
your_name = input()
print("How old are you in years")
age = input()
print("What colour are your eyes?")
eye_colour = input()
print("What is your hair colour?")
hair_colour = input()


print("Hello", your_name, "!", "your eye colour is",  eye_colour, "your hair colour is", hair_colour, "And you are", age, 
      "so that means you were born in", f"{2020-age}) 

# I want you to use operators
# equate something
# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.

import random

print("guess a number from 1 to 10")
guessed_number = input()
secret_number = random.seed(10)

if guessed_number == secret_number:
    print("Nice you got it!")

else:
    print("dang it! you got the wrong number! try again")

