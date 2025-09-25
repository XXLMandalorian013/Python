#################################################################################################################################################################

# Converting Data Types.

## To convert a float (a decimal number) to an integer (a whole number).

amount = 10.6

amount = int(amount)

print(amount)

## To convert an integer (a whole number) to a float (a decimal number).

amount = 10

amount = float(amount)

print(amount)

#################################################################################################################################################################

# Single quotes vs double quotes.

## Single quotes are used as there are not any apostrophes in the string.

singlequotes = 'John'

print(singlequotes)

## Double quotes are used as there is an apostrophe in the string, else python will think the string ends at the apostrophe.

doublequotes = "John's Warthog"

print(doublequotes)


#################################################################################################################################################################

# Concatenation aka, joining strings/vara together.

first_name = 'John'
last_name = '117'

# adding the two strings/vara together.

full_name = first_name + last_name

print(full_name)

# adding a " " between the two strings, to add a space between them.

full_name = first_name + " " + last_name

print(full_name)


##################################################################################################################################################################

# Input/asking for user input.

name = input("Hello, What is your name?")

print('Nice to meet you' + name)

