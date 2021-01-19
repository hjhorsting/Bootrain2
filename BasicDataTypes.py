# 1. Suppose you invested in Bitcoin at the end of 2017 when Bitcoin gained a lot of value.
#    What would be your money at the end of a week if you had invested $1000 with an average
#    daily increase of 12\% ? You can solve the problem using Python.

# Create a variable capital ($1000)
capital = 1000

# Create a variable for daily growth (12%)
daily_growth = 12

# Create a variable for period (7)
period = 7

# Calculate the final growth rate
growth_rate = daily_growth/100*period 

# Calculate result
result = capital + capital*growth_rate
 
# Print result
print("The money end of the week is $", int(result))

# 2. Print the text in quotes with Python. However, you must get the numbers from variables using
# .format() notation.
# Because the text is long, you might consider writing in two lines:
# `"When we buy bitcoin with 1000 USD at the beginning of the week, we would earn 1210.68 USD at the 
# end of the week, with an average gain of 12\%."`

dollars_begin = 1000
dollars_end   = 1210.68
percentage    = 0.12

print("When we buy bitcoin with {:.0f} USD at the beginning of the week, we \n \
 would earn {:.2f} USD at the end of the week, with an average gain\
 of {:.0%}.".format(dollars_begin, dollars_end, percentage))

# 3. Get the temperature in Fahrenheit from user and write a code to convert it to Celcius.
# For conversion, you can use this formula: C = (5/9) * (F - 32)

F = input("Enter the temperature in Fahrenheit: ") 
C = (5/9) * (float(F) - 32)
print("Temperature in Celsius : {:.3}".format(C))

# 4. Get a three digit number the from user and calculate the sum of the digits in the
# integer.

digit = input("Give a three number digit: ")
d0 = int(digit[0])
d1 = int(digit[1])
d2 = int(digit[2])
print("The sum of digits in the number is", d0 + d1 + d2)

# 5. Write some code to calculate the hypotenuse of a right angled triangle. 
# Get the side lengths from the user.

f = input("Give the first side length: ")
s = input("Give the second side length: ")

f_number = float(f)
s_number = float(s)

h = (f_number**2 + s_number**2)**0.5
print("The length of the hypotenuse is {:.2f}".format(h))