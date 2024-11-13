# Guess game..

print('\nGuess Game\n')

secretNumer=8
guessNumber=0
guessCount=3

while guessNumber<guessCount:
    guess=int(input('Enter a number: '))
    guessNumber+=1
    if(guess==secretNumer):
        print('You win :)')
        break
else:
    print('Try agin :(')

