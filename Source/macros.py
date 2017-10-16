import sys, pykeyboard
from keyboard import wait
from time import sleep
from logging import critical
from threading import Thread

help = '''____Macro Machine___ \n
Made By: Alexander Strole on 10/11/2017
Version: 1.0

________________________________________

TODO:
    Add a GUI
    Add support for traditional macros
    
Please give suggestions as you see fit.

_______________________________________

Command help:
    macro key phrase times activateKey
    
    key = key to press to output the text
    phrase = the phrase you want to output. Spaces need to be replaced with a underscore. 
    times = times to repeat the phrase
    activateKey = key to activate the program. Optional. It is ' by default.

    If you press escape twice it will exit.'''


args = sys.argv

#If the user puts in nothing, display the help
if len(args) < 3:
    print(help)
    sys.exit()

key = args[1]
phrase = args[2] + ' '

#Error checking
if len(key) > 1:
    raise SystemExit, "ERROR: Cannot bind to multiple keys, please only input one letter! " + key

if len(phrase) < 2:
    raise SystemExit, "ERROR: Cannot type nothing! " + phrase

if '_' in phrase:
    phrase = phrase.replace("_", " ")

try:
    times = int(args[3])
except ValueError:
    raise SystemExit, "ERROR: Cannot convert times to a number!"

if len(args) > 4:
    activateKey = args[4]
else:
	activateKey = "'"

activated = False

k = pykeyboard.PyKeyboard()
run = True

#Typing the phrase out
def write():
    global activated
    k.tap_key(k.enter_key)
    for i in range(times):
        for letter in phrase:
            k.tap_key(letter)
            sleep(0.0015)
    activated = False

#Loop for checking if the user presses the activate key and the run key
def loop():
    global activated, key, activateKey, run
    while run:
        if activated:
            wait(key)
            write()
        else:
            wait(activateKey)
            activated = True

def quit():
    global run
    wait('esc')
    wait('esc')
    run = False

#Creating and starting the threads
loop_thread = Thread(target=loop)
quit_thread = Thread(target=quit)
quit_thread.start()
loop_thread.start()

#Checking for exit
while True:
    if run is False:
        loop_thread.join()
        break
    sleep(1)
