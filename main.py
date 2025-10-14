import glob
import queue
import sqlite3
import sys
import time
import configparser
import keyboard as kb
import pyMeow.pyMeow as pm
import requests
import win32api
import win32con
import win32gui

from Memory import Memory, OFFSETS

list_ent = list(range(1, 65))
print(list_ent)

import os
import threading
from NightMatch import read_db
from ip_update import updated_ip


ip_change = f'https://{updated_ip}'
print(ip_change)

cloud_radar = 1
posbone_get = 0



def clear_queue(q):
    with q.mutex:
        q.queue.clear()

def send_place_worker(coordinates_queue, account_name, ip_change):
    global current_map
    
    server_url = ip_change + "/radar/" + account_name + "/coordinates"
    
    while True:
        try:
            # Get coordinates from the queue with timeout to handle an empty queue
            matrix= coordinates_queue.get(timeout=10)
            try:
                map = current_map
            except:
                map = "de_mirage"
            #print(matrix)
            #print(f"Worker got coordinates from queue: ({x}, {y})")  # Debug print
            for module in matrix:
                if module[3] == 2:
                    module[0]= module[0]
                else:
                    module[0]= module[0]+32
            data_to_send = {
                "matrix": matrix,
                "map": map
            }
                
            requests.post(server_url, json=data_to_send)

        
        except queue.Empty:
            time.sleep(1)  # Wait for 1 second before retrying
            continue
        
        except requests.exceptions.RequestException as e:
            print(f"Error sending coordinates : {e}")
            time.sleep(1)  # Wait for 1 second before retrying
            continue
        
        finally:
            time.sleep(0.25)
            coordinates_queue.task_done()


def read_from_in_memory_database():
    # Create a connection to the in-memory database
    conn = sqlite3.connect(appdata + '\\Imguistudio\\login.db')

    # Create a cursor object to execute SQL queries
    cur = conn.cursor()

    # Execute a SELECT query to retrieve data from the 'users' table
    select_query = 'SELECT * FROM profile;'
    cur.execute(select_query)

    # Fetch all the rows returned by the SELECT query
    rows = cur.fetchall()

    # Display the retrieved data
    for row in rows:
        print(row)

    # Close the connection when done
    conn.close()

def account(name,password):
    global launch_menu
    server_url = ip_change+"/check_login"

    # User inputs (replace these with your actual data)
    data_to_send = {
        "name": name,
        "password": password,
    }

    response = requests.post(server_url, json=data_to_send)
    if response.status_code == 200:
        # Call the function if the login is successful
        print("success: ",response.text)
        launch_menu = 1
    else:
        # Print an error message if the login is not successful
        print("Login failed:", response.text)
    return response.status_code

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Folder created: {folder_path}")
    else:
        print(f"Folder already exists: {folder_path}")

appdata = os.getenv('LOCAlAPPDATA') + '\\Imguistudio'
folder_path = appdata
create_folder_if_not_exists(folder_path)
print(appdata)
print(appdata+'\\currentcfg.ini')

#print(f"Entity({ent.controller_ptr}): health: {handle.get_health(ent)} | team: {handle.get_team(ent)} | pos: {handle.get_position(ent)} | angle: {handle.get_eye_angles(ent)} | name: {handle.get_name(ent)}")
config = configparser.ConfigParser()
config2 = configparser.ConfigParser()

## backup in case of failure to initialize

button_mouse_on_bak = pm.new_color(50,70,50,255)
button_color_bak = pm.new_color(30,30,30,255)
button_color2_bak = pm.new_color(50,50,50,255)
background_color_bak = pm.new_color(20,20,20,255)
background_color2_bak= pm.new_color(50,55,45,240)
color_check_bak = pm.new_color(30, 80, 50, 255)
button_check_bak = pm.new_color(30, 80, 50, 255)
button_inactive_bak = pm.new_color(70, 80, 70, 255)
punch = (0,0)
punchold = (0,0)

print(appdata+'\\currentcfg.ini')
##reading the current config file name from the file


config.read(appdata+'\\currentcfg.ini')

#try to access current config to get the data
try:
    currentcfg2 = config['config_name']
except:
    print(appdata+'\\currentcfg.ini')
    with open(appdata+'\\currentcfg.ini', 'w') as file:
        file.write(f"[config_name]\n")
        file.write("name = config\n")
    time.sleep(1)
    config.read(appdata+'\\currentcfg.ini')
    currentcfg2 = config['config_name']
currentcfg = currentcfg2['name']
config.read([appdata+"\\"+currentcfg+".ini",appdata+'\\currentcfg.ini'])
selectedcfg = currentcfg
print(currentcfg)

#first load - always true
load = 1

#initializing needed variables to start the gui
drawfps = 0
right_anglex = 0
right_angley = 0
rcs_im = 1
teamcheck = 1
three_x = 0
draw_game_boxes = 0
offsetesp = 0
draw_head_skeleton = 1
skeleton_style = 0
#menu variables -> choosing one
trigger_menu = 0
drawesp_menu = 0
radar_menu = 0
settings_menu = 0
future_menu = 0
chosen_menu = None





def rereadcfg():
    config.read(appdata+'\\currentcfg.ini')
    currentcfg2 = config['config_name']

    currentcfg2['name'] = selectedcfg
    config.read([appdata+"\\"+currentcfg+".ini",appdata+'\\currentcfg.ini'])
    load_cfg(currentcfg)


#loading the cfg - and initializing all the variables
def load_cfg(currentcfg):
    print(currentcfg+" executed")

    global espcfg, radarcfg ,colorcfg , colorautocfg ,styles, triggercfg ,menucfg ,aimbotcfg , button_mouse_on,button_color,button_color2,background_color,background_color2,color_check,button_check,button_inactive , boxes_color,healthnum_color,healthline_color,skeleton_color,weapon_color,aimpos_color,line_roundness,boxes_roundness, drawesp,boxes,skeleton,health,health_line,radar,health_radar,name_radar,aimbot,aimbot_debug,change_strenght,change_fov , strenght,aimbot_place,g,trigger,triggerbutton,boxes_c,skeleton_c,healthnum_c,healthline_c,weapon_c

    espcfg = config['esp' + currentcfg]
    radarcfg = config['radar' + currentcfg]
    colorcfg = config['color' + currentcfg]
    colorautocfg = config['colorauto' + currentcfg]
    styles = config['styles' + currentcfg]
    triggercfg = config['trigger' + currentcfg]
    menucfg = config['menu' + currentcfg]
    aimbotcfg = config['aimbot' + currentcfg]
    button_mouse_on = pm.new_color(int(menucfg['button_mouse_onr']), int(menucfg['button_mouse_ong']),
                                   int(menucfg['button_mouse_onb']), int(menucfg['button_mouse_ona']))
    button_color = pm.new_color(int(menucfg['button_colorr']), int(menucfg['button_colorg']),
                                int(menucfg['button_colorb']), int(menucfg['button_colora']))
    button_color2 = pm.new_color(int(menucfg['button_color2r']), int(menucfg['button_color2g']),
                                 int(menucfg['button_color2b']), int(menucfg['button_color2a']))
    background_color = pm.new_color(int(menucfg['background_colorr']), int(menucfg['background_colorg']),
                                    int(menucfg['background_colorb']), int(menucfg['background_colora']))
    background_color2 = pm.new_color(int(menucfg['background_color2r']), int(menucfg['background_color2g']),
                                     int(menucfg['background_color2b']), int(menucfg['background_color2a']))
    color_check = pm.new_color(int(menucfg['color_checkr']), int(menucfg['color_checkg']), int(menucfg['color_checkb']),
                               int(menucfg['color_checka']))
    button_check = pm.new_color(int(menucfg['button_checkr']), int(menucfg['button_checkg']),
                                int(menucfg['button_checkb']), int(menucfg['button_checka']))
    button_inactive = pm.new_color(int(menucfg['button_inactiver']), int(menucfg['button_inactiveg']),
                                   int(menucfg['button_inactiveb']), int(menucfg['button_inactivea']))
    boxes_color = pm.new_color(int(colorcfg['boxes_colorr']), int(colorcfg['boxes_colorg']),
                               int(colorcfg['boxes_colorb']), int(colorcfg['boxes_colora']))
    healthnum_color = pm.new_color(int(colorcfg['healthnum_colorr']), int(colorcfg['healthnum_colorg']),
                                   int(colorcfg['healthnum_colorb']), int(colorcfg['healthnum_colora']))
    healthline_color = pm.new_color(int(colorcfg['healthline_colorr']), int(colorcfg['healthline_colorg']),
                                    int(colorcfg['healthline_colorb']), int(colorcfg['healthline_colora']))
    skeleton_color = pm.new_color(int(colorcfg['skeleton_colorr']), int(colorcfg['skeleton_colorg']),
                                  int(colorcfg['skeleton_colorb']), int(colorcfg['skeleton_colora']))
    weapon_color = pm.new_color(int(colorcfg['weapon_colorr']), int(colorcfg['weapon_colorg']),
                                int(colorcfg['weapon_colorb']), int(colorcfg['weapon_colora']))
    aimpos_color = pm.new_color(int(colorcfg['aimpos_colorr']), int(colorcfg['aimpos_colorg']),
                                int(colorcfg['aimpos_colorb']), int(colorcfg['aimpos_colora']))
    line_roundness = float(styles['line_roundness'])
    boxes_roundness = float(styles['boxes_roundness'])

    drawesp = int(espcfg['drawesp'])
    boxes = int(espcfg['boxes'])
    skeleton = int(espcfg['skeleton'])
    health = int(espcfg['health'])
    health_line = int(espcfg['health_line'])
    radar = int(radarcfg['radar'])
    health_radar = int(radarcfg['health_radar'])
    name_radar = int(radarcfg['name_radar'])
    aimbot = int(aimbotcfg['aimbot'])
    aimbot_debug = int(aimbotcfg['aimbot_debug'])
    change_strenght = int(aimbotcfg['change_strenght'])
    change_fov = int(aimbotcfg['change_fov'])
    strenght = float(aimbotcfg['strenght'])
    aimbot_place = int(aimbotcfg['aimbot_place'])
    g = float(aimbotcfg['g'])

    trigger = int(triggercfg['trigger'])
    triggerbutton = str(triggercfg['triggerbutton'])
    boxes_c = boxes_color
    skeleton_c = skeleton_color
    healthnum_c = healthnum_color
    healthline_c = healthline_color
    weapon_c = weapon_color

#creating a new cfg with default values
def create_cfg(cfg_name):
    with open(appdata+"\\"+cfg_name+'.ini', 'w') as file:
        file.write(f"[esp{cfg_name}]\n")
        file.write("drawesp = 1\n")
        file.write("boxes = 1\n")
        file.write("skeleton = 0\n")
        file.write("health = 0\n")
        file.write("health_line = 1\n")

        file.write(f"[radar{cfg_name}]\n")
        file.write("radar = 0\n")
        file.write("health_radar = 1\n")
        file.write("name_radar = 1\n")

        file.write(f"[color{cfg_name}]\n")
        file.write("boxes_colorr = 255\n")
        file.write("boxes_colorg = 255\n")
        file.write("boxes_colorb = 255\n")
        file.write("boxes_colora = 255\n")
        file.write("healthnum_colorr = 255\n")
        file.write("healthnum_colorg = 255\n")
        file.write("healthnum_colorb = 255\n")
        file.write("healthnum_colora = 255\n")
        file.write("healthline_colorr = 255\n")
        file.write("healthline_colorg = 255\n")
        file.write("healthline_colorb = 255\n")
        file.write("healthline_colora = 255\n")
        file.write("skeleton_colorr = 255\n")
        file.write("skeleton_colorg = 255\n")
        file.write("skeleton_colorb = 255\n")
        file.write("skeleton_colora = 255\n")
        file.write("weapon_colorr = 255\n")
        file.write("weapon_colorg = 255\n")
        file.write("weapon_colorb = 255\n")
        file.write("weapon_colora = 255\n")
        file.write("aimpos_colorr = 255\n")
        file.write("aimpos_colorg = 255\n")
        file.write("aimpos_colorb = 255\n")
        file.write("aimpos_colora = 255\n")
        file.write(f"[colorauto{cfg_name}]\n")

        file.write(f"[styles{cfg_name}]\n")
        file.write("boxes_roundness = 0\n")
        file.write("line_roundness = 0\n")

        file.write(f"[trigger{cfg_name}]\n")
        file.write("trigger = 0\n")
        file.write("triggerbutton = alt\n")

        file.write(f"[aimbot{cfg_name}]\n")
        file.write("aimbot_debug = 0\n")
        file.write("aimbot = 1\n")
        file.write("aimbot_place = 1\n")
        file.write("strenght = 8\n")
        file.write("change_fov = 1\n")
        file.write("change_strenght = 1\n")
        file.write("g = 1\n")

        file.write(f"[menu{cfg_name}]\n")
        file.write("button_mouse_onr = 50\n")
        file.write("button_mouse_ong = 70\n")
        file.write("button_mouse_onb = 50\n")
        file.write("button_mouse_ona = 255\n")
        file.write("button_colorr = 30\n")
        file.write("button_colorg = 30\n")
        file.write("button_colorb = 30\n")
        file.write("button_colora = 255\n")
        file.write("button_color2r = 50\n")
        file.write("button_color2g = 50\n")
        file.write("button_color2b = 50\n")
        file.write("button_color2a = 255\n")
        file.write("background_colorr = 20\n")
        file.write("background_colorg = 20\n")
        file.write("background_colorb = 20\n")
        file.write("background_colora = 255\n")
        file.write("background_color2r = 50\n")
        file.write("background_color2g = 55\n")
        file.write("background_color2b = 45\n")
        file.write("background_color2a = 255\n")
        file.write("color_checkr = 30\n")
        file.write("color_checkg = 80\n")
        file.write("color_checkb = 50\n")
        file.write("color_checka = 255\n")
        file.write("button_checkr = 30\n")
        file.write("button_checkg = 80\n")
        file.write("button_checkb = 50\n")
        file.write("button_checka = 255\n")
        file.write("button_inactiver = 70\n")
        file.write("button_inactiveg = 80\n")
        file.write("button_inactiveb = 70\n")
        file.write("button_inactivea = 255\n")


#trying to load the cfg - if it fails, means no cfg was found with the name provided in last config -> create a new one with default values
try:
    espcfg = config['esp'+currentcfg]
    radarcfg = config['radar'+currentcfg]
    colorcfg = config['color'+currentcfg]
    colorautocfg = config['colorauto'+currentcfg]
    styles = config['styles'+currentcfg]
    triggercfg = config['trigger'+currentcfg]
    menucfg = config['menu'+currentcfg]
    aimbotcfg = config['aimbot'+currentcfg]
    load_cfg(currentcfg)
except:
    create_cfg("config")
    time.sleep(1)
    config.read([appdata+"\\config.ini", appdata+'\\currentcfg.ini'])
    selectedcfg = currentcfg
    load_cfg("config")


def cfg_change(cfg_name):
    with open(appdata+'\\currentcfg.ini', 'w') as file:
        file.write('\n[config_name]\n')
        file.write(f"name = {cfg_name}\n")


def base_menu_chooser(chosen_menu):
    global trigger_menu,drawesp_menu,radar_menu,settings_menu,future_menu
    trigger_menu = 0
    drawesp_menu = 0
    radar_menu = 0
    settings_menu = 0
    future_menu = 0
    if chosen_menu == "trigger_menu":
        trigger_menu = 1
    elif chosen_menu == "drawesp_menu":
        drawesp_menu = 1
    elif chosen_menu == "radar_menu":
        radar_menu = 1
    elif chosen_menu == "settings_menu":
        settings_menu = 1
    elif chosen_menu == "future_menu":
        future_menu = 1

base_menu_chooser("drawesp_menu")


############## initializing variables ####################

#styles for drawing
boxes_style = 0
style_boxes = 1
line_style = 0
style_line = 1

#give some popup at the settings (when conifrming changes in config)
popup = 0

#trigger main variables
trigger_visuals = 1
trigger_event =1

menu_size = 0
# visibility check - work in progress
boxes_visible_check = 0

# radar main variables
radar_health_toggle = 0
radar_name_toggle = 0
radar_name_color = pm.new_color(255,255,255,255)
radar_health_color = pm.new_color(255,255,255,255)
radar_color_auto_name = 0

# radar variables - colors
color_name_c_radar = radar_name_color
radar_color_auto_health = 0
color_health_c_radar = radar_health_color
color_aimpos_toggle = 0

#menu movement variables - initioalizing default valuesq
previus_mouse_pos = 0

goto_menu_x = 0
goto_menu_y = 0
move_menu_x = 0
move_menu_y = 0

# main for wallhack
last_mouse_pos = 0
xtrypos = 0
distanceforboxes = 1750
posbufferhelp = 0
boxes_people = 0

U = ""
startingpointcfg = 0
cfghelp = 1
pagenumcfg =1
bombscale = 0

new_distance = 1750



## colors for the logo with the fps
colorlogo1 = pm.new_color(0,0,255,255)
colorlogo2 = pm.new_color(0,30,255,255)

########################c4#################
draw_c4 = 0


import math

## basic variables - initializing
pos_buffer = 0
menu = 0
teamnum = 0

gui = 0



# gui initializing main variables
color_boxes_toggle = 0
color_numhealth_toggle = 0
color_linehealth_toggle = 0
color_skeleton_toggle = 0
weapon_color_toggle = 0



rcs = 1
version_name = "ALITY v1.93"



## show weapons - default on
show_weapons = 1
weapon_visibility = 1



