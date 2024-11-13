# Print the following:
# xxxxx
# xx
# xxxxx
# xx
# xx

# my_x=[5,2,5,2,2]
# for x_count in my_x:
#     print(x_count*'x')


my_x=[5,2,5,2,2]
for x_count in my_x:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)