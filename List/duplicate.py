# Remove the duplicates in the list:

original_list = [1, 2, 5, 1, 6, 7, 6, 8]
unique_list = []
for item in original_list:
    if(item not in unique_list):
        unique_list.append(item)
print(unique_list)

