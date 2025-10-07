# Age var prompt.
# As we are going to used the input as a number later in this script, we must change it to an integer,
# else we will get an error over how age is a string and strings can't be used to do math.
age = int(input("How old are you?\n"))

# Decades var.
# As we are doing a division, we use / to do the math. A single / gives a float answer, while a double // gives a integer answer.
decades = age // 10

# Converting the remaining rounded off years from the var above. The % gives the remainder of the division.
years = age % 10

# Output from above.
# Similar to the age var needing to be a integer, decades needs to be a string to be used in print, else it will error over it being a float.
print(" You are " + str(decades) + " decades and " + str(years) + " years old. ")
