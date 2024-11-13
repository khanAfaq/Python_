# Car Game..

print('\n **Car Game **\n')

command=''
started=False
while True:
    command=input('>').lower()
    if(command=='start'):
        if started:
            print('Car is already started..')
        else:
            started=True
            print('Car is started..')
    elif(command=='stop'):
        if not started:                         # same Started = true.
            print('Car is already stoped..')
        else:
            started=False
            print('Car is stoped..')
    elif(command=='help'):
        print("""
>Start -- To start the car
>Stop -- To stop the car
>Quit -- To quit 
""")
    elif(command=='quit'):
        break
    else:
        print("I don't understand:(")

