import random

print('''This is a number game. The rules are you guess a number Im thinking and I will tell you if its too high or too
low. You will only get 3 chances
''')

r = random.randint(1 , 10 )

guesscounter = 3
while guesscounter <=3 and guesscounter != 0 :
    guess = int(input('okay now guess what Im thinking? '))
    if  r == guess:
       print('congrats you win' )
       break;
    if r > guess:
        guesscounter = guesscounter -1
        print("the number im thinking is a little bit bigger. try again ")
    elif r < guess:
        guesscounter = guesscounter =-1
        print (
            'the number im thinking is a little bit smaller. try again and you only have ')
if guesscounter == 0:
    print ("oh you have no more chances left :( Game over " )
