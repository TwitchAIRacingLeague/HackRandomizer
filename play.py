
#import pygame
from inputs import get_gamepad
import threading
import socket
import struct
import time
import datetime
import json
import os
print ("input finished")
import sys

import retro
from datetime import datetime
import random
import itertools
import gzip

def normalize_data(data):
    for i in range(len(data)):
        data[i] = round(data[i])
    return data

list_of_hacks = ['SuperMetroidAngryFireChozo-Snes', 'SuperMetroidAiryRev3-Snes']#, 'SuperMetroid-Snes']
def save_state_to_file(env, name="start.state"):
    
    content = env.em.get_state()
    with gzip.open(name, 'wb') as f:
        f.write(content)

#def load_state_from_file(env, name):
    
class joystickEventSender(threading.Thread):
    controllers = []
    running = 1
    JoystickData = []
    def __init__(self):
        #pygame.init()
        #pygame.joystick.init()
        #for x in range(pygame.joystick.get_count()):
        #    pygame.joystick.Joystick(x).init()
        #    if(pygame.joystick.Joystick(x).get_numbuttons() == 15):
        #        self.controllers.append(1)
        #    else:
        #        self.controllers.append(0)
        self.JoystickData = [0,0,0,0,0,0,0,0,0,0,0,0]
       	threading.Thread.__init__(self)

    def run(self):
        while True:
            lookup = {"BTN_THUMB" : "B", "BTN_TOP2" : "L", "BTN_BASE" : "SELECT", "BTN_BASE2" : "START",  "BTN_PINKIE" : "R", "ABS_X" : "LR", "ABS_Y" : "UD", "BTN_THUMB2": "X", "BTN_TOP" : "Y", "BTN_TRIGGER" : "A"}
            index = {"B" : 0, "Y" : 1, "START" : 3, "SELECT" : 2, "DOWN" : 5, "UP" : 4, "RIGHT" : 7, "LEFT" : 6, "A" : 8, "X" : 9, "L" : 10, "R" : 11}
                    
            events = get_gamepad()
            for event in events:
                if event.code in lookup:
                    if lookup[event.code] == "LR":
                        if int(event.state) < 128:
                            self.JoystickData[index["LEFT"]] = 1
                            self.JoystickData[index["RIGHT"]] = 0
                        elif int(event.state) > 128:
                            self.JoystickData[index["LEFT"]] = 0
                            self.JoystickData[index["RIGHT"]] = 1
                        else:
                            self.JoystickData[index["LEFT"]] = 0
                            self.JoystickData[index["RIGHT"]] = 0
                    elif lookup[event.code] == "UD":
                        if int(event.state) < 128:
                            self.JoystickData[index["UP"]] = 1
                            self.JoystickData[index["DOWN"]] = 0
                        elif int(event.state) > 128:
                            self.JoystickData[index["UP"]] = 0
                            self.JoystickData[index["DOWN"]] = 1
                        else:
                            self.JoystickData[index["UP"]] = 0
                            self.JoystickData[index["DOWN"]] = 0  
                    else:
                        if lookup[event.code] in index:
                            self.JoystickData[index[lookup[event.code]]] = event.state
                #else:
                #    print(event.ev_type, lookup.get(event.code, event.code), event.state)
        
                
#def switch_env(x):

thread = joystickEventSender()
thread.start()


def action_to_list(buttons):
    binary_value = str(bin(buttons))
    binary_value = ''.join(list(binary_value)[2:])
    action = list(map(int,list(str(binary_value).zfill(12))))
    return action

#pygame.init()

states = {}
idx = 0
env = retro.make(game=list_of_hacks[idx])
env.reset()
obs, rew, done, info = env.step([0,0,0,0,0,0,0,0,0,0,0,0])
print (info)
hp = info['hp']

    
i = 0
while True:
    time.sleep(.01)
    obs, rew, done, info = env.step(thread.JoystickData)
    print (thread.JoystickData)
    if info['hp'] != hp:
        print ("Changing Games", info["hp"], hp)
        save_state_to_file(env, "prior_to_swap.state")
        #if list_of_hacks[idx] not in states:
        print ("Saving the last hack's state")
        states[list_of_hacks[idx]] = env.em.get_state()

        idx = (idx + 1) % len(list_of_hacks)
        env.loadRom(list_of_hacks[idx])

        if list_of_hacks[idx] not in states:
            # If the state of our "new" hack isn't already listed in our state list we then will grab the state
            print ("grabbing our current state since we don't have a prior state.")
            states[list_of_hacks[idx]] = env.em.get_state()

        # Now assign the state to set_state
        env.em.set_state(states[list_of_hacks[idx]])
        obs, rew, done, info = env.step([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
        hp = info['hp']
    #obs, rew, done, info = env.step([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    env.render()
    print (i, info)
    i += 1