## rotating function for esp - now not used
def rotate(origin, point, degree):
    amgle1 = degree * math.pi / 180

    ox, oy = origin
    px, py = point

    qx = ox + math.cos(amgle1) * (px - ox) - math.sin(amgle1) * (py - oy)
    qy = oy + math.sin(amgle1) * (px - ox) + math.cos(amgle1) * (py - oy)
    return qx, qy

# needed bones list
kfc_list = [6,5,8,9,45,9,8,5,13,14,41,14,13,5,1,22,23,24,23,22,1,25,26,27]


#games weapons list, temp - is for weapons that are not in the game anymore or not needed
kfc_weapon = ["temp","Desert Eagle","Dual Berettas",'Five-SeveN','Glock-18','temp','temp','AK-47','AUG','AWP','FAMAS','G3SG1','temp','Galil AR',
              'M249','temp','M4A4','MAC-10',"temp",'P90','Redpulsor Device','temp','temp',"MP5-SD","UMP-45","XM1014","PP-Bizon","MAG-7",
              "Negev","Sawed-Off",'Tec-9','Zeus x27','P2000',"MP7",'MP9','Nova','P250','Ballistic Shield','Scar-20','SG 553','SSG 08',
              'Golden Knife','Knife','Flashbang','HE Grenade','Smoke Grenade','	Molotov','Decoy Grenade','Incendiary Grenade','C4',
              'Kevlar Vest','Kevlar + Helmet','Heavy Assaultsuit','temp','item_nvg','Defuse Kit','Rescue Kit','Medi-Shot',
              'musickit_default','weapon_knife_t','M4A1-S','USP-S','Recipe Trade Up','CZ75-Auto','R8 Revolver','temp','temp','temp',
              'Tactical Awareness Grenade','Bare Hands','Breachcharge','temp','Tablet','temp','weapon_melee','Axe','Hammer','temp',
              'Wrench','temp','Spectral Shiv','Fire Bomb','Diversion Device','Frag Grenade','Snowball','Bump Mine']

kfc_sound = ["menusound"]

#all the ranks in game
kfc_rank = ["Unranked","Silver I","Silver II","Silver III","Silver IV","Silver Elite","Silver Elite Master","Gold Nova I","Gold Nova II",
            "Gold Nova III","Gold Nova Master","Master Guardian I","Master Guardian II","Master Guardian Elite","Distinguished Master Guardian",
            "Legendary Eagle","Legendary Eagle Master","Supreme Master First Class","Global Elite"
            ]

# all the colors in the teams there are in game
kfc_teamcolor = ["blue","green","yellow","orange","purple"]


def gui_press():
    global gui
    gui +=1
    pm.toggle_mouse()
    time.sleep(0.2)

def world_to_screen1(pos, vm, temp_proc):
    w_wo = vm[8] * pos[0] + vm[9] * pos[1] + vm[10] * pos[2] + vm[11]
    if w_wo < 80:
        raise Exception("Out of bounds")
    x_wo = vm[0] * pos[0] + vm[1] * pos[1] + vm[2] * pos[2] + vm[3]
    y_wo = vm[4] * pos[0] + vm[5] * pos[1] + vm[6] * pos[2] + vm[7]
    return pm.vec2(
        temp_proc[2] / 2 + temp_proc[2] / 2 * x_wo / w_wo + temp_proc[0],
        temp_proc[3] / 2 - temp_proc[3] / 2 * y_wo / w_wo +temp_proc[1],
    )

# get all bones at one run - efficient way
def get_posglobal():
    global posbone5, posbone8, posbone13, posbone14, posbone9, posbone22, posbone25, posbone41, posbone23, posbone26, posbone1, posbone27, posbone24,posbone45,posaimhelp , posglobal2,posglobal,pos2dglobal1,pos2dglobal2,distancepos , offsetesp,value_offset,offset_xafter,ofssetye,pos2d22b,pos2d25b,pos2d13b,pos2d8b,pos2d5b,pos2d9b,pos2d45b,pos2d14b,pos2d41b,pos2d23b,pos2d26b,pos2d1b,pos2d27b,pos2d24b , distanceforboxes
    if aimbot % 2 ==1:
        list_of_needed_bones = [6, 28, 4]
    else:
        list_of_needed_bones = [6, 28]
    bone_first = handle.get_more_bones(ent, list_of_needed_bones)
    try:
        posaimhelp = bone_first[2]
    except:
        pass
    posglobal = bone_first[0]
    posglobal2 = bone_first[1]
    #print(viewmat)
    pos2dglobal1 = world_to_screen1(posglobal, viewmat, temp_proc)
    if skeleton %2==1:
        if pos2dglobal1:
            if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
                list_bones = handle.get_more_bones(ent, [22,25,13,8,5,26,1,27,9,45,14,41,23,24])
                posbone22 = list_bones[0]
                posbone25 = list_bones[1]
                posbone13 = list_bones[2]
                posbone8 = list_bones[3]
                posbone5 = list_bones[4]
                posbone26 = list_bones[5]
                posbone1 = list_bones[6]
                posbone27 = list_bones[7]
                posbone9 = list_bones[8]
                posbone45 = list_bones[9]
                posbone14 = list_bones[10]
                posbone41 = list_bones[11]
                posbone23 = list_bones[12]
                posbone24 = list_bones[13]
    #return posglobal2,posglobal,pos2dglobal1,pos2dglobal2,distancepos,posbone5, posbone8, posbone13, posbone14, posbone9, posbone22, posbone25, posbone41, posbone23, posbone26, posbone1, posbone27, posbone24,posbone45,offsetesp,value_offset,offset_xafter,ofssetye,pos2d22b,pos2d25b,pos2d13b,pos2d8b,pos2d5b,pos2d9b,pos2d45b,pos2d14b,pos2d41b,pos2d23b,pos2d26b,pos2d1b,pos2d27b,pos2d24b


def on_exit(icon):
    icon.stop()

def toggle_reset_menu():
    global radar_menu,drawesp_menu,trigger_menu,future_menu,settings_menu
    radar_menu = 0
    drawesp_menu = 0
    trigger_menu = 0
    future_menu = 0
    settings_menu = 0

def toggle_reset_temp():
    global button_mouse_on_toggle,button_color_toggle,button_color2_toggle,background_color_toggle,background_color2_toggle,color_check_toggle,button_check_toggle,button_inactive_toggle,radar_health_toggle,radar_name_toggle,color_numhealth_toggle,color_skeleton_toggle,weapon_color_toggle,color_boxes_toggle,color_linehealth_toggle
    button_mouse_on_toggle = 0
    button_color_toggle = 0
    button_color2_toggle = 0
    background_color_toggle = 0
    background_color2_toggle = 0
    color_check_toggle = 0
    button_check_toggle = 0
    button_inactive_toggle = 0
    radar_health_toggle = 0
    radar_name_toggle = 0
    color_numhealth_toggle = 0
    color_skeleton_toggle = 0
    weapon_color_toggle = 0
    color_boxes_toggle = 0
    color_linehealth_toggle = 0  ##############################

def toggle_reset_onlymenu():
    global button_mouse_on_toggle,button_color_toggle,button_color2_toggle,background_color_toggle,background_color2_toggle,color_check_toggle,button_check_toggle,button_inactive_toggle
    button_mouse_on_toggle = 0
    button_color_toggle = 0
    button_color2_toggle = 0
    background_color_toggle = 0
    background_color2_toggle = 0
    color_check_toggle = 0
    button_check_toggle = 0
    button_inactive_toggle = 0


def toggle_reset_only_wh():
    global color_skeleton_toggle,weapon_color_toggle,color_numhealth_toggle,color_boxes_toggle,color_linehealth_toggle
    color_skeleton_toggle = 0
    weapon_color_toggle = 0
    color_numhealth_toggle = 0
    color_boxes_toggle = 0
    color_linehealth_toggle = 0




