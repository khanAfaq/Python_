def emogi_converter():

    message=input('Enter your message: ')
    words=message.split(' ')

    Emogi={
        ':)':'😂',
        ':(':'😒'
    }

    output=''
    for word in words:
        output+=Emogi.get(word,word)+' '

    print(output)
emogi_converter()


# def emogi_converter(message):

#     words=message.split(' ')

#     Emogi={
#         ':)':'😂',
#         ':(':'😒'
#     }

#     output=''
#     for word in words:
#         output+=Emogi.get(word,word)+' '

#     print(output)

# emogi_converter('Happy :)')
# emogi_converter('Sad :(')