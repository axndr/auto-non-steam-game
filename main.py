from user import *
from model import *
import sys
import os
import re


if __name__ == '__main__':
    steam_obj = Steam("C:\\Program Files (x86)\\Steam\\userdata")
    localusercontext_obj = LocalUserContext(steam_obj, 76561197993493993)
    alex = User(localusercontext_obj.steam, localusercontext_obj.user_id)
    new_shortcut = Shortcut(
        AppName='Breach',
        Exe=r"C:\Games\Into.the.Breach.v1.2.24\Breach.exe",
        StartDir=r"C:\Games\Into.the.Breach.v1.2.24"
    )
    alex.shortcuts.append(new_shortcut)
    alex.save_shortcuts()
