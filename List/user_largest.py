# Initilized empty list:
my_list=[] 

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the input into a list of numbers and store it in user_list
# Comprehensive list
my_list = [int(num) for num in user_input.split()]

# Display the list
print("List of numbers:", my_list)

# Showing the Max number in my_list:
max=0
for number in my_list:
    if(number>max):
        max=number
print(max)