### initializing the gui - big boy function
def gui_start(temp_proc):
    global tick , trigger_visuals ,popup,skeleton,color_skeleton_toggle,color_numhealth_toggle,weapon_color_toggle,skeleton_color,show_weapons,health,healthnum_color,health_line,healthline_color,line_style,style_line,line_roundness,boxes_roundness,boxes,radar_menu,settings_menu,future_menu,trigger_menu,drawesp_menu,trigger,drawesp,boxes_style,style_boxes,color_boxes_toggle,boxes_color,color_linehealth_toggle,weapon_color,triggerbutton,trigger_event,menu_size,radar,name_radar,health_radar,radar_name_color,radar_health_color,previus_mouse_pos,goto_menu_x,goto_menu_y,move_menu_x,move_menu_y,last_mouse_pos,aimbot_debug , aimbot , strenght , textu1 , ctmod , change_strenght , change_fov , new_distance , g , aimbot_place , color_aimpos_toggle , aimpos_color,radar_health_toggle,radar_name_toggle,button_mouse_on,button_color,button_color2,background_color,background_color2,color_check,button_check,button_inactive,button_mouse_on_bak,button_color_bak,button_color2_bak,background_color_bak,background_color2_bak,color_check_bak,button_check_bak,button_inactive_bak,button_mouse_on_toggle,button_color2_toggle,background_color_toggle,background_color2_toggle,color_check_toggle,button_check_toggle,button_inactive_toggle,button_color_toggle,currentcfg,U,selectedcfg,startingpointcfg,cfghelp,pagenumcfg,tri_left,aimpng,esppng,settingspng,radarpng,triggerpng
    #toggle_reset_temp()
    configs = glob.glob(appdata+"\\"+'*.ini')
    configs = [os.path.basename(path) for path in configs]
    if menu_size == 1:
        h_gui = 0.7
    else:
        h_gui = 1
    x_gui = (temp_proc[2] / 2)*h_gui
    x_place = ((x_gui + temp_proc[0] * 1.5)*h_gui)+(move_menu_x*1.47)
    y_gui = ((temp_proc[2] / 16 ) * 4.5)*h_gui
    y_place = (y_gui + temp_proc[1] * 1.5)+(move_menu_y*1.5)
    text_place = (temp_proc[1]) * h_gui
    if h_gui == 0.7:
        y_place = ((y_place/(h_gui *temp_proc[3]/1440*h_gui*2.05))*1.5)
        x_place = x_place*2.4
        text_place = (temp_proc[3])/8.5
    # --------- esp choose button ----------------
    pm.draw_rectangle(temp_proc[0],temp_proc[1],temp_proc[2],temp_proc[3],pm.new_color(0,0,0,140))
    pm.draw_rectangle_rounded(x_place / 1.5, y_place / 1.5, x_gui / 1.5, y_gui / 1.5, 0.03, 1, background_color2)
    if pm.gui_button((x_place / 1.5), y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5, ""):#esp
        toggle_reset_menu()
        drawesp_menu = 1
    ## ------------------- esp tab the one on the right with the demonstration -------------------
    if drawesp_menu %2 ==1:
        if drawesp%2==1:

            pm.draw_rectangle_rounded((x_place / 1.5)+x_gui/1.45, y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 5, y_gui/1.83,0.07,1,
                              background_color)
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 1.43, y_place / 1.5 + 0.065 * (x_gui / 1.5), x_gui / 5.5, y_gui / 18,0.07,1,
                              background_color2)
            pm.draw_font(3,"esp preview", (x_place / 1.5) + x_gui/1.37, y_place / 1.5 + y_gui / 11.7, 30 * y_gui / 800,
                         2,pm.get_color('white'))
            try:
                pm.draw_texture(ct_mod, (x_place / 1.5)+x_gui/1.36, y_place / 1.5 + 0.15 * (x_gui / 1.5), pm.get_color('white'), 0, x_gui/6500)
                if show_weapons%2==1:
                    pm.draw_texture(textu1, (x_place / 1.5)+x_gui/1.32, y_place / 1.5 + 0.46 * (x_gui / 1.5), weapon_color, 0, x_gui/1700)
            except:
                print(0)
                print(ct_mod)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 1.45, y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 5,
                                      y_gui / 1.83, 0.07, 1,
                                      pm.get_color('white'))
            if boxes%2==1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 1.365, y_place / 1.5 + 0.15 * (x_gui / 1.5),
                                                x_gui / 9,
                                                y_gui / 2.76, boxes_roundness, 1,
                                                boxes_color)
            if health_line%2==1:
                pm.draw_rectangle_rounded(((x_place / 1.5) + x_gui / 1.365+x_gui / 9)*1.0061, y_place / 1.5 + 0.15 * (x_gui / 1.5),
                                                x_gui / 180,
                                                y_gui / 2.76, 0.6, 1,
                                                healthline_color)
            if health %2==1:
                pm.draw_font(2, "100", ((x_place / 1.5) + x_gui / 1.365+x_gui / 9.7), y_place / 1.5 + 0.12 * (x_gui / 1.5), x_gui/53, 1, healthnum_color)
            if skeleton%2==1:
                pm.draw_line((x_place / 1.5) + x_gui / 1.275, y_place / 1.5 + 0.18 * (x_gui / 1.5), (x_place / 1.5) + x_gui / 1.275, y_place / 1.5 + 0.2 * (x_gui / 1), skeleton_color, x_gui/1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.275, y_place / 1.5 + 0.2 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.26, y_place / 1.5 + 0.21 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.26, y_place / 1.5 + 0.21 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.25, y_place / 1.5 + 0.242 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.25, y_place / 1.5 + 0.242 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.24, y_place / 1.5 + 0.29 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)

                pm.draw_line((x_place / 1.5) + x_gui / 1.275, y_place / 1.5 + 0.2 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.29, y_place / 1.5 + 0.21 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.29, y_place / 1.5 + 0.21 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.3, y_place / 1.5 + 0.242 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.3, y_place / 1.5 + 0.242 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.29, y_place / 1.5 + 0.29 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)

                pm.draw_line((x_place / 1.5) + x_gui / 1.275, y_place / 1.5 + 0.142 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.312, y_place / 1.5 + 0.15 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.312, y_place / 1.5 + 0.15 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.322, y_place / 1.5 + 0.172 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.322, y_place / 1.5 + 0.172 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.3265, y_place / 1.5 + 0.2015 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)

                pm.draw_line((x_place / 1.5) + x_gui / 1.275, y_place / 1.5 + 0.142 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.242, y_place / 1.5 + 0.146 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.242, y_place / 1.5 + 0.146 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.225, y_place / 1.5 + 0.165 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)
                pm.draw_line((x_place / 1.5) + x_gui / 1.225, y_place / 1.5 + 0.165 * (x_gui / 1),
                             (x_place / 1.5) + x_gui / 1.227, y_place / 1.5 + 0.2 * (x_gui / 1), skeleton_color,
                             x_gui / 1200)

    pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                      button_inactive)
    if ((x_place / 1.5)) < pm.mouse_position()['x'] < ((x_place / 1.5))+(x_gui / 6.8) and (y_place / 1.5 + 0.15 * (x_gui / 1.5))-(y_gui / 10.5)<pm.mouse_position()['y']<(y_place / 1.5 + 0.15 * (x_gui / 1.5)):

        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,button_mouse_on)
    if drawesp_menu % 2 == 1:
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                          button_color)
        pm.draw_rectangle((x_place / 1.5)+x_gui/7, y_place / 1.5 + 0.05 * (x_gui / 1.5), x_gui / 180, y_gui / 10.5,
                          button_check)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

    if pm.gui_button((x_place / 1.5), y_place / 1.5 + 0.15 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5, ""):#trigger
        toggle_reset_menu()
        trigger_menu = 1
    pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.15 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                      button_inactive)
    if ((x_place / 1.5)) < pm.mouse_position()['x'] < ((x_place / 1.5))+(x_gui / 6.8) and (y_place / 1.5 + 0.15 * (x_gui / 1.5))<pm.mouse_position()['y']<(y_place / 1.5 + 0.15 * (x_gui / 1.5))+(y_gui / 10.5):

        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.15 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,button_mouse_on)
    if trigger_menu % 2 == 1:
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.15 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                          button_color)
        pm.draw_rectangle((x_place / 1.5)+x_gui/7, y_place / 1.5 + 0.15 * (x_gui / 1.5), x_gui / 180, y_gui / 10.5,
                          button_check)

        # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

    if pm.gui_button((x_place / 1.5), y_place / 1.5 + 0.25 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5, ""):#radar
        toggle_reset_menu()
        radar_menu = 1
    pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.25 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                      button_inactive)
    if ((x_place / 1.5)) < pm.mouse_position()['x'] < ((x_place / 1.5)) + (x_gui / 6.8) and (
            y_place / 1.5 + 0.25 * (x_gui / 1.5)) < pm.mouse_position()['y'] < (
            y_place / 1.5 + 0.25 * (x_gui / 1.5)) + (y_gui / 10.5):
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.25 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                          button_mouse_on)
    if radar_menu % 2 == 1:
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.25 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                          button_color)
        pm.draw_rectangle((x_place / 1.5)+x_gui/7, y_place / 1.5 + 0.25 * (x_gui / 1.5), x_gui / 180, y_gui / 10.5,
                          button_check)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

    if pm.gui_button((x_place / 1.5), y_place / 1.5 + 0.35 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5, ""):#future
        toggle_reset_menu()
        future_menu = 1
    pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.35 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                      button_inactive)
    if ((x_place / 1.5)) < pm.mouse_position()['x'] < ((x_place / 1.5)) + (x_gui / 6.8) and (
            y_place / 1.5 + 0.35 * (x_gui / 1.5)) < pm.mouse_position()['y'] < (
            y_place / 1.5 + 0.35 * (x_gui / 1.5)) + (y_gui / 10.5):
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.35 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                          button_mouse_on)
    if future_menu % 2 == 1:
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.35 * (x_gui / 1.5), x_gui / 6.8, y_gui / 10.5,
                          button_color)
        pm.draw_rectangle((x_place / 1.5)+x_gui/7, y_place / 1.5 + 0.35 * (x_gui / 1.5), x_gui / 180, y_gui / 10.5,
                          button_check)

    # ---------------------------------------------------------------------------------------------------------------------------------------------------- #

    if pm.gui_button((x_place / 1.5), y_place / 1.5 + 0.45 * (x_gui / 1.5), x_gui / 6.8, (y_gui / 10.5)*0.75, ""):#settings
        toggle_reset_menu()
        settings_menu = 1
    pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.45 * (x_gui / 1.5), x_gui / 6.8, (y_gui / 10.5) * 0.75,
                      button_inactive)
    if ((x_place / 1.5)) < pm.mouse_position()['x'] < ((x_place / 1.5)) + (x_gui / 6.8) and (
            y_place / 1.5 + 0.45 * (x_gui / 1.5)) < pm.mouse_position()['y'] < (
            y_place / 1.5 + 0.45 * (x_gui / 1.5)) + (y_gui / 10.5)* 0.75:
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.45 * (x_gui / 1.5), x_gui / 6.8, (y_gui / 10.5) * 0.75,
                          button_mouse_on)
    if settings_menu % 2 == 1:
        pm.draw_rectangle((x_place / 1.5), y_place / 1.5 + 0.45 * (x_gui / 1.5), x_gui / 6.8, (y_gui / 10.5) * 0.75,
                          button_color)
        pm.draw_rectangle((x_place / 1.5)+x_gui/7, y_place / 1.5 + 0.45 * (x_gui / 1.5), x_gui / 180, (y_gui / 10.5)*0.75,
                          button_check)
    pm.draw_rectangle((x_place / 1.5)+x_gui/6.8, y_place / 1.5, (x_gui / 2), y_gui / 1.5, background_color)
    pm.draw_texture(aimpng, (x_place / 1.5)+x_gui/100, (y_place / 1.5) + y_gui / 2.285, pm.get_color('white'), 0,
                    x_gui / 10000)
    pm.draw_texture(esppng, (x_place / 1.5) + x_gui / 1000, (y_place / 1.5) + y_gui / 13, pm.get_color('white'), 0,
                    x_gui / 18000)
    pm.draw_texture(settingspng, (x_place / 1.5) + x_gui / 130, (y_place / 1.5) + y_gui / 1.835, pm.get_color('white'), 0,
                    x_gui / 13500)
    pm.draw_texture(radarpng, (x_place / 1.5) + x_gui / 120, (y_place / 1.5) + y_gui / 3.1, pm.get_color('white'),
                    0,
                    x_gui / 4200)
    pm.draw_texture(triggerpng, (x_place / 1.5) + x_gui / 100, (y_place / 1.5) + y_gui / 4.9, pm.get_color('white'),
                    0,
                    x_gui / 12000)

    # draw the fonts above the buttons created prior

    pm.draw_font(3,"ESP",(x_place / 1.5)+x_gui/20,y_place/1.5+y_gui/12,30*y_gui/820,2,pm.get_color('white'))
    pm.draw_font(3,"TRIGGER", (x_place / 1.5)+x_gui/22, y_place/1.5 + y_gui / 4.83, 30 * y_gui / 820, 2,pm.get_color('white'))
    pm.draw_font(3,"RADAR", (x_place / 1.5)+x_gui/22, y_place/1.5 + y_gui / 3.07, 30 * y_gui / 820, 2,pm.get_color('white'))
    pm.draw_font(3,"AIMBOT", (x_place / 1.5) +x_gui/22, y_place/1.5 + y_gui / 2.265, 30 * y_gui / 820, 2,pm.get_color('white'))
    pm.draw_font(3,"SETTINGS", (x_place / 1.5) +x_gui/22, y_place/1.5 + y_gui / 1.81, 30 * y_gui / 880, 2,pm.get_color('white'))

    # ----------------- esp menu -----------------
    if drawesp_menu % 2 == 1:
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, (x_gui / 2.55), y_gui /16,""):
            drawesp+=1
        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 13.5, (x_gui / 2.55), y_gui / 16,
                          button_color)
        pm.draw_font(3,"ESP", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 2.25), (y_place / 1.5) + y_gui / 11.5,
                     30 * y_gui / 800,
                     2,pm.get_color('white'))
        if drawesp%2==1:
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, (x_gui / 2.55), y_gui /16,0.3,1,
                              color_check)
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24, y_gui / 24, ""):
                boxes += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"BOXES", (x_place / 1.5) + x_gui / 5.35 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 4.8,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24, y_gui / 24, ""):
                health_line += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"H-LINE", (x_place / 1.5) + x_gui / 5.35  + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 3.6,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.94, y_gui / 24, y_gui / 24, ""):
                health += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.94, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.94, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"H-NUM", (x_place / 1.5) + x_gui / 5.35  + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.86,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.44, y_gui / 24, y_gui / 24, ""):
                show_weapons += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.44, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.44, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"WEAPONS", (x_place / 1.5) + x_gui / 5.35  + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.37,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.09, y_gui / 24, y_gui / 24, ""):
                skeleton += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.09, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.09, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"SKELETON", (x_place / 1.5) + x_gui / 5.35  + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.035,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            ###boxes_in_menu
            if boxes%2 == 1:
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 5.55, pm.get_color('white'), 10, x_gui/2650)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.95, (y_place / 1.5) + y_gui / 5, y_gui / 4.5, y_gui / 24, ""):
                    boxes_style += 1
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 5, y_gui / 4, y_gui / 24,0.3,1,
                                        button_color2)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.035, (y_place / 1.5) + y_gui / 4.9, y_gui / 30, y_gui / 30,
                                 ""):
                    if color_boxes_toggle % 2 == 0:
                        toggle_reset_temp()
                    color_boxes_toggle +=1
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.05, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                  y_gui / 24,0.3,1,
                                  boxes_color)
                if color_boxes_toggle%2:
                    boxes_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 1.93, (y_place / 1.5) + y_gui / 5, y_gui / 6, y_gui / 2.5,1)
                if boxes_style%2 == 1 and health_line%2 == 1:
                    line_style= 0
                    if pm.gui_button((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 4, y_gui / 4, y_gui / 24,
                                     ""):
                        style_boxes = 1
                        boxes_roundness = 0.2
                        boxes_style = 0
                    pm.draw_rectangle((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 4, y_gui / 4, y_gui / 24,button_color2)
                    if pm.gui_button((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.4, y_gui / 4, y_gui / 24,
                                     ""):
                        style_boxes = 0
                        boxes_roundness = 0
                        boxes_style = 0
                    pm.draw_rectangle((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.4, y_gui / 4, y_gui / 24,
                                      button_color2)
                    pm.draw_font(3,"cutted", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                 (y_place / 1.5) + y_gui / 3.3, 30 * y_gui / 1000,
                                 2,pm.get_color('white'))
                    pm.draw_font(3,"rounded", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                 (y_place / 1.5) + y_gui / 3.9, 30 * y_gui / 1000,
                                 2,pm.get_color('white'))
                    if style_boxes% 2 == 1:
                        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 4, y_gui / 4, y_gui / 24,
                                          color_check)
                    else:
                        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.4, y_gui / 4, y_gui / 24,
                                          color_check)
                if style_boxes% 2 == 1 and boxes_roundness!=0:
                    pm.draw_font(3,"rounded", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                 (y_place / 1.5) + y_gui / 4.8, 30 * y_gui / 1000,
                                 2,pm.get_color('white'))
                else:
                    pm.draw_font(3,"cutted", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                 (y_place / 1.5) + y_gui / 4.8, 30 * y_gui / 1000,
                                 2,pm.get_color('white'))
            #healthline in menu
            if health_line%2 == 1:
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 4.0, pm.get_color('white'), 10, x_gui/2650)
                if boxes_style %2 ==0:

                    if pm.gui_button((x_place / 1.5) + x_gui / 2.95, (y_place / 1.5) + y_gui / 3.7, y_gui / 4.5, y_gui / 24,
                                     ""):
                        line_style += 1
                    pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.71, y_gui / 4, y_gui / 24,0.3,1,
                                            button_color2)
                    if style_line % 2 == 1 and line_roundness!=0:
                        pm.draw_font(3,"rounded", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                     (y_place / 1.5) + y_gui / 3.6, 30 * y_gui / 1000,
                                     2,pm.get_color('white'))
                    else:
                        pm.draw_font(3,"cutted", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                     (y_place / 1.5) + y_gui / 3.6, 30 * y_gui / 1000,
                                     2,pm.get_color('white'))
                if pm.gui_button((x_place / 1.5) + x_gui / 2.035, (y_place / 1.5) + y_gui / 3.6, y_gui / 30, y_gui / 30,
                                 ""):
                    if color_linehealth_toggle % 2 == 0:
                        toggle_reset_temp()
                    color_linehealth_toggle +=1
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.05, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                  y_gui / 24,0.3,1,
                                  healthline_color)
                if color_linehealth_toggle%2 == 1:
                    healthline_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 1.93, (y_place / 1.5) + y_gui / 5, y_gui / 6, y_gui / 2.5,1)
                if line_style%2 == 1:
                    boxes_style = 0
                    if pm.gui_button((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.1, y_gui / 4, y_gui / 24,
                                     ""):
                        style_line = 1
                        line_style = 0
                        line_roundness = 1
                    pm.draw_rectangle((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.1, y_gui / 4, y_gui / 24,
                                      button_color2)
                    if pm.gui_button((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 2.7, y_gui / 4, y_gui / 24,
                                     ""):
                        style_line = 0
                        line_style = 0
                        line_roundness = 0
                    pm.draw_rectangle((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 2.7, y_gui / 4, y_gui / 24,
                                      button_color2)
                    pm.draw_font(3,"cutted", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                 (y_place / 1.5) + y_gui / 2.7, 30 * y_gui / 1000,
                                 2,pm.get_color('white'))
                    pm.draw_font(3,"rounded", (x_place / 1.5) + x_gui / 3.1 + ((x_gui / 2.55) / 8),
                                 (y_place / 1.5) + y_gui / 3.1, 30 * y_gui / 1000,
                                 2,pm.get_color('white'))
                    if style_line% 2 == 1:
                        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 3.1, y_gui / 4, y_gui / 24,
                                          color_check)
                    else:
                        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 3, (y_place / 1.5) + y_gui / 2.7, y_gui / 4, y_gui / 24,
                                          color_check)
            if health%2 == 1:
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 3.12, pm.get_color('white'), 10, x_gui/2650)

                if pm.gui_button((x_place / 1.5) + x_gui / 2.042, (y_place / 1.5) + y_gui / 2.9, y_gui / 26, y_gui / 30,
                                 ""):
                    if color_numhealth_toggle % 2 == 0:
                        toggle_reset_temp()
                    color_numhealth_toggle += 1
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.05, (y_place / 1.5) + y_gui / 2.94, y_gui / 24,
                                  y_gui / 24,0.3,1,
                                  healthnum_color)
                if color_numhealth_toggle % 2 == 1:
                    healthnum_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 1.93, (y_place / 1.5) + y_gui / 5,
                                                          y_gui / 6, y_gui / 2.5, 1)
            if show_weapons%2 == 1:
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 2.57,
                                pm.get_color('white'), 10, x_gui / 2650)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.042, (y_place / 1.5) + y_gui / 2.41, y_gui / 26, y_gui / 30,
                                 ""):
                    if weapon_color_toggle % 2 == 0:
                        toggle_reset_temp()
                    weapon_color_toggle += 1
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.05, (y_place / 1.5) + y_gui / 2.44, y_gui / 24,y_gui / 24,0.3,1,weapon_color)
                if weapon_color_toggle % 2 == 1:
                    weapon_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 1.93, (y_place / 1.5) + y_gui / 5,
                                                          y_gui / 6, y_gui / 2.5, 1)
            if skeleton%2 == 1:
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 2.185,
                                pm.get_color('white'), 10, x_gui / 2650)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.04, (y_place / 1.5) + y_gui / 2.067, y_gui / 26, y_gui / 30,
                                 ""):
                    if color_skeleton_toggle % 2 == 0:
                        toggle_reset_temp()
                    color_skeleton_toggle +=1
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.05, (y_place / 1.5) + y_gui / 2.09, y_gui / 24,y_gui / 24,0.3,1,skeleton_color)
                if color_skeleton_toggle % 2 == 1:
                    skeleton_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 1.93, (y_place / 1.5) + y_gui / 5,
                                                          y_gui / 6, y_gui / 2.5, 1)

            pm.draw_font(3,"DISTANCEE", (x_place / 1.5) + x_gui / 6.5 + ((x_gui / 2.55) / 8),
                             (y_place / 1.5) + y_gui / 1.78,
                             30 * y_gui / 1000,
                             2,pm.get_color('white'))
            new_distance = pm.gui_slider((x_place / 1.5) + x_gui / 3.05, (y_place / 1.5) + y_gui / 1.8, y_gui / 3.2,
                                     y_gui / 24, "", "", new_distance, 200, 10000)
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 3.09, (y_place / 1.5) + y_gui / 1.8, y_gui / 3,
                              y_gui / 24,0.3,1,
                              background_color2)
            pm.draw_rectangle_rounded(((((x_place / 1.5) + x_gui / 3.09) + (y_gui / 3) * new_distance / 10000)) - y_gui / 48,
                              (y_place / 1.5) + y_gui / 1.8, y_gui / 48,
                              y_gui / 24,0.3,1,
                              button_color2)
    else:
        toggle_reset_only_wh()
    ## ------------------- aimbot tab -------------------
    if future_menu %2 ==1:
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, (x_gui / 2.55), y_gui /16,""):
            aimbot+=1
        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 13.5, (x_gui / 2.55), y_gui / 16,
                          button_color)
        pm.draw_font(3,"AIMBOT", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 2.25), (y_place / 1.5) + y_gui / 11.5,
                     30 * y_gui / 800,
                     2,pm.get_color('white'))
        if aimbot%2==1:
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, (x_gui / 2.55), y_gui /16,0.3,1,
                              color_check)
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24, y_gui / 24, ""):
                aimbot_debug += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"DEBUG", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 4.8,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if aimbot_debug%2 == 1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 5.55, pm.get_color('white'), 10, x_gui/2650)
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24, y_gui / 24, ""):
                change_strenght += 1

            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"Change strenght", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 3.6,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if change_strenght%2 == 1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 4.0, pm.get_color('white'), 10, x_gui/2650)
                strenght = pm.gui_slider((x_place / 1.5) + x_gui / 2.35, (y_place / 1.5) + y_gui / 3.68, y_gui / 3.2,
                                        y_gui / 26,"","",strenght,1,20)
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 3.7, y_gui / 3,
                                        y_gui / 24,0.3,1,
                                        background_color2)
                pm.draw_rectangle(((((x_place / 1.5) + x_gui / 2.4)+(y_gui / 3)*strenght/20))- y_gui / 48, (y_place / 1.5) + y_gui / 3.7, y_gui / 48,
                                  y_gui / 24,
                                  button_color2)
            else:
                strenght = 5


            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.9, y_gui / 24, y_gui / 24, ""):
                change_fov += 1

            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.9, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.9, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"Change fov", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.85,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if change_fov%2 == 1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.9, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 3.08, pm.get_color('white'), 10, x_gui/2650)
                g = pm.gui_slider((x_place / 1.5) + x_gui / 2.35, (y_place / 1.5) + y_gui / 2.87,y_gui / 3.2,
                                        y_gui / 26,"","",g,0.2,2)
                pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui /2.9, y_gui / 3,
                                        y_gui / 24,0.3,1,
                                        background_color2)
                pm.draw_rectangle(((((x_place / 1.5) + x_gui / 2.4)+(y_gui / 3)*g/2))- y_gui / 48, (y_place / 1.5) + y_gui / 2.9, y_gui / 48,
                                  y_gui / 24,
                                  button_color2)
            else:
                g = 1
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.4, y_gui / 24, y_gui / 24, ""):
                aimbot_place += 1

            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.4, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.4, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"show target", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.35,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if aimbot_place%2 == 1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.4, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 2.52,
                                pm.get_color('white'), 10, x_gui / 2650)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.65, (y_place / 1.5) + y_gui / 2.4, y_gui / 24, y_gui / 24,
                                 ""):
                    if color_aimpos_toggle % 2 == 0:
                        toggle_reset_temp()
                    color_aimpos_toggle += 1
                pm.draw_rectangle((x_place / 1.5) + x_gui / 2.65, (y_place / 1.5) + y_gui / 2.4, y_gui / 24,
                                  y_gui / 24,
                                  aimpos_color)
                if color_aimpos_toggle % 2 == 1:
                    aimpos_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 1.93, (y_place / 1.5) + y_gui / 5,
                                                          y_gui / 6, y_gui / 2.5, 1)

    ## ------------------- settings  tab -------------------
    if settings_menu%2 == 1:
        #print(currentcfg)





        pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5)+y_gui/15.4, y_gui / 2.5, y_gui / 1.88, 0, 1, background_color2)
        pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 15.4, y_gui / 2.5,
                                      y_gui / 1.88, 0, 1, pm.get_color('white'))


        if pm.gui_button((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6.5, y_gui / 24, ""):
            currentcfg = selectedcfg
            cfg_change(selectedcfg)
            rereadcfg()
        pm.draw_rectangle((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6.5,
                              y_gui / 24,
                              button_color2)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6.5,
                                    y_gui / 24,
                                    pm.get_color('white'))
        pm.draw_font(3,"load cfg", (x_place / 1.5) + x_gui / 2.73 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 1.77,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
        cfgnamebox = pm.gui_text_box((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 1.95, y_gui / 2.5,
                                         y_gui / 24, U, 5)
        pm.draw_rectangle((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 1.95, y_gui / 2.5,
                              y_gui / 24,
                              button_color)
        if len(cfgnamebox) < 21:
                U = cfgnamebox
        elif len(cfgnamebox) > 20:
                U = cfgnamebox[:20-len(cfgnamebox)]
                print(U)
                cfgnamebox = U

        pm.draw_font(3,U, (x_place / 1.5) + x_gui / 2.73 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 1.93,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))



        if pm.gui_button((x_place / 1.5) + x_gui / 2.06, (y_place / 1.5) + y_gui / 1.8, y_gui / 6.5, y_gui / 24, ""):
            if U != "":
                    print('lox')
                    create_cfg(U)
            else:
                    print('empty')
        pm.draw_rectangle((x_place / 1.5) + x_gui / 2.06, (y_place / 1.5) + y_gui / 1.8, y_gui / 6.5,
                              y_gui / 24,
                              button_color2)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 2.06, (y_place / 1.5) + y_gui / 1.8, y_gui / 6.5,
                                    y_gui / 24,
                                    pm.get_color('white'))
        pm.draw_font(3,"create cfg", (x_place / 1.5) + x_gui / 2.25 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 1.77,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
        for cfg in configs:
            if cfg != "currentcfg.ini":
                visible_cfg_list = configs[startingpointcfg:8 + startingpointcfg]
                if configs.index(cfg) > configs.index("currentcfg.ini"):
                    indexinlistcfg = configs.index(cfg) - 1
                else:
                    indexinlistcfg = configs.index(cfg)
                if pagenumcfg - 1 != 0:
                    startingpointcfg = (pagenumcfg - 1) * 7 + 1
                    indexinlistcfg = configs.index(cfg) - 1
                else:
                    startingpointcfg = (pagenumcfg - 1) * 7
                if pagenumcfg - 1 != 0:
                    indexinlistcfg = indexinlistcfg - startingpointcfg + 1
                if not "currentcfg.ini" in visible_cfg_list:
                    if len(visible_cfg_list) > 7:
                        visible_cfg_list.pop()
                if cfg in visible_cfg_list:
                    if cfg != "currentcfg.ini":
                        if pm.gui_button((x_place / 1.5) + x_gui / 2.48,
                                         (y_place / 1.5) + y_gui / 12 + (y_gui / 18) * indexinlistcfg, y_gui / 2.57,
                                         y_gui / 24, ""):
                            selectedcfg = cfg[:-4]
                            print(selectedcfg)
                    if cfg[:-4] == selectedcfg:
                        pm.draw_rectangle((x_place / 1.5) + x_gui / 2.48,
                                          (y_place / 1.5) + y_gui / 12 + (y_gui / 18) * indexinlistcfg, y_gui / 2.57,
                                          y_gui / 24,
                                          button_mouse_on)
                    else:
                        pm.draw_rectangle((x_place / 1.5) + x_gui / 2.48,
                                          (y_place / 1.5) + y_gui / 12 + (y_gui / 18) * indexinlistcfg, y_gui / 2.57,
                                          y_gui / 24,
                                          button_inactive)
                    if (x_place / 1.5) + x_gui / 2.48 < pm.mouse_position()['x'] < ((x_place / 1.5) + x_gui / 2.48) + (
                            y_gui / 2.57) and ((y_place / 1.5) + y_gui / 12 + (y_gui / 18) * indexinlistcfg) < \
                            pm.mouse_position()['y'] < (
                            (y_place / 1.5) + y_gui / 12 + (y_gui / 18) * indexinlistcfg) + y_gui / 24:
                        pm.draw_rectangle((x_place / 1.5) + x_gui / 2.48,
                                          (y_place / 1.5) + y_gui / 12 + (y_gui / 18) * indexinlistcfg, y_gui / 2.57,
                                          y_gui / 24, button_mouse_on)
                    pm.draw_font(3, cfg[:-4], (x_place / 1.5) + x_gui / 2.4,
                                 (y_place / 1.5) + y_gui / 11.3 + (y_gui / 18) * indexinlistcfg, 30 * y_gui / 1000,
                                 2, pm.get_color('white'))

            if len(configs)-1>7:
                cfghelp = (len(configs) - 1)//7
                cfghelp2 = (len(configs) - 1)%7
                if cfghelp2 != 0:
                    cfghelp+=1
            else:
                cfghelp = 1
            if pm.gui_button((x_place / 1.5) + x_gui / 1.7, (y_place / 1.5) + y_gui / 2.117, y_gui / 24, y_gui / 36,
                                 ""):
                if pagenumcfg != cfghelp:
                        pagenumcfg +=1


            pm.draw_rectangle((x_place / 1.5) + x_gui / 1.7, (y_place / 1.5) + y_gui / 2.117, y_gui / 24, y_gui / 36,
                              button_inactive)

            if (x_place / 1.5) + x_gui / 1.7 < pm.mouse_position()['x'] < (x_place / 1.5) + x_gui / 1.7+ y_gui / 24 and (y_place / 1.5) + y_gui / 2.117<pm.mouse_position()['y'] < (y_place / 1.5) + y_gui / 2.117 +y_gui / 36:
                pm.draw_rectangle((x_place / 1.5) + x_gui / 1.7, (y_place / 1.5) + y_gui / 2.117, y_gui / 24, y_gui / 36, button_mouse_on)
            pm.draw_texture(tri_right, (x_place / 1.5) + x_gui / 1.7+y_gui / 96, (y_place / 1.5) + y_gui / 2.117+y_gui / 288, pm.get_color('white'), 0, y_gui / 5000)

            if pm.gui_button((x_place / 1.5) + x_gui / 1.9, (y_place / 1.5) + y_gui / 2.117, y_gui / 24, y_gui / 36,
                                 ""):
                if pagenumcfg !=1:
                        pagenumcfg -=1
            pm.draw_rectangle((x_place / 1.5) + x_gui / 1.9, (y_place / 1.5) + y_gui / 2.117, y_gui / 24, y_gui / 36,
                              button_inactive)

            if (x_place / 1.5) + x_gui / 1.9 < pm.mouse_position()['x'] < (x_place / 1.5) + x_gui / 1.9+ y_gui / 24 and (y_place / 1.5) + y_gui / 2.117<pm.mouse_position()['y'] < (y_place / 1.5) + y_gui / 2.117 +y_gui / 36:
                pm.draw_rectangle((x_place / 1.5) + x_gui / 1.9, (y_place / 1.5) + y_gui / 2.117, y_gui / 24, y_gui / 36, button_mouse_on)
            pm.draw_texture(tri_left, (x_place / 1.5) + x_gui / 1.9 + y_gui / 96,
                            (y_place / 1.5) + y_gui / 2.117 + y_gui / 288, pm.get_color('white'), 0, y_gui / 5000)
            pm.draw_font(3,str(pagenumcfg)+"/"+str(cfghelp), (x_place / 1.5) + x_gui / 1.955 + ((x_gui / 2.55) / 8),
                         (y_place / 1.5) + y_gui / 2.1,
                         30 * y_gui / 1300,
                         2,pm.get_color('white'))



            if pm.gui_button((x_place / 1.5) + x_gui / 1.745, (y_place / 1.5) + y_gui / 1.8, y_gui / 10.7, y_gui / 24,
                             ""):
                os.remove(appdata+"\\"+selectedcfg+".ini")
                rereadcfg()
            pm.draw_rectangle((x_place / 1.5) + x_gui / 1.745, (y_place / 1.5) + y_gui / 1.8, y_gui / 10.7,
                              y_gui / 24,
                              button_color2)
            pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 1.745, (y_place / 1.5) + y_gui / 1.8, y_gui / 10.7,
                                    y_gui / 24,
                                    pm.get_color('white'))
            pm.draw_font(3, "del", (x_place / 1.5) + x_gui / 1.85 + ((x_gui / 2.55) / 8),
                         (y_place / 1.5) + y_gui / 1.77,
                         30 * y_gui / 1000,
                         2, pm.get_color('white'))

        #if (x_place / 1.5) + x_gui / 2.5< pm.mouse_position()['x'] < ((x_place / 1.5) + x_gui / 2.5) + y_gui / 2.5 and ((y_place / 1.5) + y_gui / 15.4)< pm.mouse_position()['y'] <((y_place / 1.5) + y_gui / 15.4+y_gui / 1.88):


        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6, y_gui / 24, ""):
            save_cfg(currentcfg)
            rereadcfg()
            popup += 1

        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6,y_gui / 24,button_color2)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6,
                                y_gui / 24,
                                pm.get_color('white'))
        pm.draw_font(3,"save cfg", (x_place / 1.5) + x_gui / 3.95 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 1.77,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24, y_gui / 24,
                         ""):
            if background_color_toggle % 2 == 0:
                toggle_reset_temp()
            background_color_toggle +=1

        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                          y_gui / 24,
                          background_color)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if background_color_toggle % 2 == 1:
            background_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.2, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24, y_gui / 24,
                         ""):
            if background_color2_toggle % 2 == 0:
                toggle_reset_temp()
            background_color2_toggle += 1

        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                          y_gui / 24,
                          background_color2)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if background_color2_toggle % 2 == 1:
            background_color2 = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui /3, y_gui / 24, y_gui / 24,
                         ""):
            if button_inactive_toggle % 2 == 0:
                toggle_reset_temp()
            button_inactive_toggle += 1

        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3, y_gui / 24,
                          y_gui / 24,
                          button_inactive)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if button_inactive_toggle % 2 == 1:
            button_inactive = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.5, y_gui / 24, y_gui / 24,
                         ""):
            if button_check_toggle % 2 == 0:
                toggle_reset_temp()
            button_check_toggle += 1

        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.5, y_gui / 24,
                          y_gui / 24,
                          button_check)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.5, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if button_check_toggle % 2 == 1:
            button_check = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.15, y_gui / 24, y_gui / 24,
                         ""):
            if button_mouse_on_toggle % 2 == 0:
                toggle_reset_temp()
            button_mouse_on_toggle += 1
        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.15, y_gui / 24,
                          y_gui / 24,
                          button_mouse_on)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 2.15, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if button_mouse_on_toggle % 2 == 1:
            button_mouse_on = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 7.5, y_gui / 24, y_gui / 24,
                         ""):
            if button_color2_toggle % 2 == 0:
                toggle_reset_temp()
            button_color2_toggle += 1
        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 7.5, y_gui / 24,
                          y_gui / 24,
                          button_color2)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 7.5, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if button_color2_toggle % 2 == 1:
            button_color2 = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 14, y_gui / 24, y_gui / 24,
                         ""):
            if color_check_toggle % 2 == 0:
                toggle_reset_temp()
            color_check_toggle += 1
        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 14, y_gui / 24,
                          y_gui / 24,
                          color_check)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 14, y_gui / 24,
                          y_gui / 24,
                          pm.get_color('white'))
        if color_check_toggle % 2 == 1:
            color_check = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.4, (y_place / 1.5) + y_gui / 14,
                                                     y_gui / 3, y_gui / 2.2, 1)


        pm.draw_font(3,"BACKGROUND-1", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 4.8,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"CHECK-MENU", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.44,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"BACKGROUND-2", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 3.6,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"SUB-MENU", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.9,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"MOUSE-ON", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 2.1,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"CHECK", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 13.5,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"BUTTON_C", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 7,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
    else:
        toggle_reset_onlymenu()

    if popup%2 == 1:
        settings_menu = 0
        pm.draw_rectangle_rounded(x_place / 1.5, y_place / 1.5, x_gui / 1.5, y_gui / 1.5,0.02,1,pm.new_color(30, 70, 50, 120))
        if pm.gui_button((x_place / 1.5) + x_gui / 3.5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6, y_gui / 24, ""):
            popup = 0
        pm.draw_rectangle((x_place / 1.5) + x_gui / 3.5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6,
                          y_gui / 24,
                          button_color2)
        pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 3.5, (y_place / 1.5) + y_gui / 1.8, y_gui / 6,
                                y_gui / 24,
                                pm.get_color('white'))
        pm.draw_font(3,"config saved", (x_place / 1.5) + x_gui / 2.7 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 1.77,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))
        pm.draw_font(3,"ok", (x_place / 1.5) + x_gui / 3.6 + ((x_gui / 2.55) / 8),
                     (y_place / 1.5) + y_gui / 1.77,
                     30 * y_gui / 1000,
                     2,pm.get_color('white'))

    ## ------------------- trigger  tab -------------------
    if trigger_menu%2== 1:
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, y_gui /3.5, y_gui /16,""):
            trigger+=1

        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 13.5, y_gui / 3.5, y_gui / 16,
                          button_color)
        pm.draw_font(3,"TRIGGER", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 10.5), (y_place / 1.5) + y_gui / 11.5,
                     30 * y_gui / 800,
                     2,pm.get_color('white'))
        if trigger%2==1:
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, y_gui / 3.5, y_gui /16,0.3,1,
                              color_check)
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24, y_gui / 24, ""):
                trigger_visuals += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"DEBUG", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 4.8,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if trigger_visuals%2==1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 5.55, pm.get_color('white'), 10, x_gui/2650)
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 4, y_gui / 20, ""):
                triggerbutton = change_trigger_key(trigger_event)
            pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 4, y_gui / 20,
                              button_color2)
            pm.draw_rectangle_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 4, y_gui / 20,
                                    pm.get_color('white'))
            pm.draw_font(3,triggerbutton, (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 5.7), (y_place / 1.5) + y_gui / 3.5,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))

    ## ------------------- radar  tab -------------------
    if radar_menu%2==1:
        
        if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, (x_gui / 2.55), y_gui /16,""):
            radar+=1
        pm.draw_rectangle((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 13.5, (x_gui / 2.55), y_gui / 16,
                          button_color)
        pm.draw_font(3,"RADAR", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 2.25), (y_place / 1.5) + y_gui / 11.5,
                     30 * y_gui / 800,
                     2,pm.get_color('white'))
        if radar%2==1:
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5)+y_gui/13.5, (x_gui / 2.55), y_gui /16,0.3,1,
                              color_check)
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24, y_gui / 24, ""):
                health_radar += 1
            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"HEALTH", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 4.8,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if pm.gui_button((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24, y_gui / 24, ""):
                name_radar += 1

            pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    button_color2)
            pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
            pm.draw_font(3,"NAMES", (x_place / 1.5) + x_gui / 5 + ((x_gui / 2.55) / 8), (y_place / 1.5) + y_gui / 3.6,
                         30 * y_gui / 1000,
                         2,pm.get_color('white'))
            if health_radar%2 == 1:
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 5.55, pm.get_color('white'), 10, x_gui/2650)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.8, (y_place / 1.5) + y_gui / 5, y_gui / 24, y_gui / 24,
                                 ""):
                    if radar_health_toggle % 2 == 0:
                        toggle_reset_temp()
                    radar_health_toggle += 1

                pm.draw_rectangle((x_place / 1.5) +  x_gui / 2.8, (y_place / 1.5) + y_gui / 5, y_gui / 24,
                                  y_gui / 24,
                                  radar_health_color)
                if radar_health_toggle%2==1:
                    radar_health_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 5, y_gui / 3, y_gui / 2.5,1)

            if name_radar % 2 == 1:
                #print(color_numhealth_toggle,color_skeleton_toggle,weapon_color_toggle,color_boxes_toggle,radar_health_toggle,radar_name_toggle,color_linehealth_toggle)
                pm.draw_rectangle_rounded_lines((x_place / 1.5) + x_gui / 5, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                    y_gui / 24,0.3,1,
                                    pm.get_color('white'))
                pm.draw_texture(tick, (x_place / 1.5) + x_gui / 5.2, (y_place / 1.5) + y_gui / 4.0, pm.get_color('white'), 10, x_gui/2650)
                if pm.gui_button((x_place / 1.5) + x_gui / 2.8, (y_place / 1.5) + y_gui / 3.7, y_gui / 24, y_gui / 24,
                                 ""):
                    if radar_name_toggle % 2 == 0:
                        toggle_reset_temp()
                    radar_name_toggle += 1

                pm.draw_rectangle((x_place / 1.5) +  x_gui / 2.8, (y_place / 1.5) + y_gui / 3.7, y_gui / 24,
                                  y_gui / 24,
                                  radar_name_color)
                if radar_name_toggle%2==1:
                    radar_name_color = pm.gui_color_picker((x_place / 1.5) + x_gui / 2.5, (y_place / 1.5) + y_gui / 5, y_gui / 3, y_gui / 2.5,1)


    # ------------------ menu movement realization - works good (windowed fullscreen / windowed mode)---------------------
    pm.draw_rectangle(((x_place / 1.5)),(y_place / 1.5 - 0.05 * (x_gui / 1.5)),(x_gui)/1.5,(y_gui / 10),pm.new_color(0,0,0,0))
    if ((x_place / 1.5)) < pm.mouse_position()['x'] < ((x_place / 1.5))+(x_gui / 1.5) and (y_place / 1.5 - 0.05 * (x_gui / 1.5))<pm.mouse_position()['y']<(y_place / 1.5 - 0.05 * (x_gui / 1.5))+(y_gui / 8):
        if pm.key_pressed(1):
            if previus_mouse_pos != 0:
                goto_menu_x = pm.mouse_position()['x'] - previus_mouse_pos['x']
                goto_menu_y = pm.mouse_position()['y'] - previus_mouse_pos['y']
            #print(temp_proc[0]+x_place/temp_proc[2],x_gui)
            esp_change = 0
            esp_change1 = 0
            if drawesp_menu %2==1 and drawesp%2==1:
                esp_change = 1.2
                esp_change1 = 1.18
            else:
                esp_change = 1
                esp_change1 = 1

            ##while fullscreen movement at edges
            if temp_proc[0] == 0:
                if (0<temp_proc[0]+x_place/temp_proc[2]<1/(esp_change*(h_gui**math.sqrt(h_gui))) and (0<temp_proc[1]+y_place/temp_proc[3]<1/(h_gui**0.75))):
                    move_menu_x += goto_menu_x
                    move_menu_y += goto_menu_y
                else:
                    ##left side
                    if 0>temp_proc[0]+x_place/temp_proc[2]:
                        move_menu_x += 1
                    ##right side
                    elif 1/esp_change<(temp_proc[0]+x_place/temp_proc[2])*h_gui**math.sqrt(h_gui):
                        move_menu_x-=1
                    #low
                    elif 0>(temp_proc[1]+y_place/temp_proc[3]):
                        move_menu_y += 15
                    #high
                    else:
                        move_menu_y -= 5
            ##while windowed movement at edges
            else:
                if temp_proc[0]<(temp_proc[0] + temp_proc[2] - (temp_proc[2] + x_place)) * (-2) +10 and (temp_proc[0] + temp_proc[2] - (temp_proc[2] + x_place)) * (-2) <(temp_proc[0] + (temp_proc[2]) * 2)/esp_change1 and temp_proc[1]<(temp_proc[1] + temp_proc[3] - (temp_proc[3] + y_place)) * (-2) + 4 <temp_proc[1] + (temp_proc[3])*2:
                    move_menu_x += goto_menu_x
                    move_menu_y += goto_menu_y
                else:
                    if temp_proc[0]>(temp_proc[0] + temp_proc[2] - (temp_proc[2] + x_place)) * (-2) + 4 :
                        move_menu_x += 1
                    elif (temp_proc[0] + temp_proc[2] - (temp_proc[2] + x_place)) * (-2) + 4>(temp_proc[0] + (temp_proc[2]) * 2)/esp_change1:
                        move_menu_x-=1
                    elif temp_proc[1]>(temp_proc[1] + temp_proc[3] - (temp_proc[3] + y_place)) * (-2) + 4:
                        move_menu_y += 15
                    else:
                        move_menu_y -= 10
                    #pm.draw_rectangle_rounded((x_place / 1.5) + x_gui / 1.45, y_place / 1.5 + 0.05 * (x_gui / 1.5),x_gui / 5, y_gui / 1.83, 0.07, 1,background_color)
            previus_mouse_pos = pm.mouse_position()
        else:
            previus_mouse_pos = 0
    pm.draw_rectangle_rounded_lines(x_place / 1.5, y_place / 1.5, x_gui / 1.5, y_gui / 1.5, 0.03, 1, pm.get_color('white'))





