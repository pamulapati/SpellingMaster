'''
Created on Mar 25, 2013

@author: APamulapati
'''
# Anjali is smart, this is Dad's test code for princess Anjali Spelling homework.

import sys, os, glob, random
import subprocess
import time

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'Y', 'ye', 'yes', 'Yes', 'Sure', 'sure', 'bring it on','add','A','new'):
                return True
            if ok in ('n', 'N','no', 'nop', 'nope', 'No', 'Nope','nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise IOError('refusenik child')
            print (complaint)
            
def randomLine(filename):
    "Retrieve a  random line from a file, reading through the file once"
    fh = open(filename, "r")
    lineNum = 0
    it = ''
    whichLine=0;
    while 1:
        aLine = fh.readline()
        lineNum = lineNum + 1
        if aLine != "":
            #
            # How likely is it that this is the last line of the file ? 
            if random.uniform(0,lineNum)<1:
                it = aLine
                whichLine = lineNum
        else:
            break

    fh.close()
    #print(it+"===>"+str(whichLine)+"===>"+str(lineNum))
    return it,whichLine,(lineNum-1)

def play(word):
      
    #for word in words:
        p=os.system("mpg321 -q  sounds/"+word+".mp3")
        
        
def correctSpelling(word):
     print('Correct spelling is *****'+word+'*****') 

name = input('What is your name?\n')
if name not in ('Anjali', 'Angel'):
    print ('This system servers only Anjali princess, you are not my master go away!!!')
    print ('System shutting down')
else:
    print ('Welcome Dear Anjali, Let us buzz some words')
    if ask_ok('Can we do some spellings?') == 0:
        print ('Hmmm ... ok , let me know when you are in mood for some words.')
    else:
        print ('Ok let us rock on ...') 
       
                   
                      
        print ('Ok , let the Spell Buzz begin.')
        
        which_file = int(input('What do you want to spell from (Enter 1: For latest home work, 2: for all home work, 3: for big list of any words 4: for past misspells) '))
        
        if(which_file == 1):
           filename="recenthomework.txt"
        elif(which_file==2):
           filename="allhomework.txt" 
        elif(which_file==4):
           filename='misspelled.txt'
        else:  		
           filename="biglist.txt"         
        
        
        correct = 0
        count = 0;
        seen = []
      
        ask = True
        while True:
                line,lineNum,size = randomLine(filename);
                if lineNum in seen :
                    continue
                seen.append(lineNum)
                
                question = line.strip()
                if os.path.isfile("sounds/"+question+".mp3") :
                    play(question)
                    answer = input("Enter spelling (q : to quit; r : to repeat):")
                    if(answer == 'q'):
                        break
                    while answer == 'r':
                        play(question) 
                        answer = input("Enter spelling (q : to quit; r : to repeat):")
                    if(answer == question):
                        play('/response/ding')
                        #play('is')
                       
                        print("Excellent! Very good spelling !")
                        correct = correct +1
                    else:
                        play('/response/buzzer')
                        correctSpelling(question)
                        e=open('misspelledfile.txt','a')
                        e.write(question+'\n')
                        e.flush()
                        e.close()
                    count = count +1
                    if(len(seen) >= size):
                        print ('You worked on all words that i have in this section !!!')
                        break
                else:
                    continue

        print ('You answered {0} out of {1} correct !!!'.format(correct,count)) 
