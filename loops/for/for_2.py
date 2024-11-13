# Take list of numbers from the user and the show the total:

# Initilized empty list
user_list=[]

# Take input from the user
user_list=input('Enter the numbers sperated by spaces:')

# .split() takes this string and splits it into a list of individual strings based on spaces.
#  So, if user_input is "3 5 8 2", user_input.split() would produce ["3", "5", "8", "2"].

user_list=user_list.split()

print(user_list)

total=0
user_list=[int(num) for num in user_list]
for afaq in user_list:
    total+=afaq
print(user_list)
print(f'The total is: {total}')
