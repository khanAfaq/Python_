def emogi_converter(message):

    words=message.split(' ')

    Emogi={
        ':)':'😂',
        ':(':'😒'
    }

    output=''
    for word in words:
        output+=Emogi.get(word,word)+' '
    return output

# print(emogi_converter('Happy :)'))
# print(emogi_converter('Sad :('))
message=input('> ')
print(emogi_converter(message))