def change_trigger_key(trigger_event):
    time.sleep(0.05)
    key_trigger = kb.read_key()
    print(key_trigger)
    return key_trigger

def calculate_3d_distance(place1, place2):
    distance = math.sqrt((place2[0] - place1[0])**2 + (place2[1] - place1[1])**2 + (place2[2] - place1[2])**2)
    return distance

def save_cfg(currentcfg):
    cfg_name = currentcfg
    print(appdata + "\\" + cfg_name + '.ini')
    with open(appdata+"\\"+cfg_name+'.ini', 'w') as file:
        file.write(f"[esp{cfg_name}]\n")
        file.write(f"drawesp = {str(drawesp)}\n")
        file.write(f"boxes = {str(boxes)}\n")
        file.write(f"skeleton = {str(skeleton)}\n")
        file.write(f"health = {str(health)}\n")
        file.write(f"health_line = {str(health_line)}\n")

        file.write(f"[radar{cfg_name}]\n")
        file.write(f"radar = {str(radar)}\n")
        file.write(f"health_radar = {str(name_radar)}\n")
        file.write(f"name_radar = {str(health_radar)}\n")

        file.write(f"[color{cfg_name}]\n")
        file.write(f"boxes_colorr = {str(boxes_color['r'])}\n")
        file.write(f"boxes_colorg = {str(boxes_color['g'])}\n")
        file.write(f"boxes_colorb = {str(boxes_color['b'])}\n")
        file.write(f"boxes_colora = {str(boxes_color['a'])}\n")
        file.write(f"healthnum_colorr = {str(healthnum_color['r'])}\n")
        file.write(f"healthnum_colorg = {str(healthnum_color['g'])}\n")
        file.write(f"healthnum_colorb = {str(healthnum_color['b'])}\n")
        file.write(f"healthnum_colora = {str(healthnum_color['a'])}\n")
        file.write(f"healthline_colorr = {str(healthline_color['r'])}\n")
        file.write(f"healthline_colorg = {str(healthline_color['g'])}\n")
        file.write(f"healthline_colorb = {str(healthline_color['b'])}\n")
        file.write(f"healthline_colora = {str(healthline_color['a'])}\n")
        file.write(f"skeleton_colorr = {str(skeleton_color['r'])}\n")
        file.write(f"skeleton_colorg = {str(skeleton_color['g'])}\n")
        file.write(f"skeleton_colorb = {str(skeleton_color['b'])}\n")
        file.write(f"skeleton_colora = {str(skeleton_color['a'])}\n")
        file.write(f"weapon_colorr = {str(weapon_color['r'])}\n")
        file.write(f"weapon_colorg = {str(weapon_color['g'])}\n")
        file.write(f"weapon_colorb = {str(weapon_color['b'])}\n")
        file.write(f"weapon_colora = {str(weapon_color['a'])}\n")
        file.write(f"aimpos_colorr = {str(aimpos_color['r'])}\n")
        file.write(f"aimpos_colorg = {str(aimpos_color['g'])}\n")
        file.write(f"aimpos_colorb = {str(aimpos_color['b'])}\n")
        file.write(f"aimpos_colora = {str(aimpos_color['a'])}\n")
        file.write(f"[colorauto{cfg_name}]\n")


        file.write(f"[styles{cfg_name}]\n")
        file.write(f"boxes_roundness = {str(boxes_roundness)}\n")
        file.write(f"line_roundness = {str(line_roundness)}\n")

        file.write(f"[trigger{cfg_name}]\n")
        file.write(f"trigger = {str(trigger)}\n")
        file.write(f"triggerbutton = {str(triggerbutton)}\n")

        file.write(f"[aimbot{cfg_name}]\n")
        file.write(f"aimbot_debug = {str(aimbot_debug)}\n")
        file.write(f"aimbot = {str(aimbot)}\n")
        file.write(f"aimbot_place = {str(aimbot_place)}\n")
        file.write(f"strenght = {str(strenght)}\n")
        file.write(f"change_fov = {str(change_fov)}\n")
        file.write(f"change_strenght = {str(change_strenght)}\n")
        file.write(f"g = {str(g)}\n")

        file.write(f"[menu{cfg_name}]\n")
        file.write(f"button_mouse_onr = {str(button_mouse_on['r'])}\n")
        file.write(f"button_mouse_ong = {str(button_mouse_on['g'])}\n")
        file.write(f"button_mouse_onb = {str(button_mouse_on['b'])}\n")
        file.write(f"button_mouse_ona = {str(button_mouse_on['a'])}\n")
        file.write(f"button_colorr = {str(button_color['r'])}\n")
        file.write(f"button_colorg = {str(button_color['g'])}\n")
        file.write(f"button_colorb = {str(button_color['b'])}\n")
        file.write(f"button_colora = {str(button_color['a'])}\n")
        file.write(f"button_color2r = {str(button_color2['r'])}\n")
        file.write(f"button_color2g = {str(button_color2['g'])}\n")
        file.write(f"button_color2b = {str(button_color2['b'])}\n")
        file.write(f"button_color2a = {str(button_color2['a'])}\n")
        file.write(f"background_colorr = {str(background_color['r'])}\n")
        file.write(f"background_colorg = {str(background_color['g'])}\n")
        file.write(f"background_colorb = {str(background_color['b'])}\n")
        file.write(f"background_colora = {str(background_color['a'])}\n")
        file.write(f"background_color2r = {str(background_color2['r'])}\n")
        file.write(f"background_color2g = {str(background_color2['g'])}\n")
        file.write(f"background_color2b = {str(background_color2['b'])}\n")
        file.write(f"background_color2a = {str(background_color2['a'])}\n")
        file.write(f"color_checkr = {str(color_check['r'])}\n")
        file.write(f"color_checkg = {str(color_check['g'])}\n")
        file.write(f"color_checkb = {str(color_check['b'])}\n")
        file.write(f"color_checka = {str(color_check['a'])}\n")
        file.write(f"button_checkr = {str(button_check['r'])}\n")
        file.write(f"button_checkg = {str(button_check['g'])}\n")
        file.write(f"button_checkb = {str(button_check['b'])}\n")
        file.write(f"button_checka = {str(button_check['a'])}\n")
        file.write(f"button_inactiver = {str(button_inactive['r'])}\n")
        file.write(f"button_inactiveg = {str(button_inactive['g'])}\n")
        file.write(f"button_inactiveb = {str(button_inactive['b'])}\n")
        file.write(f"button_inactivea = {str(button_inactive['a'])}\n")

