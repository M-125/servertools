import subprocess
import os
import time
leds=subprocess.run(["ls","/sys/class/leds"],capture_output=True).stdout.decode().split("\n")[:-1]#if problematic u can delete the [:-1]
inputs=[]
#handles leds, loads inputs to input list in case we use all inputs
for e in leds:
    if not e.split("::")[0] in inputs:
        inputs.append(e.split("::")[0])
def led_path(type,input):
    #return path of led
    #type is the light id on the keyboard
    #input tells which inputs light to set
    return f"/sys/class/leds/{input}::{type}/brightness"

def write(path,data):
    #writes the task onto the brightness "file"
    if os.path.exists(path):
        with open(path,"w") as f:
            f.write(str(data))

def led_on(type,input=-1):
    #turn type(eg. capslock) led on input on
    #by default it will try on all inputs
    #input can be a string which is the name of input
    #or an integer to get by index (based on ls' ordering)

    if input==-1:
        for e in inputs:
            path=led_path(type,e)
            print(f"{path} >> on")
            write(path,1)
    else:
        path=led_path(type,input if input is str else inputs[input])
        write(path,1)
        print(f"{path} >> on")
    
def led_off(type,input=-1):
    #turn type(eg. capslock) led on input off
    #see led_on()
    if input<=-1:
        for e in inputs:
            path=led_path(type,e)
            write(path,0)
            print(f"{path} >> off")
    else:
        path=led_path(type,input if input is str else inputs[input])
        write(path,0)
        print(f"{path} >> off")

def blink(type,sec,input=-1):
    #blinks
    #turns led on for sec/2 then turns it off and waits another sec/2
    led_on(type,input)
    time.sleep(sec/2)
    led_off(type,input)
    time.sleep(sec/2)

def all_on():
    #turn all possible leds on
    for e in leds:
        write(f"/sys/class/leds/{e}/brightness",1)
def all_off():
    #turn all possible leds off
    for e in leds:
        write(f"/sys/class/leds/{e}/brightness",0)
