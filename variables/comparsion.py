# if temperature is greater than 30 it's a hot day 
# otherwise if it's less than 10 it is cold
# otherwise it's neither cold or hot

temp=4
if(temp>30):
    print("It's hot day")

elif(temp<10):
    print("It's cold day")

else:
    print("It is neither cold or hot")


print('\n')

# Input from the user having name of less cheracter then 3
# show must contain 3 cheracters 
# can't be more than 6 cheracters
# otherwise it look good

x=input('Enter a name: ')
a=len(x)
b=int(a)
if(b<3):
    print('Must contain 3 cheracters')

elif(b>6):
    print('Not be more than of 6 cheracters')

else:
    print('It look good')

