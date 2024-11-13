birth_year=input('Enter your Birth year:')
# Conversion of String into integer..
current_age=2024-int(birth_year)
# Direct show it..
print(current_age)
# Error :(
#print('You are'+ current_age +'old') Mixing up String and integer together
print('You are '+str(current_age)+' years old')
# Check the dataType of particular variable..
print(type(birth_year))
print(type(current_age))

