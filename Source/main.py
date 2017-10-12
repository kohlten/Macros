import sys, pykeyboard
from keyboard import wait
from time import sleep
from logging import critical

help = '''____Macro Machine___ \n
Made By: Alexander Strole on 10/11/2017
Version: 0.1 ALPHA

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
    activateKey = key to activate the program. Optional. It is ' by default.'''


args = sys.argv

if len(args) < 3:
    print(help)
    run = False
else:
    activateKey = "'"
    run = True

key = args[1]

if len(key) > 1:
    raise SystemExit, "ERROR: Cannot bind to multiple keys, please only input one letter! " + key

phrase = args[2] + ' '
critical(phrase)

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

activated = False

k = pykeyboard.PyKeyboard()
#critical(phrase)

def write():
    global activated
    k.tap_key(k.enter_key)
    for i in range(times):
        for letter in phrase:
            k.tap_key(letter)
            sleep(0.0015)

while run:
    if activated:
        wait(key)
        write()
    else:
        wait(activateKey)
        activated = True

