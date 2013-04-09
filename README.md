#make sure you have python as executable
 sudo apt-get install python3.2
# Make sure you have mp3 player.
	sudo apt-get install alsa-utils
	sudo apt-get install mpg321
	sudo reboot
	sudo modprobe snd_bcm2835
    sudo amixer cset numid=3 1
	
    Test sound by running mpg321 any mp3 file. 
	On raspebery pi try following:
	 mpg321 /usr/share/scratch/Media/Sounds/Animal/Cat.mp3 
# Upload code from git hub to linux into ~/projects/SpellingMaster
# Too feed homework run following:
 pi@raspberrypi ~/projects/SpellingMaster $ sudo python3.2 FeedWords.py
What is your name?
Anjali
Welcome Dear Anjali, Please feed me some words
Can you feed me some new words?sure
Ok let us rock on ...
Enter new word (q: to quit)fun
--2013-04-08 21:08:57--  https://ssl.gstatic.com/dictionary/static/sounds/de/0/fun.mp3
Resolving ssl.gstatic.com (ssl.gstatic.com)... 74.125.228.15, 2607:f8b0:4004:800::100f
Connecting to ssl.gstatic.com (ssl.gstatic.com)|74.125.228.15|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 13791 (13K) [audio/mpeg]
Saving to: `sounds/fun.mp3'

100%[======================================================================================================================>] 13,791      --.-K/s   in 0.01s

2013-04-08 21:09:03 (1.16 MB/s) - `sounds/fun.mp3' saved [13791/13791]

Enter new word (q: to quit)



# To do homework run:
pi@raspberrypi ~/projects/SpellingMaster $ sudo python3.2 SpellingMaster.py
What is your name?
Anjali
Welcome Dear Anjali, Let us buzz some words
Can we do some spellings?sure
Ok let us rock on ...
Ok , let the Spell Buzz begin.
What do you want to spell from (Enter 1: For latest home work, 2: for all home work, 3: for big list of any words 4: for past misspells) 1
Enter spelling (q : to quit; r : to repeat):luck



#
