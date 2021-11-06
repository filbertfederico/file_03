<<<<<<< HEAD
import random
randomint = random.randint(1, 100)

x = int(input ("Input a number between 1 - 100 :"))

while x != "randomint":
    if x > 1 or x < 100 :
        if x == randomint :
            print ("correct")
            break
        elif x < randomint :
            print ("too low")
            x = int(input ("Input a number between 1 - 100 :"))
        elif x > randomint :
            print ("too high")
            x = int(input ("Input a number between 1 - 100 :"))
        else :
            print ("incorrect input")    
=======
import random
randomint = random.randint(1, 100)

x = int(input ("Input a number between 1 - 100 :"))
print (x)

if x < 1 or x > 100 :
    print ("invalid input")
else :
    if x == randomint :
        print (x,"correct")
    else :
        print ("incorect, computer guessed :", randomint) 
>>>>>>> 58e8fd07329be9b8c53b96ac0bba3fbeff4b7e6c
