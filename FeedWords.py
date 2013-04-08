# Anjali is smart, this is Dad's test code for princess Anjali.

import random,os

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
            
def play(word):
      
    #for word in words:
        p=os.system('mpg321 -q  sounds/'+word+'.mp3')



name = input('What is your name?\n')
if name not in ('Anjali', 'Angel'):
    print ('This system servers only Anjali princess, you are not my master go away!!!')
    print ('System shutting down')
else:
    print ('Welcome Dear Anjali, Please feed me some words')
    if ask_ok('Can you feed me some new words?') == 0:
        print ('Hmmm ... ok , let me know when you are in mood for teaching me new words.')
    else:
        print ('Ok let us rock on ...') 
        add = True
        recenthomeworkfile = open('recenthomework.txt', 'w')
        allhomeworkfile = open('allhomework.txt', 'a')
        count=0
        while(1):
            value = input('Enter new word (q: to quit)')
            if(value =='q'):
                break
            
            #https://ssl.gstatic.com/dictionary/static/sounds/de/0/WORD.mp3
            #do we know this file?
            if os.path.isfile("sounds/"+value+".mp3") == False:
                 os.system('wget https://ssl.gstatic.com/dictionary/static/sounds/de/0/'+value+'.mp3 -P sounds/')
                 if os.path.isfile("sounds/"+value+".mp3") :
                    play(value)
                    recenthomeworkfile.write(value+"\n")
                    allhomeworkfile.write(value+"\n")
                    count = count +1
                 else:
                    print ('I am sorry, i do not know how to speak this word!!!')     
            else:
                    play(value)
                    recenthomeworkfile.write(value+"\n")
                    allhomeworkfile.write(value+"\n")
        recenthomeworkfile.flush()
        recenthomeworkfile.close()
        allhomeworkfile.flush()
        allhomeworkfile.close()    
            
        print ('You added {0} words, thanks for teaching me new words!!! '.format(count))
    
