import datetime

from pyMeow.pyMeow import vec3
import numpy as nump
import re
from offsets import *
from client import *
then = None

##taking the offsets from client.py and offsets.py
OFFSETS = {
    "entity_list"            : client_dll.dwEntityList,
    "global_vars"            : client_dll.dwGlobalVars,
    "local_player_controller": client_dll.dwLocalPlayerController,
    "view_angles"            : client_dll.dwViewAngles,
    "view_matrix"            : client_dll.dwViewMatrix ,
    "dwLocalPlayerPawn"      : client_dll.dwLocalPlayerPawn,
    "dwPlantedC4"            : client_dll.dwPlantedC4,

    "client"                 : {
        "C_BasePlayerPawn": {
            "m_pWeaponServices": C_BasePlayerPawn.m_pWeaponServices,
             "m_vOldOrigin": C_BasePlayerPawn.m_vOldOrigin,
            "m_hController":C_BasePlayerPawn.m_hController,
            "m_pObserverServices":C_BasePlayerPawn.m_pObserverServices,
         },
        "C_BaseEntity": {
             "m_iTeamNum": C_BaseEntity.m_iTeamNum,
            "m_iHealth": C_BaseEntity.m_iHealth,
            "m_fFlags":C_BaseEntity.m_fFlags,
            "m_hOwnerEntity" : C_BaseEntity.m_hOwnerEntity
         },
        "CCSPlayerController": {
            "m_szCrosshairCodes":CCSPlayerController.m_szCrosshairCodes,
             "m_iPawnHealth": CCSPlayerController.m_iPawnHealth,
             "m_hPlayerPawn": CCSPlayerController.m_hPlayerPawn,
            "m_hPawn":CBasePlayerController.m_hPawn,
            "m_iCompetitiveRanking":CCSPlayerController.m_iCompetitiveRanking,
            "m_iCompTeammateColor":CCSPlayerController.m_iCompTeammateColor,
            "m_iCompetitiveWins":CCSPlayerController.m_iCompetitiveWins,
         },
        "CBasePlayerController": {
             "m_iszPlayerName": CBasePlayerController.m_iszPlayerName,
            "m_nTickBase":CBasePlayerController.m_nTickBase
         },
        "C_CSPlayerPawnBase": {
            "m_entitySpottedState": C_CSPlayerPawn.m_entitySpottedState,
            "m_iShotsFired":C_CSPlayerPawn.m_iShotsFired,
            #"m_pClippingWeapon": C_CSPlayerPawnBase.m_pClippingWeapon
         },
        "CBaseEntity": {
            "m_iTeamNum": C_BaseEntity.m_iTeamNum,
            "m_pGameSceneNode": C_BaseEntity.m_pGameSceneNode,
            "m_lifeState": C_BaseEntity.m_lifeState,
         },
         "CSkeletonInstance": {
             "m_modelState": CSkeletonInstance.m_modelState,  # 0x160 - 0x390
         },
         "CModelState": {
             "m_pBoneArray": 0x80,  # 0x0 - 0xA0
         },
        "CPlayer_WeaponServices": {
            "m_hActiveWeapon": CPlayer_WeaponServices.m_hActiveWeapon,
            "m_iAmmo": CPlayer_WeaponServices.m_iAmmo,
            "m_hMyWeapons":CPlayer_WeaponServices.m_hMyWeapons
        },
        "C_EconItemView":{
            "m_iItemDefinitionIndex": C_EconItemView.m_iItemDefinitionIndex

        },
        "CCSObserver_ObserverServices": {
            #"m_hLastObserverTarget":CCSObserver_ObserverServices.m_hLastObserverTarget
        },
        "EntitySpottedState_t": {
            "m_bSpotted": EntitySpottedState_t.m_bSpotted,
            "m_bSpottedByMask":EntitySpottedState_t.m_bSpottedByMask
        },
        "C_CSPlayerPawn":{
            "m_aimPunchAngle":C_CSPlayerPawn.m_aimPunchAngle,
            "m_pClippingWeapon": C_CSPlayerPawn.m_pClippingWeapon,
            "m_iIDEntIndex":C_CSPlayerPawn.m_iIDEntIndex,
            "m_angEyeAngles": C_CSPlayerPawn.m_angEyeAngles,
        },
        "CPlayer_ObserverServices":{
            "m_hObserverTarget":CPlayer_ObserverServices.m_hObserverTarget
        },
        "C_EconEntity":{
            "m_AttributeManager":C_EconEntity.m_AttributeManager
        },
        "C_AttributeContainer":{
            "C_AttributeContainer":0x1BA,
            "m_Item":C_AttributeContainer.m_Item
        },
        "C_PlantedC4":{
            "m_bC4Activated":C_PlantedC4.m_bC4Activated,
            "m_flDefuseCountDown":C_PlantedC4.m_flDefuseCountDown,
            "m_flC4Blow":C_PlantedC4.m_flC4Blow,
            "m_bBeingDefused":C_PlantedC4.m_bBeingDefused

        },
        "CGameSceneNode":{
            "m_vecAbsOrigin":CGameSceneNode.m_vecOrigin
        },
        "C_SceneEntity":{
            "m_hOwner":C_SceneEntity.m_hOwner
        },
        "CGameSceneNodeHandle":{
            "m_hOwner":CGameSceneNodeHandle.m_hOwner
        },
        "C_CSWeaponBase":{
            #"m_iState":C_CSWeaponBase.m_iState
        }




    }
}






