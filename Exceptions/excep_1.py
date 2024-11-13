try:
    age=int(input('Enter age:'))
    income=20000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("Can't divide by 0.")
except ValueError:
    print('Invalied number.')

