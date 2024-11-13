# Module:
# used to have declare some functions or variables which are 
# used in the project several times.
# so, made a module and call where it is being used by:
# import ---.py


# Example:
# we have a module that give us max number in a list 
# consider as a module call it and find the max number.

    
import utiles

numbers=[10,50,80,60,70,81]

maximun=utiles.find_max(numbers)
print(f'The maximum number in list is: {maximun}')

