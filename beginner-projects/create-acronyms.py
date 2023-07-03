"""
Author: Kadir KAYA
Date: 3.7.2023
Description: This code sample creates acronym for given phrase.
"""

# get phrase from user
user_input = input('Enter a phrase: ')
text_list = user_input.split()
print(text_list)

# creating acronym
acronym = ''
for i in text_list:
    acronym = acronym + i[0].upper()
print(acronym)