# Take list of numbers from the user and the show the total:
# This code is more efficent:


# Initialize an empty list
user_list = []

# Take input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the input into a list of numbers and store it in user_list
# Comprehensive list
user_list = [int(num) for num in user_input.split()]

# Display the list
print("List of numbers:", user_list)

# Display the total_amount
# total=0
# for amount in user_list:
#     total+=amount
# print(f'The total amount is: {total}')

# Display the total amount using sum()
total = sum(user_list)
print(f'The total amount is: {total}')