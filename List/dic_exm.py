# Take the digit from the user and show in character form.

digit_form={
    '1':'One',
    '2':'Two',
    '3':'Three',
    '4':'Four',
    '5':'Five'
}

phone=input('Enter numbers: ')
output=''

for ch in phone:
    output+=digit_form.get(ch,'!')+' '

print(output)

