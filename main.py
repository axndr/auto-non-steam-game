from user import *
from model import *
import sys
import os
import re


"""
'\x00\x01
AppName\x00Audacity\x00\x01
Exe\x00"C:\\Program Files (x86)\\Audacity\\audacity.exe"\x00\x01
StartDir\x00"C:\\Program Files (x86)\\Audacity\\"\x00\x01
icon\x00\x00\x01
ShortcutPath\x00\x00\x01
LaunchOptions\x00\x00\x02
IsHidden\x00\x00\x00\x00\x00\x02
AllowDesktopConfig\x00\x01\x00\x00\x00\x02
AllowOverlay\x00\x01\x00\x00\x00\x02
OpenVR\x00\x00\x00\x00\x00\x02
Devkit\x00\x00\x00\x00\x00\x01
DevkitGameID\x00\x00\x02
LastPlayTime\x00_\x1d¸_\x00
tags\x00'

"""

if __name__ == '__main__':
    steam_obj = Steam("C:\\Program Files (x86)\\Steam\\userdata")
    localusercontext_obj = LocalUserContext(steam_obj, 76561197993493993)
    alex = User(localusercontext_obj.steam, localusercontext_obj.user_id)

    pass
