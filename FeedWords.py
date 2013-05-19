# Anjali is smart, this is Dad's test code for princess Anjali.

import random,os
import json
import pprint
import httplib2

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

def word_definition (word):
    print ("------Definition-------")
    df = open("definitions/"+word+".txt")
    definition = df.readline()

    definition = definition.replace("dict_api.callbacks.id100(", "").replace(",200,null)", "").replace("\\x","\\u00");
    #print (definition)    
    definition_list = json.loads(definition)
    #pprint.pprint(definition_list)
    #print type(definition_list)
    #print definition_list['primaries']	
    #pprint.pprint(definition_list['primaries'])
    found = 0
    part_of_speach = []
    if 'primaries' in definition_list:
        for primaries in definition_list['primaries']:
			#pprint.pprint( primaries['entries'])
            for entries in primaries['entries']:
				#pprint.pprint( entries)
				#print "---------------------"
                if entries['type'] == 'meaning':
					#pprint.pprint(entries)
                	if len(entries['terms']) > 0:
                		print(entries['terms'][0]['text'].replace((word),"<Your Word>"))
                		found = 1
					
            if 'labels' in primaries['terms'][0]:
            	part_of_speach.append(" "+ primaries['terms'][0]["labels"][0]['text'])
	
    if not found:
    	if 'webDefinitions' in definition_list:	
            for primaries in definition_list['webDefinitions']:
				#pprint.pprint( primaries['entries'])
            	for entries in primaries['entries']:
					#pprint.pprint( entries)
					#print "---------------------"
            		if entries['type'] == 'meaning':
						#pprint.pprint(entries)
            			if len(entries['terms']) > 0:
            				print(entries['terms'][0]['text'].replace((word),"<Your Word>"))
            				found =0
            	if 'labels' in primaries['terms'][0]:			
            		part_of_speach.append( primaries['terms'][0]["labels"][0]['text'])
    print ("Part of Speach :"+ str(part_of_speach))		
    print ("------End of Definition-------")

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
			
			#Do we have definition file?
            if os.path.isfile("definitions/"+value+".txt") == False:
                 #os.system('wget http://www.google.com/dictionary/json?callback=dict_api.callbacks.id100&q='+value+'&sl=en&tl=en&restrict=pr%2Cde&client=te -P definitions/'+value+'.txt')
            	 resp, content = httplib2.Http().request("http://www.google.com/dictionary/json?callback=dict_api.callbacks.id100&q="+value+"&sl=en&tl=en&restrict=pr%2Cde&client=te")
            	 #print (resp)
            	 #print (content)
            	 definitionfile = open('definitions/'+value+'.txt', 'w')
            	 definitionfile.write(content.decode("utf-8")+"\n")
            	 definitionfile.flush()
            	 definitionfile.close() 
				 
            	 if os.path.isfile("definitions/"+value+".txt") :
            	    word_definition(value)
            	 else:
            	    print ('I am sorry, i do not know how to define this word!!!')     
            else:
                    word_definition(value)
                    	
        recenthomeworkfile.flush()
        recenthomeworkfile.close()
        allhomeworkfile.flush()
        allhomeworkfile.close()    
            
        print ('You added {0} words, thanks for teaching me new words!!! '.format(count))
    
