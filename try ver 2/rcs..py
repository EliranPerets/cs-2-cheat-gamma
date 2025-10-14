import time
import os
import pyMeow.pyMeow as pm
import keyboard as kb
import win32api
from random import randint
import numpy as np
from numpy import array
from pyMeow.pyMeow import vec3, world_to_screen
from pyMeow.pyMeow import vec2
from Memory import Memory, OFFSETS
import pynim
import configparser
import math
kfc_weapon = ["temp","Desert Eagle","Dual Berettas",'Five-SeveN','Glock-18','temp','temp','AK-47','AUG','AWP','FAMAS','G3SG1','temp','Galil AR',
              'M249','temp','M4A4','MAC-10',"temp",'P90','Redpulsor Device','temp','temp',"MP5-SD","UMP-45","XM1014","PP-Bizon","MAG-7",
              "Negev","Sawed-Off",'Tec-9','Zeus x27','P2000',"MP7",'MP9','Nova','P250','Ballistic Shield','Scar-20','SG 553','SSG 08',
              'Golden Knife','Knife','Flashbang','HE Grenade','Smoke Grenade','	Molotov','Decoy Grenade','Incendiary Grenade','C4',
              'Kevlar Vest','Kevlar + Helmet','Heavy Assaultsuit','temp','item_nvg','Defuse Kit','Rescue Kit','Medi-Shot',
              'musickit_default','weapon_knife_t','M4A1-S','USP-S','Recipe Trade Up','CZ75-Auto','R8 Revolver','temp','temp','temp',
              'Tactical Awareness Grenade','Bare Hands','Breachcharge','temp','Tablet','temp','weapon_melee','Axe','Hammer','temp',
              'Wrench','temp','Spectral Shiv','Fire Bomb','Diversion Device','Frag Grenade','Snowball','Bump Mine']
handle = Memory()
check = [28, 7, 16, 10, 8, 14, 39, 13, 60]
punchold = (0,0)
punch = (0,0)

def main():
    if not handle.connect():
        while not handle.connect():
            print("Waiting for CS2.")
            time.sleep(0.5)
            print("Waiting for CS2..")
            time.sleep(0.5)
            print("Waiting for CS2...")
            time.sleep(0.5)
        os.system('cls')
        print("Done")
    else:
        os.system('cls')
        print("Done")
    global punchold
    global punch


    while 1:
        temp_proc = pm.get_window_info("Counter-Strike 2")
        if int(handle.get_weapon(handle.get_local_player_pawn())) in check:
            print(handle.get_weapon(handle.get_local_player_pawn()))
            if pm.key_pressed(1):
                if handle.get_shotsfired(handle.get_local_player_pawn()):
                    punchold = punch
                    try:
                        right_anglex = 0
                        punch = handle.get_punch_angle(handle.get_local_player_pawn())
                        # win32api.mouse_event(0x00001, 0, int(((temp_proc[3]*2.25)/89)*2), 0, 0)
                        angley = punchold[0] - punch[0]
                        anglex = punch[1] - punchold[1]
                        if angley >= 0.525:
                            angley = 1
                        if anglex >= 0.75:
                            anglex = 1
                        if angley <= -0.525:
                            angley = -1
                        if anglex <= -0.75:
                            anglex = -1
                        right_angley = int(angley) * int(((temp_proc[3] * 2.25) / 89) * 2)
                        right_anglex = int(anglex) * int(((temp_proc[2] * 1.29) / 90) * 2)
                        if right_anglex > 73:
                            right_anglex = 73
                        if right_angley > 73:
                            right_angley = 73
                    except:
                        continue
                    print(right_anglex)
                    win32api.mouse_event(0x00001, right_anglex, right_angley, 0, 10000)
        else:
            punch = (0, 0)
            punchold = (0, 0)

main()