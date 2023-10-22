'''Welcome 
This is a NUMBER GUESSING GAME where the computer will guess a number between 1 and 50....You can choose your level of difficulty which will give you the required number of attempts....The computer will provide you the signs  whether you are close to the guess or not....
So lets start...'''
'''Last modified at 22/10/2023 6:47pm
 Author VJ 13 SS'''
import random
print('WELCOME TO FIND THE GUESSING NUMBER GAME ')
print('Let me guess a number between 1 and 50' )
num=random.randint(1,50)
win='false'
difficulty=input('Enter your difficulty need..."easy" .... or "hard" ').lower()
if(difficulty=='easy'):
	attempts=10
elif(difficulty=='hard'):
	attempts=5
else:
	print('error')
	attempts=0
chances=0
while(chances!=attempts):
	print(f'You have {attempts} attempts')
	guess=int(input('Enter your gussed number '))
	if(guess>num+5):
		print('You are too high ')
		attempts=attempts-1
	elif(guess<num-5):
		print('You are too low ')
		attempts=attempts-1
	elif(guess==num):
		print('You won')
		win='true'
		exit(1)
	else:
		print('You are too close ')
		attempts=attempts-1
if(win=='false'):
	print('You lose')
	print(f'The number is {num}')