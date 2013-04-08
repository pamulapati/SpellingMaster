# Anjali is smart, this is Dad's test code for princess Anjali.

import random

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'Y', 'ye', 'yes', 'Yes', 'Sure', 'sure', 'bring it on'):
                return True
            if ok in ('n', 'N','no', 'nop', 'nope', 'No', 'Nope','nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise IOError('refusenik user')
            print (complaint)

name = input('What is your name?\n')
if name not in ('Anjali', 'Angel'):
    print ('This system serves only Anjali princess, you are not my master go away!!!')
    print ('System shutting down')
else:
    print ('Welcome Dear Anjali, Let us do some math')
    if ask_ok('Can we do some math?') == 0:
        print ('Hmmm ... ok , let me know when you are in the mood for some math.')
    else:
        print ('Ok let us rock on ...') 
        
        num_problems = int(input("How many problems do you want to solve?"))
        
        num_digits = int(input("Number of digits in problems?"))
        count = 0
        correct = 0;
        if num_problems <=0 and num_digits <= 0 :
            print ("Hmmm ... i thought you wanted to play with me :-( !!!!")
            
        else:
            while count < num_problems:
                choice = random.randint(1, 2)
                number1 = random.randint((10**num_digits)/10,(10**num_digits)-1)
                number2 = random.randint((10**num_digits)/10,(10**num_digits)-1)
                if choice == 2 and number2 > number1 :
                    continue
                
                if choice == 1 :
                    answer = number1+number2
                elif choice == 2 :    
                    answer = number1-number2
                print ("What is?\n")
                print (" {0}".format(number1))
                if choice == 1 :
                    print ("+")
                
                if choice == 2 :
                    print ("-")
                
                print (" {0}".format(number2))
                print ("===")
                
                guess = int(input())
                    
                if answer == guess:
                    print ('Good job, {0}! You got it!'.format(name))
                    correct = correct +1
                else:
                    print ('Nope. Answer is {0}'.format(answer))
                    
                count = count+1
                
                    
            print ('You answered {0} out of {1} correct !!!'.format(correct,count))   
            
            percentage = (correct/count)*100;
            if percentage == 100:
                print ("You are a mathematician. You rock!!!")
            elif percentage >= 95:
                print ("Next time better luck ")
            elif percentage <= 95 and percentage >= 50:
                print ("Ok you need major practice!!! ")
            else :    
                print ("Let's try again!!! ")