def open_gui():
    global gui
    gui += 1
    pm.toggle_mouse()
    time.sleep(0.1)
    pm.mouse_click("left")



handle = Memory()

global overlay
class Entity:
    def __init__(self, module_client, mem):
        self.dormant = pm.r_int(mem, module_client + OFFSETS["m_bDormant"])
        self.team = pm.r_int(mem, module_client + OFFSETS['m_iTeamNum'])
        self.position = pm.r_vec3(mem, module_client + OFFSETS['m_vecOrigin'])
        self.position2d = None
def print_queue(q):
    while not q.empty():
        item = q.get()
        print(item)
        q.task_done()

def get_fps(pm):
    fpsget = pm.get_fps()
    pm.draw_rectangle_rounded(temp_proc[0] + temp_proc[2] / 170, temp_proc[1] + temp_proc[3] / 100,
                              (temp_proc[3] / 19) * 2.4, temp_proc[3] / 19, 0.15, 1, pm.new_color(0, 0, 0, 170))
    pm.draw_font(3, "fps: " + str(fpsget), temp_proc[0] + temp_proc[2] / 75, temp_proc[1] + temp_proc[3] / 50,
                 temp_proc[3] / 70, 3, pm.new_color(255, 255, 255, 255))
    pm.draw_font(3, "NightMatch menu", temp_proc[0] + temp_proc[2] / 75,
                 temp_proc[1] + temp_proc[3] / 25, temp_proc[3] / 90, 3, pm.new_color(255, 120, 120, 255))

## recoil control system using memory and win32api to move mouse
def rcs_control(pm):
    global punch, punchold, right_anglex, right_angley,handle
    punchold = (0, 0)
    if pm.key_pressed(1):
        if handle.get_shotsfired(handle.get_local_player_pawn()):
            punchold = punch
            try:
                right_anglex = 0
                punch = handle.get_punch_angle(handle.get_local_player_pawn())
                # win32api.mouse_event(0x00001, 0, int(((temp_proc[3]*2.25)/89)*2), 0, 0)
                angley = punchold[0] - punch[0]
                anglex = punch[1] - punchold[1]
                if angley >= 0.7:
                    angley = 1
                if anglex >= 0.7:
                    anglex = 1
                if angley <= -0.7:
                    angley = -1
                if anglex <= -0.7:
                    anglex = -1
                right_angley = int(angley) * int(((temp_proc[3] * 2.25) / 89) * 2)
                right_anglex = int(anglex) * int(((temp_proc[2] * 1.29) / 90) * 2)
                if right_anglex > 73:
                    right_anglex = 73
                if right_angley > 73:
                    right_angley = 73
            except:
                return(0)
            print(right_anglex)
            win32api.mouse_event(0x00001, right_anglex, right_angley, 0, 0)
    else:
        punch = (0, 0)
        punchold = (0, 0)

##cloud radar offsets by map:
map_location_offset = {"cs_italy":{"y":2592,"x":2647,"scale":4.6},
                       "cs_office":{"y":1858,"x":1838,"scale":4.1},
                       "de_ancient":{"y":2164,"x":2953,"scale":5},
                       "de_anubis":{"y":3328,"x":2796,"scale":5.22},
                       "de_dust2":{"y":3239,"x":2476,"scale":4.4},
                       "de_inferno":{"y":3870,"x":2087,"scale":4.9},
                       "de_mirage":{"y":1713,"x":3230,"scale":5.00},
                       "de_nuke":{"y":2887,"x":3453,"scale":7},
                       "de_overpass":{"y":1781,"x":4831,"scale":5.2},
                       "de_vertigo":{"y":3168,"x":3168,"scale":4.0},
                       "cs_agency":{"y":3239,"x":2476,"scale":4.4},
                       "de_grail":{"y":4203.903,"x":4395.903,"scale":4.3513728},
                       "de_jura":{"y":2389.8,"x":2126.9092,"scale":5.008376},
                       "de_mills":{"y":320,"x":4810,"scale":5.148437},
                       "de_thera":{"y":2261.8025,"x":85.609764,"scale":4.846961},
                       "de_train":{"y":2078,"x":2308,"scale":4.082077}}
#y_player_p = player_pos[1] / 5 + 680
#x_player_p = (player_pos[0] / 5) * (-1) + 375
# sending updates to radar process
def update_cloud_radar(entity_list,coordinates_queue):
    global current_map

    matrix_players = []
    for ent in entity_list:
        player_pos = handle.get_position(ent)
        try:
            y_player_p = (player_pos[1] * (-1) + map_location_offset[current_map]["y"]) / map_location_offset[current_map]["scale"]
            x_player_p = (player_pos[0] + map_location_offset[current_map]["x"] ) / map_location_offset[current_map]["scale"]
        except:
            y_player_p = player_pos[1]
            x_player_p = player_pos[0]

        index_entity = entity_list.index(ent)
        teamnum_matrix = handle.get_team(ent)
        health_matrix = handle.get_he(ent)
        if health_matrix <= 0:
            x_player_p = -100
            y_player_p = -100

        listneededent = []
        listneededent.append(index_entity)
        listneededent.append(x_player_p)
        listneededent.append(y_player_p)
        listneededent.append(teamnum_matrix)

        matrix_players.append(listneededent)
    # print(matrix_players)

    clear_queue(coordinates_queue)
    coordinates_queue.put((matrix_players))

