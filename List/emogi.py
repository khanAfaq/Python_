# Convert the text into emogy
message=input('Enter your message: ')

# When it see the space it consider 2nd word/name/etc.,
words=message.split(' ')

# Dictionary for the Emogi

Emogi={
    ':)':'😂',
    ':(':'😒'
}

output=''
for word in words:
    output+=Emogi.get(word,word)+' '

print(output)
