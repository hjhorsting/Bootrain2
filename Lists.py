# 1. Write a code to compute the sum of the two lowest numbers and the two highest numbers
# in the following list.
# my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]

# First I sort the list in ascending order
my_list = [34, 56, 76, 45, 2, 12, 67, 98, 37, 54, 66]
my_list.sort() 
print("Sorted list: ", my_list)

lowest = my_list[0]          # Lowest
print("Lowest number:", lowest)
second_lowest = my_list[1]   # Second lowest
print("Second lowest:", second_lowest)
second_highest = my_list[-2] # Second highest
print("Second highest:", second_highest)
highest = my_list[-1]        # Highest
print("Highest:", highest)

# sum of the two lowest numbers and the two highest numbers
sum = lowest + second_lowest + second_highest + highest
print("Sum:", sum, "\n")


# 2. The following two lists contain student names and scores. 
# Write a code that gets the name from the user and prints the score of that student.

# names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
#         "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]

# scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]

names = ["David", "Michael", "John", "James", "Greg", "Mark", "William", "Richard", "Thomas", "Steven", 
        "Mary", "Susan", "Maria", "Karen", "Lisa", "Linda", "Donna", "Patricia", "Debra", "Eric"]
scores = [99, 87, 78, 86, 68, 94, 76, 97, 56, 98, 76, 87, 79, 90, 73, 93, 82, 69, 97, 98]
print(names[names.index("David")], scores[names.index("David")])
print(names[names.index("Michael")], scores[names.index("Michael")])
print(names[names.index("John")], scores[names.index("John")])
print(names[names.index("James")], scores[names.index("James")])
print(names[names.index("Greg")], scores[names.index("Greg")])
print(names[names.index("Mark")], scores[names.index("Mark")])
print(names[names.index("William")], scores[names.index("William")])
print(names[names.index("Richard")], scores[names.index("Richard")])
print(names[names.index("Thomas")], scores[names.index("Thomas")])
print(names[names.index("Steven")], scores[names.index("Steven")])
print(names[names.index("Mary")], scores[names.index("Mary")])
print(names[names.index("Susan")], scores[names.index("Susan")])
print(names[names.index("Maria")], scores[names.index("Maria")])
print(names[names.index("Karen")], scores[names.index("Karen")])
print(names[names.index("Lisa")], scores[names.index("Lisa")])
print(names[names.index("Linda")], scores[names.index("Linda")])
print(names[names.index("Donna")], scores[names.index("Donna")])
print(names[names.index("Patricia")], scores[names.index("Patricia")])
print(names[names.index("Debra")], scores[names.index("Debra")])
print(names[names.index("Eric")], scores[names.index("Eric")])
print()

# 3. By using the two lists above, what is the maximum score and how many students got
# that score?

scores.sort()
print(scores)
maximum = scores[-1]
print("The maximum score is ", maximum)
count = scores.count(maximum)
print(count, "students got that score")
print()

# 4. We can confuse about how many days a month is. Create a list to handle it. 
# You will have month names and day counts in your list together as a nested list.

months = ["January", "February", "March", "April", "May", "June", "July", "August",
         "September", "Oktober", "November", "December"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_days = [months, days]

print(months_days[0][0], "has", months_days[1][0], "days.")
print(months_days[0][1], "has", months_days[1][1], "days.")
print(months_days[0][2], "has", months_days[1][2], "days.")
print(months_days[0][3], "has", months_days[1][3], "days.")
print(months_days[0][4], "has", months_days[1][4], "days.")
print(months_days[0][5], "has", months_days[1][5], "days.")
print(months_days[0][6], "has", months_days[1][6], "days.")
print(months_days[0][7], "has", months_days[1][7], "days.")
print(months_days[0][8], "has", months_days[1][8], "days.")
print(months_days[0][9], "has", months_days[1][9], "days.")
print(months_days[0][10], "has", months_days[1][10], "days.")
print(months_days[0][11], "has", months_days[1][11], "days.")
print()

# 5. Now create lists of months for each season. 
# Get month names and day counts from the list that you create before with slicing.
# Name the lists with seasons.

spring = [months_days[0][2:5], months_days[1][2:5]]
summer = [months_days[0][5:8], months_days[1][5:8]]
fall   = [months_days[0][8:11], months_days[1][8:11]]
winter_months = [months_days[0][11], *months_days[0][0:2]]
winter_days = [months_days[1][11], *months_days[1][0:2]] 
winter = [winter_months, winter_days]

print("Spring: ", spring)
print()
print("Summer: ", summer)
print()
print("Fall: ", fall)
print()
print("Winter: ", winter)

# 6. Finally, from the list in the previous question, 
# calculate how many days the summer season lasts.

number = summer[1][0] + summer[1][1] + summer[1][2]
print("The summer season lasts:", number, "days.")