# drawing player rank in tab menu - with names and color
def tab_rank_menu(pm,entity_list, textures):
    rank = handle.get_rank(ent)
    wins = str(handle.get_wins(ent))
    name = handle.get_name(ent)

    t_color = handle.get_color_mm(ent)
    if name != "":
        player_index = entity_list.index(ent) + 1
        t_color_str = kfc_teamcolor[t_color]
        # print(name)

        rank_str = kfc_rank[rank]
        # print(rank_str)
        heigth_calc = temp_proc[1] + temp_proc[3] * 0.3 + (temp_proc[3] // 28.8) * player_index
        text_size_tab = temp_proc[2] // 75
        texture_size = 0.00034722222 * temp_proc[3]

        pm.draw_font(3, "rank", temp_proc[0] + temp_proc[2] // 51.2, temp_proc[1] + temp_proc[3] * 0.3, text_size_tab,
                     1, pm.get_color("white"))
        pm.draw_font(3, "wins", temp_proc[0] + temp_proc[2] // 15, temp_proc[1] + temp_proc[3] * 0.3, text_size_tab, 1,
                     pm.get_color("white"))
        pm.draw_font(3, "color", temp_proc[0] + temp_proc[2] // 10, temp_proc[1] + temp_proc[3] * 0.3, text_size_tab, 1,
                     pm.get_color("white"))
        pm.draw_font(3, "name", temp_proc[0] + temp_proc[2] // 7.3, temp_proc[1] + temp_proc[3] * 0.3, text_size_tab, 1,
                     pm.get_color("white"))

        pm.draw_font(3, wins, temp_proc[0] + temp_proc[2] // 15, heigth_calc, text_size_tab, 1, pm.get_color("white"))
        pm.draw_texture(textures[rank_str], temp_proc[0] + temp_proc[2] // 51.2, heigth_calc, pm.get_color("white"), 0,
                        texture_size)
        # pm.draw_font(3,rank_str, temp_proc[0]+temp_proc[2]//51.2 ,heigth_calc, text_size_tab,1, pm.get_color("white"))
        pm.draw_font(3, name, temp_proc[0] + temp_proc[2] // 7.3, heigth_calc, text_size_tab, 1, pm.get_color("white"))
        pm.draw_font(3, t_color_str, temp_proc[0] + temp_proc[2] // 10, heigth_calc, text_size_tab, 1,
                     pm.get_color("white"))
        # print(entity_list)

#
def find_bomber(pm):
    global color_time
    temp_bomb = handle.get_plantedbomb()
    bomb_place = temp_bomb[0]
    time_b = temp_bomb[1]
    defused = temp_bomb[2]
    if time_b < 5:
        color_time = pm.new_color(255, 0, 0, 255)
    elif time_b < 10:
        color_time = pm.new_color(255, 255, 0, 255)
    else:
        color_time= pm.new_color(255, 255, 255, 255)
    if defused:
        lines_def = pm.new_color(0, 255, 0, 255)
    else:
        lines_def = pm.new_color(255, 255, 255, 255)
    posbomb = world_to_screen1(bomb_place, viewmat, temp_proc)
    pm.draw_circle(posbomb['x'], posbomb['y'], 3, pm.get_color('red'))
    pm.draw_rectangle_rounded(posbomb['x'] - 50, posbomb['y'] - 60, 100, 40, 0.1, 1, pm.new_color(0, 0, 0, 120))
    pm.draw_rectangle_rounded_lines(posbomb['x'] - 50, posbomb['y'] - 60, 100, 40, 0.1, 1,
                                    lines_def)
    pm.draw_font(3, "Bomb", posbomb['x'] - 16, posbomb['y'] - 57, 15, 1, pm.new_color(255, 255, 255, 255))
    pm.draw_rectangle_rounded(posbomb['x'] - 45, posbomb['y'] - 35, 90, 10, 0.3, 1,
                              pm.new_color(0, 0, 0, 255))
    pm.draw_rectangle_rounded(posbomb['x'] - 44, posbomb['y'] - 33, 87 / 40 * time_b, 6, 0.3, 1,
                              color_time)


def draw_radar_func(pm,x_window,y_window,x_wid, y_hei,dot_y_per,dot_x_per,health_ent,ent):
    global radar_name_color, radar_health_color, health_radar, name_radar, radar_color_auto_name, radar_color_auto_health, color_name_c_radar, color_health_c_radar
    color2 = pm.new_color(0, 0, 0, 100)
    pm.new_color(50, 50, 50, 50)
    pm.draw_line(50 + x_window, y_hei + 200 + y_window, 450 + x_window, y_hei + 200 + y_window,
                 color2,
                 10)
    pm.draw_line(50 + x_window, y_hei - 200 + y_window, 450 + x_window, y_hei - 200 + y_window,
                 color2,
                 10)
    pm.draw_line(50 + x_window, y_hei - 205 + y_window, 50 + x_window, y_hei + 205 + y_window,
                 color2,
                 10)
    pm.draw_line(450 + x_window, y_hei - 205 + y_window, 450 + x_window, y_hei + 205 + y_window,
                 color2,
                 10)
    pm.draw_line(250 + x_window, y_hei - 195 + y_window, 250 + x_window, y_hei + 195 + y_window,
                 pm.get_color("black"), 1)
    pm.draw_line(55 + x_window, y_hei + y_window, 445 + x_window, y_hei + y_window,
                 pm.get_color("black"), 1)
    if dot_y_per + y_hei > y_hei + 197 or dot_y_per + y_hei < y_hei - 200 or 250 - dot_x_per > 452 or 250 - dot_x_per < 52:
        temp = "temp"
    else:
        healthnum = str(health_ent)
        name = str(handle.get_name(ent))
        if radar_color_auto_name == 0:
            color_name_c_radar = radar_name_color
        if radar_color_auto_health == 0:
            color_health_c_radar = radar_health_color
        if health_radar % 2 == 1:
            pm.draw_text(healthnum, 50 + 200 + x_window - (dot_x_per),
                         y_hei + y_window + (dot_y_per) + 10, 20, color_health_c_radar)
        if name_radar % 2 == 1:
            pm.draw_text(name, 50 + 200 + x_window - (dot_x_per),
                         y_hei + y_window + (dot_y_per) + 35, 15, color_name_c_radar)
        pm.draw_circle(50 + 200 + x_window, y_hei + y_window, 3, pm.get_color('purple'))
        pm.draw_circle(50 + 200 + x_window - (dot_x_per), y_hei + y_window + (dot_y_per), 6.5,
                       color_health_c_radar)
        pm.draw_circle(50 + 200 + x_window - (dot_x_per), y_hei + y_window + (dot_y_per), 2,
                       pm.get_color("white"))


def trigger_func(pm, ent):
    global ofssetye, offsetesp, offset_xafter, pos2dglobal1, pos2dglobal2, distancepos, fixforoffsetboxes_x, fixforoffsetboxes_y, numxtimed, value_offset, right_anglex, right_angley
    pos2dglobal1 = world_to_screen1(posglobal, viewmat, temp_proc)
    pos2dglobal2 = world_to_screen1(posglobal2, viewmat, temp_proc)
    distancepos = math.sqrt((pos2dglobal1['x'] - pos2dglobal2['x']) ** 2 + (
            pos2dglobal1['y'] - pos2dglobal2['y']) ** 2)
    fixforoffsetboxes_x = (temp_proc[0] + temp_proc[2] / 2 - pos2dglobal1['x'])
    if fixforoffsetboxes_x < xtrypos / 2:
        offsetesp = ((fixforoffsetboxes_x * distancepos / 3 / temp_proc[2]))
    else:
        offsetesp = ((fixforoffsetboxes_x * distancepos / 4 / temp_proc[2]))

    fixforoffsetboxes_y = (temp_proc[1] + temp_proc[3] / 2 - pos2dglobal1['y'])
    if fixforoffsetboxes_y < three_x / 2:
        ofssetye = ((fixforoffsetboxes_y * distancepos / 3 / temp_proc[3])) / 120
        numxtimed = 1
        value_offset = 1
    else:
        ofssetye = ((fixforoffsetboxes_y * distancepos / 4 / temp_proc[3])) / 120
        numxtimed = 1.1
        value_offset = -1
    offset_xafter = 1
    if ofssetye != 0:
        offset_xafter = numxtimed / 1 / ofssetye / 500
    if ofssetye < 0:
        ofssetye = ofssetye * (-1)


def objects_without_trigger(pm, ent):
    global ofssetye, offsetesp, offset_xafter, pos2dglobal1, pos2dglobal2, distancepos, fixforoffsetboxes_x, fixforoffsetboxes_y, numxtimed, value_offset, right_anglex, right_angley
    pos2dglobal1 = world_to_screen1(posglobal, viewmat, temp_proc)
    pos2dglobal2 = world_to_screen1(posglobal2, viewmat, temp_proc)

    distancepos = math.sqrt(
        (pos2dglobal1['x'] - pos2dglobal2['x']) ** 2 + (
                pos2dglobal1['y'] - pos2dglobal2['y']) ** 2)
    fixforoffsetboxes_x = (temp_proc[0] + temp_proc[2] / 2 - pos2dglobal1['x'])
    if fixforoffsetboxes_x < xtrypos / 2:
        offsetesp = ((fixforoffsetboxes_x * distancepos / 3 / temp_proc[2]))
    else:
        offsetesp = ((fixforoffsetboxes_x * distancepos / 4 / temp_proc[2]))


def get_the_rest_of_the_bones():
    global pos2d22b, pos2d25b, pos2d13b, pos2d8b, pos2d5b, pos2d9b, pos2d45b, pos2d14b, pos2d41b, pos2d23b, pos2d26b, pos2d1b, pos2d27b, pos2d24b
    pos2d22b = world_to_screen1(posbone22, viewmat, temp_proc)
    pos2d25b = world_to_screen1(posbone25, viewmat, temp_proc)
    pos2d13b = world_to_screen1(posbone13, viewmat, temp_proc)
    pos2d8b = world_to_screen1(posbone8, viewmat, temp_proc)
    pos2d5b = world_to_screen1(posbone5, viewmat, temp_proc)
    pos2d9b = world_to_screen1(posbone9, viewmat, temp_proc)
    pos2d45b = world_to_screen1(posbone45, viewmat, temp_proc)
    pos2d14b = world_to_screen1(posbone14, viewmat, temp_proc)
    pos2d41b = world_to_screen1(posbone41, viewmat, temp_proc)
    pos2d23b = world_to_screen1(posbone23, viewmat, temp_proc)
    pos2d26b = world_to_screen1(posbone26, viewmat, temp_proc)
    pos2d1b = world_to_screen1(posbone1, viewmat, temp_proc)
    pos2d27b = world_to_screen1(posbone27, viewmat, temp_proc)
    pos2d24b = world_to_screen1(posbone24, viewmat, temp_proc)


def aimbot_function_moved():

    global sens,strenght, three_x111, posaim2d, head2dya, body2da, xtrypos111, distancepos, body2dya, shots, posaimhelpwd
    if 1 == 1:
        try:
            shots = handle.get_shotsfired(handle.get_local_player_pawn())
            posaim2d = pos2dglobal1
            posaim2_2d = pos2dglobal2
            xpos1, ypos1 = posaim2d['x'], posaim2d['y']
            xpos2, ypos2 = posaim2_2d['x'], posaim2_2d['y']
            distancepos = math.sqrt((xpos2 - xpos1) ** 2 + (ypos2 - ypos1) ** 2)
            hypotenusepos = distancepos / 2
            xtrypos111 = math.sqrt(hypotenusepos ** 2 / 4.5796)  # 10 is 1^2 + 3^2
            xtrypos111 = (xtrypos111 * 1.2) * g

            three_x111 = 2.14 * xtrypos111
            head2dya = posaim2d['y'] - three_x111 / 8
            body2da = posaim2d['x'] - xtrypos111 / 10
            body2dya = posaim2d['y'] + three_x111 / 10
        except:
            pass
        j = float(1)
        if aimbot_place % 2 == 1:
            if (body2da - xtrypos111 * 0.8) / j < temp_proc[0] + temp_proc[2] / 2 < (
                    body2da - xtrypos111 * 0.8 + xtrypos111 * 2) * j and (
                    head2dya - three_x111 * 0.4) / j < temp_proc[1] + temp_proc[3] / 2 < (
                    head2dya - three_x111 * 0.4 + three_x111 * 0.7) * j:
                pm.draw_circle(posaim2d['x'] + offsetesp, posaim2d['y'], distancepos / 20, aimpos_color)
            if (body2da - xtrypos111 * 0.8) * j < temp_proc[0] + temp_proc[2] / 2 < (
                    body2da - xtrypos111 * 0.8 + xtrypos111 * 2) * j and (
                    body2dya + xtrypos111 * 0.2) * j < temp_proc[1] + temp_proc[3] / 2 < (
                    body2dya + xtrypos111 * 0.2 + three_x111 * 0.7) * j:
                posaimhelpwd = world_to_screen1(posaimhelp, viewmat, temp_proc)
                pm.draw_circle(posaimhelpwd['x'] + offsetesp, posaimhelpwd['y'], distancepos / 20, aimpos_color)
        if shots:
            if 1 == 1:
                if 1 == 1:
                    if rcs_im % 2 == 1:
                        reduce_recoil = shots * (temp_proc[3] * 0.01) * 1.5 / sens
                    else:
                        reduce_recoil = 0
                    strenght = int(strenght)

                    if aimbot_debug % 2 == 1:
                        pm.draw_rectangle_rounded_lines(body2da - xtrypos111 * 0.8,
                                                        head2dya - three_x111 * 0.4,
                                                        xtrypos111 * 2, three_x111 * 0.7,
                                                        boxes_roundness, 1,
                                                        pm.get_color('white'), 2)
                        pm.draw_rectangle_rounded_lines(body2da - xtrypos111 * 0.8,
                                                        head2dya - three_x111 * 0.55,
                                                        xtrypos111 * 2, three_x111 * 0.7,
                                                        boxes_roundness, 1,
                                                        pm.get_color('white'), 2)
                        pm.draw_rectangle_rounded_lines(body2da - xtrypos111 * 0.8,
                                                        body2dya + xtrypos111 * 0.2,
                                                        xtrypos111 * 2, three_x111 * 0.7,
                                                        boxes_roundness, 1,
                                                        pm.get_color('white'), 2)
                        pm.draw_rectangle_rounded_lines(body2da - xtrypos111 * 0.8,
                                                        body2dya - xtrypos111 * 0.65,
                                                        xtrypos111 * 2, three_x111 * 0.7,
                                                        boxes_roundness, 1, pm.get_color('red'),
                                                        2)
                        pm.draw_line(temp_proc[0] + temp_proc[2] / 2 - temp_proc[2] / 17,
                                     temp_proc[1] + temp_proc[3] / 2 + temp_proc[3] / 9.57,
                                     temp_proc[0] + temp_proc[2] / 2 + temp_proc[2] / 17,
                                     temp_proc[1] + temp_proc[3] / 2 - temp_proc[3] / 9.57, pm.get_color('white'), 2)
                    if temp_proc[0] + temp_proc[2] / 2 - temp_proc[2] / 17 < posaim2d['x'] < temp_proc[0] + temp_proc[
                        2] / 2 + temp_proc[2] / 17 and temp_proc[1] + temp_proc[3] / 2 - temp_proc[3] / 9.57 < posaim2d[
                        'y'] < temp_proc[1] + temp_proc[3] / 2 + temp_proc[3] / 9.57:
                        if (body2da - xtrypos111 * 0.8) / j < temp_proc[0] + temp_proc[2] / 2 < (
                                body2da - xtrypos111 * 0.8 + xtrypos111 * 2) * j and (
                                head2dya - three_x111 * 0.4) / j < temp_proc[1] + temp_proc[
                            3] / 2 < (head2dya - three_x111 * 0.4 + three_x111 * 0.7) * j:
                            distanceforaim = math.sqrt(
                                (posaim2d['x'] - (temp_proc[0] + temp_proc[2]) / 2) ** 2 + (
                                        posaim2d['y'] + reduce_recoil - (temp_proc[1] + temp_proc[3]) / 2) ** 2)
                            speedaim = int(strenght * distanceforaim / 150)

                            if temp_proc[0] + temp_proc[2] / 2 * 0.99 < (((
                                                                                  body2da - xtrypos111 * 0.8) + (
                                                                                  body2da - xtrypos111 * 0.8 + xtrypos111 * 2)) / 2) * j:
                                win32api.mouse_event(0x00001, speedaim, 0, 0, 0)
                            if (((body2da - xtrypos111 * 0.8) + (
                                    body2da - xtrypos111 * 0.8 + xtrypos111 * 2)) / 2) * j < \
                                    temp_proc[0] + temp_proc[2] / 2 * 1.005:
                                win32api.mouse_event(0x00001, -speedaim, 0, 0, 0)
                            if temp_proc[1] + temp_proc[3] / 2 < head2dya / j + reduce_recoil:
                                win32api.mouse_event(0x00001, 0, speedaim, 0, 0)
                    try:
                        if temp_proc[0] + temp_proc[2] / 2 - temp_proc[2] / 17 < posaimhelpwd['x'] < temp_proc[0] + \
                                temp_proc[2] / 2 + temp_proc[2] / 17 and temp_proc[1] + temp_proc[3] / 2 - temp_proc[
                            3] / 9.57 < posaimhelpwd['y'] < temp_proc[1] + temp_proc[3] / 2 + temp_proc[3] / 9.57:
                            if (body2da - xtrypos111 * 0.8) * j < temp_proc[0] + temp_proc[2] / 2 < (
                                    body2da - xtrypos111 * 0.8 + xtrypos111 * 2) * j and (
                                    body2dya + xtrypos111 * 0.2) * j < temp_proc[1] + temp_proc[
                                3] / 2 < (body2dya + xtrypos111 * 0.2 + three_x111 * 0.7) * j:

                                reduce_recoil = reduce_recoil * 0.5

                                distanceforaim = math.sqrt(
                                    ((temp_proc[1] + temp_proc[3]) - (posaimhelpwd['x'] + reduce_recoil) / 2) ** 2)
                                speedaim = int(strenght * distanceforaim / 1700)

                                if temp_proc[0] + temp_proc[2] / 2 * 0.98 < (((
                                                                                      body2da - xtrypos111 * 0.8) + (
                                                                                      body2da - xtrypos111 * 0.8 + xtrypos111 * 2)) / 2) * j:
                                    win32api.mouse_event(0x00001, speedaim, 0, 0, 0)
                                if (((body2da - xtrypos111 * 0.8) + (
                                        body2da - xtrypos111 * 0.8 + xtrypos111 * 2)) / 2) * j < \
                                        temp_proc[0] + temp_proc[2] / 2 * 1.005:
                                    win32api.mouse_event(0x00001, -speedaim, 0, 0, 0)
                                if temp_proc[1] + temp_proc[3] / 2 < (body2dya) * j + reduce_recoil:
                                    win32api.mouse_event(0x00001, 0, speedaim, 0, 0)
                    except:
                        pass

def trigger_activated(pm,x_window,y_window,x_wid, y_hei,dot_y_per,dot_x_per,health_ent,ent,avoid_x2,widwindow,avoid_y,heiwindow,avoid_x,avoid_y2):
        global body2d, xtrypos11, body2dy, three_x11, head2dy
        try:
            xpos1, ypos1 = pos2dglobal1['x'], pos2dglobal1['y']
            xpos2, ypos2 = pos2dglobal2['x'], pos2dglobal2['y']
            distancepos = math.sqrt((xpos2 - xpos1) ** 2 + (ypos2 - ypos1) ** 2)
            hypotenusepos = distancepos / 2

            # Use the Pythagorean theorem to find x
            xtrypos11 = math.sqrt(hypotenusepos ** 2 / 4.5796)  # 10 is 1^2 + 3^2
            xtrypos11 = xtrypos11 * 1.2

            three_x11 = 2.14 * xtrypos11
            body2d = pos2dglobal1['x'] - xtrypos11 / 10
            body2dy = pos2dglobal1['y'] + three_x11 / 10
            head2dy = pos2dglobal1['y'] - three_x11 / 8

        except:
            pass
        if x_window == 0:
            if (
                    body2d + offsetesp < x_wid < body2d + xtrypos11 * 0.5 + offsetesp and body2dy < y_hei < body2dy + three_x11 * 0.7) or (
                    body2d + offsetesp < x_wid < body2d + xtrypos11 * 0.3 + offsetesp and head2dy < y_hei < head2dy + three_x11 * 0.2):
                pm.mouse_click('left')
        else:
            if (
                    body2d + offsetesp < avoid_x2 + widwindow / 2 < body2d + xtrypos11 * 0.3 + offsetesp and body2dy < avoid_y - heiwindow / 2 < body2dy + three_x11 * 0.7) or (
                    body2d + offsetesp < avoid_x2 + widwindow / 2 < body2d + xtrypos11 * 0.15 + offsetesp and head2dy < avoid_y - heiwindow / 2 < head2dy + three_x11 * 0.2):
                pm.mouse_click('left')
        pm.draw_text("trigger", 20, 20, 25, pm.get_color('red'))
        if trigger_visuals % 2 == 1:
            if avoid_x2 < body2d < avoid_x - xtrypos11 and avoid_y2 < head2dy < avoid_y - three_x11:
                pm.draw_rectangle_rounded_lines(body2d + offsetesp, body2dy, xtrypos11 * 0.3,
                                                three_x11 * 0.7, boxes_roundness, 1,
                                                pm.get_color('white'), 2)
                pm.draw_rectangle_rounded_lines(body2d + offsetesp, head2dy, xtrypos11 * 0.15,
                                                three_x11 * 0.2, boxes_roundness, 1,
                                                pm.get_color('white'), 2)


def draw_weapon(pm, ent, textures,weapon_temp,enemy_pos_temp,x_window,avoid_x2,avoid_x,avoid_y2,avoid_y):

    global temp_c4,c4_pos, weapon, weapon_scale, bomb_carrier, x_weapon_bomb
    if show_weapons % 2 == 1:
        try:
            weapon = kfc_weapon[weapon_temp[0]]
        except:
            pass
        try:
            if weapon == "C4":
                save_c4 = weapon_temp[1]
        except:
            pass
        try:
            if c4_pos == enemy_pos_temp:
                bomb_carrier = ent.pawn_ptr
        except:
            pass
        if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
            xposht1, yposht1 = pos2dglobal1['x'], pos2dglobal1['y']
            xposht2, yposht2 = pos2dglobal2['x'], pos2dglobal2['y']
            distancepos = math.sqrt((xposht2 - xposht1) ** 2 + (yposht2 - yposht1) ** 2)
            hypotenusepos = distancepos

            # Use the Pythagorean theorem to find x
            xtrypos2 = math.sqrt(hypotenusepos ** 2 / 1)  # 10 is 1^2 + 3^2
            xtrypos2 = xtrypos2 * 1.2

            three_x2 = 2.14 * xtrypos2
            x_weapon = pos2dglobal1['x']
            y_weapon = pos2dglobal1['y'] + three_x2 / 2.4

            weapon_c = weapon_color
            try:

                try:
                    weapon_scale = xtrypos2 / 1200
                    active_texture = textures[weapon]
                    x_weapon = x_weapon - xtrypos2 * (0.0004 * (active_texture['width']))
                    x_weapon_bomb = pos2dglobal1['x'] - xtrypos2 * (0.0026 * (textures['C4']['width']))

                    if weapon_visibility % 2 == 0:
                        if weapon_scale < 0.25:
                            weapon_scale = 0.25
                            x_weapon = x_weapon - xtrypos2 * (0.0000001 * (textu['width'])) + (
                                        xtrypos - textu['width']) / 7.5
                            y_weapon = y_weapon - (xtrypos - textu['width']) / 14

                except:
                    pass
                x_weapon += offsetesp
                if 0 != x_window:
                    if avoid_x2 < x_weapon < avoid_x - xtrypos2 / 4.5 and avoid_y2 < y_weapon < avoid_y - xtrypos2 / 6:
                        try:
                            pm.draw_texture(textures[weapon], x_weapon, y_weapon, weapon_c, 0, weapon_scale)
                        except:
                            pass
                else:
                    try:
                        pm.draw_texture(textures[weapon], x_weapon, y_weapon, weapon_c, 0, weapon_scale)
                    except:
                        pass
                    try:
                        if temp_c4[0] != 0:
                            if ent.pawn_ptr == bomb_carrier:
                                if draw_c4 % 2 == 1:
                                    pm.draw_texture(textures['C4'], x_weapon_bomb + offsetesp,
                                                    pos2dglobal1['y'] - three_x2 / 16, weapon_c, 0,
                                                    weapon_scale)
                    except:
                        pass
            except:
                pass
            # list_ent[index_check] = weapon
def draw_health_line(pm,x_window,avoid_x2,avoid_x,avoid_y2,avoid_y,health_ent):
    global pos2dhealth_line, xtrypos1, three_x1, healthline_c
    if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
        poshealth = posglobal
        poshealth2 = posglobal2
        # print(pos1)
        try:
            pos2dhealth_line = world_to_screen1(poshealth, viewmat, temp_proc)
            pos2dhealth_line2 = world_to_screen1(poshealth2, viewmat, temp_proc)

            xposh1, yposh1 = pos2dhealth_line['x'], pos2dhealth_line['y']
            xposh2, yposh2 = pos2dhealth_line2['x'], pos2dhealth_line2['y']
            distancepos1 = math.sqrt((xposh2 - xposh1) ** 2 + (yposh2 - yposh1) ** 2)
            hypotenusepos1 = distancepos1

            xtrypos1 = math.sqrt(hypotenusepos1 ** 2 / 842)  # 10 is 1^2 + 3^2
            xtrypos1 = xtrypos1 * 1.2

            three_x1 = 29 * xtrypos1
            pos2dhealth_line['x'] += xtrypos1 * 8
            pos2dhealth_line['y'] -= three_x1 / 8
            healthline_c = healthline_color
            try:
                pos2dhealth_line['x'] += offsetesp
            except:
                pass
            # 310,150,250
        except:
            pass
        if x_window != 0:
            if avoid_x2 < pos2dhealth_line['x'] < avoid_x - xtrypos1 and avoid_y2 < \
                    pos2dhealth_line['y'] < avoid_y - three_x1:
                healthnum = health_ent
                pm.draw_rectangle_rounded(pos2dhealth_line['x'], pos2dhealth_line['y'],
                                          xtrypos1, three_x1, line_roundness, 1,
                                          pm.new_color(0, 0, 0, 170))
                pm.draw_rectangle_rounded(pos2dhealth_line['x'], pos2dhealth_line['y'],
                                          xtrypos1, three_x1 / 100 * healthnum,
                                          line_roundness, 1, healthline_c)
        else:
            healthnum = health_ent
            pm.draw_rectangle_rounded(pos2dhealth_line['x'], pos2dhealth_line['y'],
                                      xtrypos1, three_x1, line_roundness, 1,
                                      pm.new_color(0, 0, 0, 170))
            pm.draw_rectangle_rounded(pos2dhealth_line['x'], pos2dhealth_line['y'],
                                      xtrypos1, three_x1 / 100 * healthnum, line_roundness,
                                      1, healthline_c)

def draw_skeleton_in_game(pos2d8b,pos2d13b):
    global sens, posbone5, posbone8, posbone13, posbone14, posbone9, posbone22, posbone25, posbone41, posbone23, posbone26, posbone1, posbone27, posbone24, posbone45
    if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
        distancepos1 = math.sqrt(
            (posglobal[0] - posbone5[0]) ** 2 + (posglobal[1] - posbone5[1]) ** 2 + (
                    posglobal[2] - posbone5[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2dglobal1['x'] + offsetesp, pos2dglobal1['y'], pos2d5b['x'] + offsetesp,
                         pos2d5b['y'], skeleton_color, 1)

        distancepos1 = math.sqrt(
            (posbone5[0] - posbone8[0]) ** 2 + (posbone5[1] - posbone8[1]) ** 2 + (
                    posbone5[2] - posbone8[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d5b['x'] + offsetesp, pos2d5b['y'], pos2d8b['x'] + offsetesp,
                         pos2d8b['y'], skeleton_color, 1)

        distancepos1 = math.sqrt(
            (posbone5[0] - posbone13[0]) ** 2 + (posbone5[1] - posbone13[1]) ** 2 + (
                    posbone5[2] - posbone13[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d5b['x'] + offsetesp, pos2d5b['y'], pos2d13b['x'] + offsetesp,
                         pos2d13b['y'], skeleton_color, 1)

        distancepos1 = math.sqrt(
            (posbone13[0] - posbone14[0]) ** 2 + (posbone13[1] - posbone14[1]) ** 2 + (
                    posbone13[2] - posbone14[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d13b['x'] + offsetesp, pos2d13b['y'], pos2d14b['x'] + offsetesp,
                         pos2d14b['y'], skeleton_color, 1)

        distancepos1 = math.sqrt(
            (posbone8[0] - posbone9[0]) ** 2 + (posbone8[1] - posbone9[1]) ** 2 + (
                    posbone8[2] - posbone9[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d8b['x'] + offsetesp, pos2d8b['y'], pos2d9b['x'] + offsetesp,
                         pos2d9b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone9[0] - posbone45[0]) ** 2 + (posbone9[1] - posbone45[1]) ** 2 + (
                    posbone9[2] - posbone45[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d9b['x'] + offsetesp, pos2d9b['y'], pos2d45b['x'] + offsetesp,
                         pos2d45b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone14[0] - posbone41[0]) ** 2 + (posbone14[1] - posbone41[1]) ** 2 + (
                    posbone14[2] - posbone41[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d14b['x'] + offsetesp, pos2d14b['y'], pos2d41b['x'] + offsetesp,
                         pos2d41b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone5[0] - posbone1[0]) ** 2 + (posbone5[1] - posbone1[1]) ** 2 + (
                    posbone5[2] - posbone1[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d5b['x'] + offsetesp, pos2d5b['y'], pos2d1b['x'] + offsetesp,
                         pos2d1b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone1[0] - posbone22[0]) ** 2 + (posbone1[1] - posbone22[1]) ** 2 + (
                    posbone1[2] - posbone22[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d1b['x'] + offsetesp, pos2d1b['y'], pos2d22b['x'] + offsetesp,
                         pos2d22b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone22[0] - posbone23[0]) ** 2 + (posbone22[1] - posbone23[1]) ** 2 + (
                    posbone22[2] - posbone23[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d22b['x'] + offsetesp, pos2d22b['y'], pos2d23b['x'] + offsetesp,
                         pos2d23b['y'], skeleton_color, 1)

        distancepos1 = math.sqrt(
            (posbone23[0] - posbone24[0]) ** 2 + (posbone23[1] - posbone24[1]) ** 2 + (
                    posbone23[2] - posbone24[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d23b['x'] + offsetesp, pos2d23b['y'], pos2d24b['x'] + offsetesp,
                         pos2d24b['y'], skeleton_color, 1)

        distancepos1 = math.sqrt(
            (posbone1[0] - posbone25[0]) ** 2 + (posbone1[1] - posbone25[1]) ** 2 + (
                    posbone1[2] - posbone25[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d1b['x'] + offsetesp, pos2d1b['y'], pos2d25b['x'] + offsetesp,
                         pos2d25b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone25[0] - posbone26[0]) ** 2 + (posbone25[1] - posbone26[1]) ** 2 + (
                    posbone25[2] - posbone26[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d25b['x'] + offsetesp, pos2d25b['y'], pos2d26b['x'] + offsetesp,
                         pos2d26b['y'], skeleton_color, 1)
        distancepos1 = math.sqrt(
            (posbone26[0] - posbone27[0]) ** 2 + (posbone26[1] - posbone27[1]) ** 2 + (
                    posbone26[2] - posbone27[2]) ** 2)
        if distancepos1 < 30:
            pm.draw_line(pos2d26b['x'] + offsetesp, pos2d26b['y'], pos2d27b['x'] + offsetesp,
                         pos2d27b['y'], skeleton_color, 1)

        if skeleton_style % 2 == 1:
            distancepos1 = math.sqrt(
                (posbone8[0] - posbone13[0]) ** 2 + (posbone8[1] - posbone13[1]) ** 2 + (
                        posbone8[2] - posbone13[2]) ** 2)
            if distancepos1 < 30:
                pm.draw_line((pos2d8b['x']) + offsetesp, pos2d8b['y'], (pos2d13b['x']) + offsetesp,
                             pos2d13b['y'], skeleton_color, 1)

            distancepos1 = math.sqrt(
                (posbone8[0] - posbone22[0]) ** 2 + (posbone8[1] - posbone22[1]) ** 2 + (
                        posbone8[2] - posbone22[2]) ** 2)
            if distancepos1 < 30:
                pm.draw_line((pos2d8b['x']) + offsetesp, pos2d8b['y'], (pos2d22b['x']) + offsetesp,
                             pos2d22b['y'],
                             skeleton_color, 1)

            distancepos1 = math.sqrt(
                (posbone13[0] - posbone25[0]) ** 2 + (posbone13[1] - posbone25[1]) ** 2 + (
                        posbone13[2] - posbone25[2]) ** 2)
            if distancepos1 < 30:
                pm.draw_line((pos2d13b['x']) + offsetesp, pos2d13b['y'],
                             (pos2d25b['x']) + offsetesp, pos2d25b['y'],
                             skeleton_color, 1)

            distancepos1 = math.sqrt(
                (posbone25[0] - posbone22[0]) ** 2 + (posbone25[1] - posbone22[1]) ** 2 + (
                        posbone25[2] - posbone22[2]) ** 2)
            if distancepos1 < 30:
                pm.draw_line((pos2d25b['x']) + offsetesp, pos2d25b['y'],
                             (pos2d22b['x']) + offsetesp, pos2d22b['y'],
                             skeleton_color, 1)
        if draw_head_skeleton % 2 == 1:
            xpos1, ypos1 = pos2dglobal1['x'], pos2dglobal1['y']
            xpos2, ypos2 = pos2dglobal2['x'], pos2dglobal2['y']
            distancepos = math.sqrt((xpos2 - xpos1) ** 2 + (ypos2 - ypos1) ** 2)
            pm.draw_ellipse_lines(pos2dglobal1['x'] + offsetesp, pos2dglobal1['y'], (distancepos * 2 / 3) / 10,
                                  (distancepos) / 10, skeleton_color)
        if draw_game_boxes % 2 == 1:
            try:
                bone1help = list(posbone8)
                bone1help[1] = posbone8[1] * 1.035
                posbone8 = tuple(bone1help)
                pos2d8b = world_to_screen1(posbone8, viewmat, temp_proc)
                bone1help = list(posbone13)
                bone1help[1] = posbone13[1] / 1.035
                posbone13 = tuple(bone1help)
                pos2d13b = world_to_screen1(posbone13, viewmat, temp_proc)

                bone2d1 = world_to_screen1(posbone1, viewmat, temp_proc)

                pm.draw_circle((bone2d1['x'] - (bone2d1['x'] - pos2d13b['x'])) + offsetesp,
                               bone2d1['y'] + (bone2d1['y'] - pos2dglobal2['y']), 6,
                               pm.get_color('white'))
                pm.draw_circle((bone2d1['x'] - (bone2d1['x'] - pos2d8b['x'])) + offsetesp,
                               bone2d1['y'] + (bone2d1['y'] - pos2dglobal2['y']), 6,
                               pm.get_color('cyan'))

                pm.draw_circle((bone2d1['x'] - (bone2d1['x'] - pos2d13b['x'])) + offsetesp,
                               bone2d1['y'] - (bone2d1['y'] - pos2dglobal2['y']), 6,
                               pm.get_color('green'))
                pm.draw_circle((bone2d1['x'] - (bone2d1['x'] - pos2d8b['x'])) + offsetesp,
                               bone2d1['y'] - (bone2d1['y'] - pos2dglobal2['y']), 6,
                               pm.get_color('red'))

                pm.draw_line((bone2d1['x'] - (bone2d1['x'] - pos2d13b[
                    'x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * offset_xafter,
                             bone2d1['y'] - (bone2d1['y'] - pos2dglobal2['y']), (bone2d1['x'] - (bone2d1['x'] - pos2d8b[
                        'x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * offset_xafter,
                             bone2d1['y'] - (bone2d1['y'] - pos2dglobal2['y']), pm.get_color('yellow'), 1)
                pm.draw_line((bone2d1['x'] - (
                            bone2d1['x'] - pos2d13b['x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * 2,
                             bone2d1['y'] + (bone2d1['y'] - pos2dglobal2['y']),
                             (bone2d1['x'] - (bone2d1['x'] - pos2d13b[
                                 'x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * offset_xafter,
                             bone2d1['y'] - (bone2d1['y'] - pos2dglobal2['y']), pm.get_color('green'),
                             1)

                pm.draw_line((bone2d1['x'] - (
                            bone2d1['x'] - pos2d13b['x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * 2,
                             bone2d1['y'] + (bone2d1['y'] - pos2dglobal2['y']),
                             (bone2d1['x'] - (bone2d1['x'] - pos2d8b[
                                 'x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * 2,
                             bone2d1['y'] + (bone2d1['y'] - pos2dglobal2['y']), pm.get_color('white'),
                             1)
                pm.draw_line((bone2d1['x'] - (
                            bone2d1['x'] - pos2d8b['x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * 2,
                             bone2d1['y'] + (bone2d1['y'] - pos2dglobal2['y']),
                             (bone2d1['x'] - (bone2d1['x'] - pos2d8b[
                                 'x']) / 2.7) + offsetesp * ofssetye * value_offset + offsetesp * offset_xafter,
                             bone2d1['y'] - (bone2d1['y'] - pos2dglobal2['y']),
                             pm.get_color('red'),
                             1)

            except:
                pass


def draw_boxes_in_game(pm, x_window, avoid_x2, avoid_x, avoid_y2, avoid_y):
    global xtrypos, three_x, boxes_c
    if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
        try:
            xpos1, ypos1 = pos2dglobal1['x'], pos2dglobal1['y']
            xpos2, ypos2 = pos2dglobal2['x'], pos2dglobal2['y']
            distancepos = math.sqrt((xpos2 - xpos1) ** 2 + (ypos2 - ypos1) ** 2)
            hypotenusepos = distancepos

            xtrypos = math.sqrt(hypotenusepos ** 2 / 4.5796)  # 10 is 1^2 + 3^2
            xtrypos = xtrypos * 1.2

            three_x = 2.14 * xtrypos
            pos2dglobal1['x'] -= xtrypos / 2
            pos2dglobal1['y'] -= three_x / 8
            pos2dglobal2['y'] -= three_x / 8
            try:
                pos2dglobal1['x'] += offsetesp
            except:
                pass
            # 310,150,250
            if boxes_visible_check % 2 == 1:
                if handle.get_spotted_by_me(ent.pawn_ptr) == 1:
                    boxes_c = pm.new_color(255, 255, 255, 255)
                else:
                    boxes_c = boxes_color
            else:
                boxes_c = boxes_color


        except:
            pass
        if 0 != x_window:
            if avoid_x2 < pos2dglobal1['x'] < avoid_x - xtrypos and avoid_y2 < pos2dglobal1[
                'y'] < avoid_y - three_x:
                pm.draw_rectangle_rounded_lines(pos2dglobal1['x'], pos2dglobal1['y'],
                                                xtrypos, three_x, boxes_roundness, 1,
                                                boxes_c, 2)
        else:
            pm.draw_rectangle_rounded_lines(pos2dglobal1['x'], pos2dglobal1['y'], xtrypos,
                                            three_x, boxes_roundness, 1, boxes_c, 2)

def main():
    if not handle.connect():
        while not handle.connect():
            print("Waiting for CS2.")
            print("Waiting for CS2..")
            print("Waiting for CS2...")
        os.system('cls')
        print("Done")
    else:
        os.system('cls')
        print("Done")
    #global ofssetye, offsetesp, offset_xafter, pos2dglobal1, pos2dglobal2, distancepos, fixforoffsetboxes_x, fixforoffsetboxes_y, numxtimed, value_offset, right_anglex, right_angley
    global current_map,sens,posbone5, posbone8, posbone13, posbone14, posbone9, posbone22, posbone25, posbone41, posbone23, posbone26, posbone1, posbone27, posbone24,posbone45,offsetesp, value_offset, offset_xafter, ofssetye, pos2d22b, pos2d25b, pos2d13b, pos2d8b, pos2d5b, pos2d9b, pos2d45b, pos2d14b, pos2d41b, pos2d23b, pos2d26b, pos2d1b, pos2d27b, pos2d24b,posglobal2, posglobal, pos2dglobal1, pos2dglobal2, distancepos, ent,viewmat,temp_proc,x_e,x_me,y_e,y_me,line_roundness,weapon_visibility,new_distance,boxes_roundness,xtrypos,boxes_color , healthnum_color,healthline_color,skeleton_color,weapon_color,teamnum,boxes_visible_check,punch,punchold,textu1,ct_mod,right_anglex,right_angley,rcs,aimbot_debug,strenght,aimbot_place,rcs_im,boxes_people,textu,load,posbufferhelp,tri_left,tri_right,tick,averagefps,teamcheck,aimpng,esppng,settingspng,boxes_ingame,three_x,radarpng,triggerpng,ofssetye,draw_game_boxes,offsetesp,drawfps,ent,list_ent,distanceforboxes,posbone_get,posaimhelp,bombscale,draw_c4,kfc_rank,kfc_teamcolor,name,ip_change,cloud_radar, coordinates_queue, textures, degree1, degreepitch, save_c4, temp_bomb, im_alive
    if cloud_radar %2==1:
        coordinates_queue = queue.Queue()


        worker_thread = threading.Thread(target=send_place_worker, args=(coordinates_queue, account_name, ip_change))
        worker_thread.daemon = True
        worker_thread.start()
# ------------------------- setting the basic constants for the program ------------------------------
    cs2_id = pm.get_process_id("cs2.exe")
    mem = pm.open_process("cs2.exe")
    module_client = pm.get_module(mem,'client.dll')["base"]
    # client_mod = handle.client_module
    # client_module = pm.get_module("cs2.exe", "client.dll")
    # view_matrix = pm.r_floats(mem, client_module + 25659360, 16)
    # print(view_matrix)
    overlay = pm.overlay_init()
    pm.gui_load_style("style\\style_jungle.txt.rgs")
    #fonts to make it more beautiful
    pm.load_font(appdata+'\\neededfiles\\OpenSans-Medium.ttf', 3)
    pm.load_font(appdata+'\\neededfiles\\RobotoSlab-Black.ttf', 2)
    #set program fps to refresh rate of monitor
    fps = pm.get_monitor_refresh_rate()
    pm.set_fps(fps)
    pm.set_window_title("menu")
    pm.set_window_icon(str(appdata+"\\neededfiles\\nightsrun_icon.png"))
    windows_temp = pm.get_window_info("Counter-Strike 2")
    width, height,width_x,width_y = windows_temp[2], windows_temp[3],windows_temp[0],windows_temp[1]
    x_wid, y_hei = width // 2, height // 2
    x_wid_gui,y_wid_gui = x_wid+width_x, y_hei+width_y
    pm.gui_fade(1)
# -----------------------------------------------------------------------------------------------------
    while pm.overlay_loop():
                sens = handle.get_sensetivity()
                # ---- loading the textures only once ----
                if load%2==1:
                    radarpng = pm.load_texture(appdata+"\\neededfiles\\radar.png")
                    triggerpng = pm.load_texture(appdata+"\\neededfiles\\trigger.png")
                    tick = pm.load_texture(appdata+"\\neededfiles\\tick.png")
                    tri_right = pm.load_texture(appdata+"\\neededfiles\\tri-right.png")
                    tri_left = pm.load_texture(appdata+"\\neededfiles\\tri-left.png")
                    ct_mod = pm.load_texture(appdata+"\\neededfiles\\ctmod.png")
                    textu1 = pm.load_texture(appdata+"\\neededfiles\\AK-47" + ".png")
                    aimpng = pm.load_texture(appdata+"\\neededfiles\\aim.png")
                    esppng = pm.load_texture(appdata+"\\neededfiles\\esp.png")
                    settingspng = pm.load_texture(appdata+"\\neededfiles\\settings.png")

                    textures = {}


                    for weapon in kfc_weapon:
                        if weapon != "temp":
                            texture = pm.load_texture(str(appdata+"\\neededfiles\\"+weapon + "_hi.png"))
                            textures[weapon] = texture
                    
                    for rank in kfc_rank:
                        texture = pm.load_texture(str(appdata+"\\neededfiles\\"+rank + ".png"))
                        textures[rank] = texture


                    print(textures)
                    time.sleep(0.3)
                    os.system('cls')
                    print("ready!")




                    load = 0
                # recoil control
                if rcs % 2 == 0:
                    rcs_control(pm)

                global boxes
                temp_proc = pm.get_window_info("Counter-Strike 2")

                # draw the fps on the left side of the screen
                if drawfps%2==0:
                    get_fps(pm)

                # open the gui with home button
                if kb.is_pressed("home"):
                    open_gui()

                viewmat = pm.r_floats(mem, module_client + OFFSETS["view_matrix"], 16)
                pm.begin_drawing()
                global menu
                entity_list = handle.get_entities()
                
                player_count = len(entity_list)

                # update cloud radar toggle
                if cloud_radar %2==1:
                    update_cloud_radar(entity_list,coordinates_queue)


                # --- tab menu with info --- just the background
                if kb.is_pressed("tab"):
                    pm.draw_rectangle_rounded(temp_proc[0]+temp_proc[2]//80, temp_proc[1]+temp_proc[3]*0.2975, temp_proc[2]//4.25, temp_proc[3]/20*(player_count+1)/1.42, 0.05, 1, pm.new_color(0,0,0,150))

                ####test for map - so the online one would change - WORKING !!!
                current_map = handle.get_current_map_name()


                for ent in entity_list:
                    #print(f"Main loop added coordinates to queue: ({x_player_p}, {y_player_p})")
                    #print_queue(coordinates_queue)
                    #print(x_player,y_player)
                    #print(f"Entity({ent.controller_ptr}): health: {handle.get_he(ent)} | team: {handle.get_team(ent)} | pos: {handle.get_position(ent)} | angle: {handle.get_eye_angles(ent)} | name: {handle.get_name(ent)}")

                    try:
                        if kb.is_pressed("tab"):
                            tab_rank_menu(pm,entity_list, textures)

                        if teamnum == 3:
                            temp_bomb = handle.get_plantedbomb()
                            find_bomber(pm)

                        else:bomb_carrier =None

                    except:

                        pass
                    try:

                        #be able to see the entire map
                        health_ent = handle.get_he(ent)
                        if handle.get_local_player_ptr() == ent.controller_ptr:
                            if health_ent == 0:
                                distanceforboxes = 99999
                                im_alive = 9
                            else:
                                distanceforboxes = new_distance
                                im_alive = 1

                    except:
                        continue

                    #print(f" * Entity({ent.controller_ptr} | health: {handle.get_he(ent)} \n | team: {handle.get_team(ent)} | pos: {handle.get_position(ent)} \n | name: {handle.get_name(ent)} | spotted: {handle.get_spotted_by_me(ent.pawn_ptr)} \n | weapon: {handle.get_weapon(ent.pawn_ptr)}")

                    #try to get observers
                    if  handle.get_local_player_ptr() == ent.controller_ptr:
                        observer = handle.observer(ent)
                        #print(handle.get_observer(ent.pawn_ptr))

                    if handle.get_lifestate(ent.pawn_ptr) != 0:
                        continue

                    if health_ent <= 0:
                        continue

                    elif handle.get_local_player_ptr() == ent.controller_ptr:
                        degree_pos = handle.get_local_eye_angles()
                        degreepitch = degree_pos[0]
                        degree1 = degree_pos[1]
                        pos_me = handle.get_position(ent)
                        x_me = pos_me[0]
                        y_me = pos_me[1]
                        teamnum = handle.get_team(ent)
                        try:
                            teamnum == handle.get_team(ent)
                        except:
                            continue
                    if teamnum == handle.get_team(ent) and teamcheck==1:
                        continue
                    else:
                        enemy_pos_temp = handle.get_position(ent)
                        x_e = enemy_pos_temp[0]
                        y_e = enemy_pos_temp[1]
                        try:
                            x_h = (x_e - x_me) * (-1)
                            y_h = ((y_e - y_me) * (-1))
                            coords_of_kfc = (x_h, y_h)
                            coords_center = (0, 0)
                        except:
                            continue

                        if degree1 < 0:
                            degree_right = (degree1 + 360)
                        else:
                            degree_right = degree1
                        if degreepitch < 0:
                            degree_right1 = (degree1 + 90)
                        else:
                            degree_right1 = degreepitch
                        dotx, doty = rotate(coords_center, coords_of_kfc, (degree_right - 90) * (-1))

                        dot_y_per = doty / 7
                        dot_x_per = dotx / 7

                        avoid_x = temp_proc[0] + temp_proc[2]
                        avoid_x2 = temp_proc[0]
                        avoid_y = temp_proc[1] + temp_proc[3]
                        avoid_y2 = temp_proc[1]
                        y_window = temp_proc[1]
                        x_window = temp_proc[0]
                        widwindow = temp_proc[2]
                        heiwindow = temp_proc[3]
                        width_mon = pm.get_screen_width()
                        height_mon = pm.get_screen_height()
                        try:
                            weapon_temp = handle.get_weapon(ent.pawn_ptr)
                        except:continue
                        try:
                            save_c4 = save_c4
                            #print(save_c4)
                        except:pass
                        try:
                            if save_c4: #saving c_4 entity when picked up
                                temp_c4 = handle.get_bomb_dropped(save_c4)
                                c4_pos = temp_c4[1]
                                c2d = world_to_screen1(c4_pos, viewmat, temp_proc)
                                c4_x=c4_pos[0]
                                c4_y = c4_pos[1]
                                try:
                                    if draw_c4 %2 ==1:
                                        if temp_c4[0] == 0 and temp_bomb[3]==False:
                                            #print(try2)
                                            distance_me = math.sqrt((x_me - c4_x) ** 2 + (
                                                    y_me - c4_y) ** 2)
                                            if distance_me < 990 and im_alive == 1:
                                                bombscale = 100 / distance_me
                                            else:
                                                bombscale = 0.1
                                            pm.draw_texture(textures['C4'], c2d['x'], c2d['y'],
                                                            pm.new_color(255,255,255,255), 0,
                                                            bombscale)
                                except:pass
                                #print(c2d)
                        except:pass
                        if radar % 2 == 1: #draw radar
                            draw_radar_func(pm,x_window,y_window,x_wid, y_hei,dot_y_per,dot_x_per,health_ent,ent)

                        try:
                            get_posglobal()
                            if trigger % 2 == 0:
                                trigger_func(pm,ent)

                            else:
                                objects_without_trigger(pm, ent)

                            if skeleton % 2 == 1:
                                get_the_rest_of_the_bones()
                        except:
                            continue

                        if aimbot % 2 == 1:
                            try:
                                aimbot_function_moved()
                            except:
                                print("aimbot_fail")
                                continue

                        if trigger % 2 == 1:
                            if kb.is_pressed(triggerbutton):
                                trigger_activated(pm,x_window,y_window,x_wid, y_hei,dot_y_per,dot_x_per,health_ent,ent,avoid_x2,widwindow,avoid_y,heiwindow,avoid_x,avoid_y2)

                        if drawesp % 2 == 1:
                            if show_weapons % 2 == 1:
                                draw_weapon(pm, ent, textures,weapon_temp,enemy_pos_temp,x_window,avoid_x2,avoid_x,avoid_y2,avoid_y)

                        if drawesp % 2 == 1:
                            if health % 2 == 1:
                                if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
                                    # print(pos1)
                                    try:

                                        xposht1, yposht1 = pos2dglobal1['x'], pos2dglobal1['y']
                                        xposht2, yposht2 = pos2dglobal2['x'], pos2dglobal2['y']
                                        distancepos = math.sqrt((xposht2 - xposht1) ** 2 + (yposht2 - yposht1) ** 2)
                                        hypotenusepos = distancepos

                                        # Use the Pythagorean theorem to find x
                                        xtrypos2 = math.sqrt(hypotenusepos ** 2 / 1)  # 10 is 1^2 + 3^2
                                        xtrypos2 = xtrypos2 * 1.2

                                        three_x2 = 2.14 * xtrypos2
                                        x_healthnum = pos2dglobal1['x'] + xtrypos2 / 5.5
                                        y_healthnum = pos2dglobal1['y'] - three_x2 / 8
                                        healthnum_c = healthnum_color
                                        healthsize = xtrypos2/8
                                        healthnum = str(health_ent)







                                    except:
                                        continue
                                    try:
                                         x_healthnum += offsetesp
                                    except:
                                        continue
                                    if 0 != x_window:
                                        if avoid_x2 < x_healthnum < avoid_x - xtrypos2 / 4.5 and avoid_y2 < y_healthnum < avoid_y - xtrypos2 / 6:
                                            pm.draw_font(2, healthnum, x_healthnum, y_healthnum, xtrypos2 / 10, 0.5,
                                                         healthnum_c)
                                    else:
                                        pm.draw_font(2, healthnum, x_healthnum, y_healthnum, xtrypos2 / 10, 1,
                                                     healthnum_c)
                                        #pm.draw_text(healthnum, x_healthnum, y_healthnum, xtrypos2 / 8, healthnum_c)



                            # ---- temp show their names - to be canged
                            if boxes_people%2==1:
                                if x_e - x_me < distanceforboxes and y_e - y_me < distanceforboxes and y_e - y_me > -distanceforboxes and x_e - x_me > -distanceforboxes:
                                    # print(pos1)
                                    try:

                                        xposht1, yposht1 = pos2dglobal1['x'], pos2dglobal1['y']
                                        xposht2, yposht2 = pos2dglobal2['x'], pos2dglobal2['y']
                                        distancepos = math.sqrt((xposht2 - xposht1) ** 2 + (yposht2 - yposht1) ** 2)
                                        hypotenusepos = distancepos

                                        #Use the Pythagorean theorem to find x
                                        xtrypos2 = math.sqrt(hypotenusepos ** 2 / 1)  # 10 is 1^2 + 3^2
                                        xtrypos2 = xtrypos2 * 1.2

                                        three_x2 = 2.14 * xtrypos2
                                        x_healthnum = pos2dglobal1['x'] - xtrypos2 /6
                                        y_healthnum = pos2dglobal1['y'] + three_x2 /2
                                        healthnum_c = healthnum_color
                                        healthnum = str(handle.get_name(ent))



                                    except:
                                        continue
                                    if 0 != x_window:
                                        if avoid_x2 < x_healthnum < avoid_x - xtrypos2 / 4.5 and avoid_y2 < y_healthnum < avoid_y - xtrypos2 / 6:
                                            pm.draw_text(healthnum, x_healthnum, y_healthnum, xtrypos2 / 10, healthnum_c)
                                    else:
                                        pm.draw_text(healthnum, x_healthnum, y_healthnum, xtrypos2 / 10, healthnum_c)


                            if health_line % 2 == 1:
                                draw_health_line(pm,x_window,avoid_x2,avoid_x,avoid_y2,avoid_y,health_ent)
                            if skeleton % 2 == 1:

                                draw_skeleton_in_game(pos2d8b,pos2d13b)


                            if boxes % 2 == 1:
                                draw_boxes_in_game(pm, x_window, avoid_x2, avoid_x, avoid_y2, avoid_y)
                if gui % 2 == 1:
                    gui_start(temp_proc)

                pm.end_drawing()

def set_window_topmost():
    window_title = "NightMatch"
    while 1:
        # Find the window by title
        hwnd = win32gui.FindWindow(None, window_title)

        if hwnd == 0:
            print(f"Window with title '{window_title}' not found.")
            return

        # Set the window position
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Ensure the window is not minimized
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

launch_mode = "secure"
#launch_mode = "dev"

def cycle_prog():
    print(1)

if launch_mode == "secure":
    login_info = read_db()
    print(login_info)
    account_name = login_info[0]
    account_password = login_info[1]
    result_of_login = account(account_name,account_password)
    cycle = threading.Thread(target=cycle_prog)
    cycle.start()
    ontop = threading.Thread(target=set_window_topmost)
    ontop.start()
    if result_of_login == 200:
        main()
    else:
        sys.exit()
if launch_mode == "dev":
    main()
















