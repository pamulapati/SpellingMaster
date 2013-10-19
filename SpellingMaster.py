'''
Created on Mar 25, 2013

@author: APamulapati
'''
# Anjali is smart, this is Dad's test code for princess Anjali Spelling homework.

import sys, os, glob, random
import subprocess
import time
import json
import pprint

def ask_ok(prompt, retries=4, complaint='Yes or no, please!'):
        while True:
            ok = input(prompt)
            if ok in ('y', 'Y', 'ye', 'yes', 'Yes', 'Sure', 'sure', 'bring it on', 'add', 'A', 'new'):
                return True
            if ok in ('n', 'N', 'no', 'nop', 'nope', 'No', 'Nope', 'nope'):
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
    whichLine = 0;
    while 1:
        aLine = fh.readline()
        lineNum = lineNum + 1
        if aLine != "":
            #
            # How likely is it that this is the last line of the file ? 
            if random.uniform(0, lineNum) < 1:
                it = aLine
                whichLine = lineNum
        else:
            break

    fh.close()
    # print(it+"===>"+str(whichLine)+"===>"+str(lineNum))
    return it, whichLine, (lineNum - 1)

def play(word):
      
    # for word in words:
        p = os.system("mpg321 -q  sounds/" + word + ".mp3")
        
        
def correctSpelling(word):
     print('Correct spelling is *****' + word + '*****') 


def word_definition (word):
    print ("------Definition-------")
    df = open("definitions/" + word + ".txt")
    definition = df.readline()
    definition = definition.replace("dict_api.callbacks.id100(", "").replace(",200,null)", "").replace("\\x", "\\u00");
    # print definition
    definition_list = json.loads(definition)
    # pprint.pprint(definition_list)
    # print type(definition_list)
    # print definition_list['primaries']    
    # pprint.pprint(definition_list['primaries'])
    found = 0
    part_of_speach = []
    count = 0
    if 'primaries' in definition_list:
        for primaries in definition_list['primaries']:
            # pprint.pprint( primaries['entries'])
            for entries in primaries['entries']:
                # pprint.pprint( entries)
                # print "---------------------"
                if entries['type'] == 'meaning':
                    # pprint.pprint(entries)
                    if len(entries['terms']) > 0:
                        count = count+1	
                        print(str(count)+") "+ entries['terms'][0]['text'].replace((word), "<Your Word>"))
                        found = 1
                        
            if 'labels' in primaries['terms'][0]:
                part_of_speach.append(" " + primaries['terms'][0]["labels"][0]['text'])
    
    if not found:
        if 'webDefinitions' in definition_list:    
            for primaries in definition_list['webDefinitions']:
                # pprint.pprint( primaries['entries'])
                for entries in primaries['entries']:
                    # pprint.pprint( entries)
                    # print "---------------------"
                    if entries['type'] == 'meaning':
                        # pprint.pprint(entries)
                        if len(entries['terms']) > 0:
                            count = count+1						
                            print(str(count)+") "+ entries['terms'][0]['text'].replace((word), "<Your Word>"))
                            found = 0
                if 'labels' in primaries['terms'][0]:            
                    part_of_speach.append(primaries['terms'][0]["labels"][0]['text'])
    print ("Part of Speach :" + str(part_of_speach))
    print ("------End of Definition-------") 

name = input('What is your name?\n')
if name not in ('Anjali', 'Angel','Test','Arun','Chins'):
    print ('This system servers only Anjali princess, you are not my master go away!!!')
    print ('System shutting down')
else:
    print ('Welcome Dear Anjali, Let us buzz some words')
    if ask_ok('Can we do some spellings?') == 0:
        print ('Hmmm ... ok , let me know when you are in mood for some words.')
    else:
        print ('Ok let us rock on ...') 
       
                   
                      
        print ('Ok , let the Spell Buzz begin.')
        
        which_file = int(input('What do you want to spell from (Enter 1: Latest home work, 2: All home work, 3: Big list of any words 4: Past misspells 5:Elementry Dictionary) '))
        
        if(which_file == 1):
           filename = name+"/recenthomework.txt"
        elif(which_file == 2):
           filename = name+"/allhomework.txt" 
        elif(which_file == 4):
           filename = name+"/misspelledfile.txt"
        elif(which_file == 5):
           filename = name+"/elementrydct.txt"
        elif(which_file == 3):
           filename = "biglist.txt"         
        
        
        correct = 0
        count = 0;
        seen = []
      
        ask = True
        while True:
                line, lineNum, size = randomLine(filename);
                if lineNum in seen :
                    continue
                seen.append(lineNum)
                
                question = line.strip()
                if os.path.isfile("sounds/" + question + ".mp3") :
                    play(question)
                    answer = input("Enter spelling (q : to quit; r : to repeat d : to define):")
                    answer = answer.strip()
                    if(answer == 'q'):
                        break
                    while not answer or answer == 'r' or answer == 'd':
                        if answer == 'r':
                            play(question) 
                        if answer == 'd':
                            if os.path.isfile("definitions/" + question + ".txt"):
                                word_definition(question) 
                            else:
                                print("Sorry no definition!")
                        answer = input("Enter spelling (q : to quit; r : to repeat d : to define):")
                        answer = answer.strip()                        
                    if(answer == question):
                        play('/response/ding')
                        # play('is')
                       
                        print("Excellent! Very good spelling !")
                        correct = correct + 1
                    else:
                        play('/response/buzzer')
                        correctSpelling(question)
                        e = open(name+'/misspelledfile.txt', 'a')
                        e.write(question + '\n')
                        e.flush()
                        e.close()
                    count = count + 1
                    if(len(seen) >= size):
                        print ('You worked on all words that i have in this section !!!')
                        break
                else:
                    continue

        print ('You answered {0} out of {1} correct !!!'.format(correct, count)) 
