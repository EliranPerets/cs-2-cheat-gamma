# cs-2-cheat-gamma
So this is an external hack to cs 2, which uses python and nim build with pymeow and many other repositories
## created by Eliran Perets 
<details closed><summary> included files - structure: </summary>
│   client.py
        
│   Entity.py

│   firstlaunch.py

│   ip_update.py

│   main.py

│   Memory.py

│   offsets.py

│   rcs..py

│   start.lnk

│   update offsets.lnk

│

├───automation_update_the_offsets

│       update-the-offsets.py

│

├───db - on the server

│   │   asusdb.py

│   │   commands.txt

│   │

│   └───templates

│       │   1.html

│       │   account.html

│       │   add_account.html

│       │   index.html

│       │   login.html

│       │   market.html

│       │   radar - Copy.html

│       │   radar.html

│       │   register.html

│       │

│       └───radars

│               cs_agency.png

│               cs_italy.png

│               cs_office.png

│               de_ancient.png

│               de_anubis.png

│               de_dust2.png

│               de_grail.png

│               de_inferno.png

│               de_jura.png

│               de_mills.png

│               de_mirage.png

│               de_nuke.png

│               de_overpass.png

│               de_thera.png

│               de_train.png

│               de_vertigo.png

│

├───json converter to py

│   │   client.py

│   │   client_dll.json

│   │   json_convert_V3.py

│   │   offsets.json

│   │   offsets.py

│   │

│   ├───bak

│   │       json_convert_V3.py

│   │

│   └───dumper

│       │   cs2-dumper.exe

│       │   cs2-dumper.log

│       │   json-dumper.exe.lnk

│       │

│       └───output

│               animationsystem_dll.json

│               buttons.json

│               engine2_dll.json

│               host_dll.json

│               info.json

│               interfaces.json

│               materialsystem2_dll.json

│               networksystem_dll.json

│               panorama_dll.json

│               particles_dll.json

│               pulse_system_dll.json

│               rendersystemdx11_dll.json

│               resourcesystem_dll.json

│               scenesystem_dll.json

│               schemasystem_dll.json

│               server_dll.json

│               soundsystem_dll.json

│               steamaudio_dll.json

│               vphysics2_dll.json

│               worldrenderer_dll.json

│

└───needed files or repositories

        needed repositories.txt
      
        neededfiles.zip
       
        pyM.zip
</details>

## So how to use it?
### Make sure the offsets are up to date, can be updated by:

1. run the game CS2.exe
2. run `update offsets` shortcut
   
### So how to set it up?

1. change the ip in `ip_update.py` to the ip you will be using as a server
2. on the server create a `database` folder in `/home/{user}`
3. put the file `asusdb.py` and the folder `templates` inside the database folder created
4. compile `NightMatch.py` to exe without console using auto-py-to-exe and put it in `/home/{user}` folder
5. compile `main.py` to exe using auto-py-to-exe without console
6. put `main.exe` into the `neededfiles.zip`
7. put the `neededfiles.zip` into the `/home/{user}` folder
8. log in into ssh : `ssh {username}@{ip}`
9. open `asusdb.py` with interprenter and inside change the `ALLOWED_IPS = ['192.168.50.125', '192.168.50.44', '192.168.50.1']` to your local Ip adress
10. now you can run the `asusdb.py` in the background using :

   ```sh
   nohup python3 /home/{username}/database/asusdb.py > /home/{username}/database/log.log 2>&1 &
   ```

### How to run it after setting it up? 
1.go to the `{ip adress}:2096/add_profile` and create an account for yourself
2. go to the `{ip adress}:2096` via google and log in to your account
3. download the file `NightMatch.exe`
4. run it
5. log in in the `NightMatch.exe`
6. press start and wait till the program will download the cheat and the necessary files
7. start CS2.exe