import pymem
import pymem.process
from typing import Any
from Entity import *
import binascii

# define a class to handle memory reading
class Memory:
    def __init__(self):
        self.handle: Any = None
        self.client_module: int = 0
        self.engine_module: int = 0
        self.connect()
    def connect(self) -> bool:
        try:
            self.handle = pymem.Pymem("cs2.exe")
            self.client_module = pymem.process.module_from_name(self.handle.process_handle, "client.dll").lpBaseOfDll
            self.engine_module = pymem.process.module_from_name(self.handle.process_handle, "engine2.dll").lpBaseOfDll
            return True
        except:  # because pymem could give an error somethimes
            return False

    def get_pointer(self, address: int) -> int:
        # 64 bit pointer
        try:
            return self.handle.read_ulonglong(address)
        except pymem.exception.MemoryReadError:
            return 0

    def read_int(self, address: int) -> int:
        try:
            return self.handle.read_int(address)
        except pymem.exception.MemoryReadError:
            return 0

    def read_float(self, address: int) -> float:
        try:
            return self.handle.read_float(address)
        except pymem.exception.MemoryReadError:
            return 0

    def read_float16(self, address: bytes):
        data = self.handle.read_bytes(self.client_module + address, 2)
        float16_value = nump.frombuffer(data, dtype=nump.float16)[0]
        float16_array = nump.array([float16_value], dtype=nump.float16)
        float16_value1 = nump.float16(float16_value)
        matrix = nump.full((4, 4), float16_value)
        return matrix

    def read_dword(self, address):
        buffer = self.handle.read_bytes(address, 4)
        return int.from_bytes(buffer, byteorder='little') #########

    def read_uint64(self, address):
        buffer = self.handle.read_bytes(address, 8)
        return int.from_bytes(buffer, byteorder='little', signed=False)

    def read_uint32(self, address):
        buffer = self.handle.read_bytes(address, 4)
        return int.from_bytes(buffer, byteorder='little', signed=False)

    def read_uint16(self, address):
        buffer = self.handle.read_bytes(address, 2)
        return int.from_bytes(buffer, byteorder='little', signed=False)

    def read_uint8(self, address):
        buffer = self.handle.read_bytes(address, 1)
        return int.from_bytes(buffer, byteorder='little', signed=False)

    def read_vec3(self, address: int) -> tuple:
        try:
            return self.handle.read_float(address), self.handle.read_float(address + 4), self.handle.read_float(
                address + 8)
        except pymem.exception.MemoryReadError:
            return 0, 0, 0

    def read_vec2(self,address:int) ->tuple:
        try:
            return self.handle.read_float(address), self.handle.read_float(address + 4)
        except pymem.exception.MemoryReadError:
            return 0, 0
    def read_string(self, address: int, size: int) -> str:
        try:
            return self.handle.read_string(address, size)
        except pymem.exception.MemoryReadError:
            return ""

    def read_raw(self, address: int, size: int) -> bytes:
        try:
            return self.handle.read_bytes(address, size)
        except pymem.exception.MemoryReadError:
            return b''

    def read_bool(self, address):
        try:
            # Read a single byte from the specified memory address
            value = self.read_raw(address, 1)

            # Interpret the byte as a boolean (0=False, 1=True)
            return bool(value[0])
        except pymem.exception.MemoryReadError:
            # Handle any exceptions that may occur during the read operation
            print("Failed to read the boolean value.")
            return None

    def get_current_map_name(self) -> str:
        _globals = self.get_pointer(self.client_module + OFFSETS["global_vars"])
        if _globals == 0:
            return "none"
        map_name_ptr = self.get_pointer(_globals + 384)
        return self.read_string(map_name_ptr,64)

    def get_local_player_ptr(self) -> int:
        return self.get_pointer(self.client_module + OFFSETS["local_player_controller"])

    def get_local_player_pawn(self) -> int:
        return self.get_pointer(self.client_module+OFFSETS['dwLocalPlayerPawn'])

    def get_position(self, entity: Entity) -> tuple:
        return self.read_vec3(entity.pawn_ptr + OFFSETS["client"]["C_BasePlayerPawn"]["m_vOldOrigin"])

    def get_team(self, entity: Entity) -> int:
        return self.read_int(entity.pawn_ptr + OFFSETS["client"]["C_BaseEntity"]["m_iTeamNum"])

    def get_he(self, entity: Entity) -> int:
        #print(entity.pawn_ptr)
        return self.read_int(entity.pawn_ptr + OFFSETS["client"]["C_BaseEntity"]["m_iHealth"])

    def get_health(self, entity: Entity) -> int:
        #print(entity.controller_ptr + OFFSETS["client"]["CCSPlayerController"]["m_iPawnHealth"])
        return self.read_int(entity.controller_ptr + OFFSETS["client"]["CCSPlayerController"]["m_iPawnHealth"])

    def get_lifestate(self,player):
        return self.read_uint8(player + OFFSETS['client']['CBaseEntity']['m_lifeState'])

    def get_weapon(self,player) -> int:
        h = self.read_uint64(player + OFFSETS['client']['C_CSPlayerPawn']['m_pClippingWeapon'])
        current_weapon = self.read_uint16(h + OFFSETS['client']['C_AttributeContainer']['C_AttributeContainer'] + OFFSETS['client']['C_AttributeContainer']['m_Item'] + OFFSETS['client']['C_EconEntity']['m_AttributeManager'])
        list = [current_weapon,h]
        return list


    def get_rank(self, entity: Entity) -> int:
        return self.read_int(entity.controller_ptr + OFFSETS['client']['CCSPlayerController']['m_iCompetitiveRanking'])
    def get_color_mm(self, entity: Entity) -> int:
        return self.read_int(entity.controller_ptr + OFFSETS['client']['CCSPlayerController']['m_iCompTeammateColor'])
    def get_wins(self, entity: Entity) -> int:
        return self.read_int(entity.controller_ptr + OFFSETS['client']['CCSPlayerController']['m_iCompetitiveWins'])

    

    def get_bomb_dropped(self,bomb):
        o = self.get_pointer(bomb)
        ol = self.get_pointer(bomb+OFFSETS['client']['C_CSWeaponBase']['m_iState'])
        p = self.get_pointer(bomb+OFFSETS["client"]["CBaseEntity"]["m_pGameSceneNode"])
        l = self.read_vec3(p+OFFSETS["client"]["CGameSceneNode"]["m_vecAbsOrigin"])
        list = [ol,l]
        return list

    def observer(self, entity: Entity):
        observer = self.get_pointer(self.get_pointer(entity.controller_ptr+0x7F0))
        return observer

    def get_observer(self, player) -> tuple:
        #h = self.read_int(self.get_pointer(self.client_module+client_dll.dwGameEntitySystem)+client_dll.dwGameEntitySystem_getHighestEntityIndex)
        #self.read_vec3(player + 0x120C)
        p = self.get_pointer(self.get_local_player_pawn())
        skeleton_instance = self.get_pointer(player + OFFSETS["client"]["CBaseEntity"]["m_pGameSceneNode"])
        pos = self.read_vec3(skeleton_instance + 0x80)
        pos2 = self.read_vec3(player+0xC48)
        list = [pos[0]+pos2[0],pos[1]+pos2[1],pos[2]+pos2[2]]
        return list

    def get_sensetivity(self):
        return self.read_float(self.get_pointer(self.client_module+client_dll.dwSensitivity)+client_dll.dwSensitivity_sensitivity)





    def get_plantedbomb(self):
        global then
        bomb = self.read_bool(self.client_module+OFFSETS['dwPlantedC4']-0x8)
        if bomb:
            if then == None:
                then = datetime.datetime.now()
            bombplace = self.get_pointer(self.get_pointer(self.client_module + OFFSETS['dwPlantedC4']))
            time = int(40-(datetime.datetime.now()-then).total_seconds())
            defu = self.read_bool(bombplace + OFFSETS["client"]["C_PlantedC4"]["m_bBeingDefused"])
            cnode = self.get_pointer(bombplace+OFFSETS["client"]["CBaseEntity"]["m_pGameSceneNode"])
            c4origin = self.read_vec3(cnode+OFFSETS["client"]["CGameSceneNode"]["m_vecAbsOrigin"])
            list = [c4origin,time,defu,bomb]
        else:
            then = None
            list = [None,None,None,bomb]
        return list

    # get ammo amount
    def get_ammo(self, entity: Entity) -> int:
        return self.read_int(entity.pawn_ptr + OFFSETS["client"]["CPlayer_WeaponServices"]["m_iAmmo"],)

    # get the name of the player
    def get_name(self, entity: Entity) -> str:
        return self.read_string(entity.controller_ptr + OFFSETS["client"]["CBasePlayerController"]["m_iszPlayerName"],
                                256)
    # get my eye position
    def get_local_eye_angles(self) -> tuple:
        return self.read_vec3(self.client_module + OFFSETS["view_angles"])

    # get the position that somene is looking at
    def get_eye_angles(self, entity: Entity) -> tuple:
        return self.read_vec3(entity.pawn_ptr + OFFSETS["client"]["C_CSPlayerPawn"]["m_angEyeAngles"])

    def get_spotted(self,player):
        spotted = self.read_int(player+OFFSETS['client']["C_CSPlayerPawnBase"]["m_entitySpottedState"]+OFFSETS['client']["EntitySpottedState_t"]["m_bSpotted"])
        return spotted
    #get the offset of punch after shooting
    def get_punch_angle(self,local):
        punch = self.read_vec2(local + OFFSETS['client']['C_CSPlayerPawn']['m_aimPunchAngle'])
        return punch
    # get if the player is spotted by me
    def get_spotted_by_me(self,player):
        spotted_by_me = self.read_int(player + OFFSETS['client']["C_CSPlayerPawnBase"]["m_entitySpottedState"] +
                                OFFSETS['client']["EntitySpottedState_t"]["m_bSpottedByMask"])
        return spotted_by_me
    # count shots fired
    def get_shotsfired(self,player):
        fired = self.read_int((player+OFFSETS['client']['C_CSPlayerPawnBase']['m_iShotsFired']))
        return fired

    #getting the spectator list
    def get_spectators(self,player): #not working
        spec0 = self.read_int(player+OFFSETS['client']['CCSPlayerController']['m_hPawn'])
        spec = self.read_int((spec0+(self.client_module+OFFSETS["entity_list"]+((OFFSETS['client']['CPlayer_ObserverServices']['m_hObserverTarget']&0xFFF)))))
        spec1 = self.read_int(spec+OFFSETS['client']['C_BasePlayerPawn']['m_hController'])
        return spec1

    ## get specific bone

    def get_bone_position(self, entity: Entity, bone_id: int) -> vec3:
        skeleton_instance = self.get_pointer(entity.pawn_ptr + OFFSETS["client"]["CBaseEntity"]["m_pGameSceneNode"])
        bone_array_ptr = self.get_pointer(skeleton_instance + OFFSETS["client"]["CSkeletonInstance"]["m_modelState"] + OFFSETS["client"]["CModelState"]["m_pBoneArray"])
        result = self.read_vec3(bone_array_ptr + bone_id * 32)
        return result

    ## get all the bones in a list
    def get_more_bones(self, entity: Entity, bone_id: list) -> vec3:
        result = []
        skeleton_instance = self.get_pointer(entity.pawn_ptr + OFFSETS["client"]["CBaseEntity"]["m_pGameSceneNode"])
        bone_array_ptr = self.get_pointer(skeleton_instance + OFFSETS["client"]["CSkeletonInstance"]["m_modelState"] + OFFSETS["client"]["CModelState"]["m_pBoneArray"])
        for bone in bone_id:
            result.append(self.read_vec3(bone_array_ptr + bone * 32))
        return result

    #get player state to implenment bhop - not really used anymore
    def bhop(self,player):
        state = self.read_int(player+OFFSETS["client"]["C_BaseEntity"]["m_fFlags"])
        vel = self.read_vec3(player+0x3CC)
        if state == 65664:
            playerstate = "jump"
        elif state == 65667:
            playerstate = "crouch"
        elif state == 65665:
            playerstate = "walking"
        else:
            playerstate = "uknown"
        return playerstate,vel

    ## get spectators - work in progress
    def get_spectators_team(self,entity: Entity):
        spec0 = self.get_pointer(entity.pawn_ptr + (OFFSETS['client']['C_BasePlayerPawn']['m_pObserverServices']))
        spec2 = self.read_int(spec0+OFFSETS['client']['CPlayer_ObserverServices']['m_hObserverTarget'])
        spec = self.read_int((spec0 + (self.client_module + OFFSETS["entity_list"] + ((OFFSETS['client']['C_BasePlayerPawn']['m_pObserverServices'] & 0xFFF)))))
        spec1 = self.read_int(spec + OFFSETS['client']['C_BasePlayerPawn']['m_hController'])
        return spec2

    ## function to get all the entities in the game and return a list of Entity objects (from player one to player 64 (max players in cs2))
    def get_entities(self) -> list:
        ent_list: list = []
        for i in range(1, 64):
            g_dw_ent_list = self.get_pointer(self.client_module + OFFSETS["entity_list"])
            #print(g_dw_ent_list)
            if g_dw_ent_list == 0:
                continue

            list_entry_ptr = self.get_pointer(g_dw_ent_list + (8 * (i & 0x7FFF) >> 9) + 16)
            if list_entry_ptr == 0:
                continue

            controller_ptr = self.get_pointer(list_entry_ptr + 0x70 * (i & 0x1FF))
            if controller_ptr == 0:
                continue

            controller_pawn_ptr = self.get_pointer(
                controller_ptr + OFFSETS["client"]["CCSPlayerController"]["m_hPlayerPawn"])
            if controller_pawn_ptr == 0:
                continue

            list_entry_ptr = self.get_pointer(g_dw_ent_list + 0x8 * ((controller_pawn_ptr & 0x7FFF) >> 9) + 16)
            if list_entry_ptr == 0:
                continue

            pawn_ptr = self.get_pointer(list_entry_ptr + 0x70 * (controller_pawn_ptr & 0x1FF))
            if pawn_ptr == 0:
                continue

            ent_list.append(Entity(controller_ptr=controller_ptr, pawn_ptr=pawn_ptr))
        return ent_list

