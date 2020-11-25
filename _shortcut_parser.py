import sys
import os
import re
from model import Shortcut

x00 = u'\x00'
x01 = u'\x01'
x08 = u'\x08'
x0a = u'\x0a'


def parse_tags(string):
    tags = []
    pattern = '(?:\u0001[0-9]+\u0000)(.+?)\u0000'
    regex = re.findall(pattern, string)
    if regex:
        for ele in regex:
            tags.append(ele)
    return tags


def parse_bool(string):
    if string == x00:
        return False
    elif string == x01:
        return True
    else:
        raise ValueError('parse_bool() was not given valid boolean.')


def match_contents(string):
    # r'LastPlayTime\u0000(.*)\u0001' \
    # r'£yµ_\u0000(.*)\u0001' \
    pattern = r'\u0000\u0001' \
              r'AppName\u0000(.*)\u0000\u0001' \
              r'Exe\u0000(.*)\u0000\u0001' \
              r'StartDir\u0000(.*)\u0000\u0001' \
              r'icon\u0000(.*)\u0000\u0001' \
              r'ShortcutPath\u0000(.*)\u0000\u0001' \
              r'LaunchOptions\u0000(.*)\u0000\u0002' \
              r'IsHidden\u0000([\u0000\u0001])\u0000\u0000\u0000\u0002' \
              r'AllowDesktopConfig\u0000([\u0000\u0001])\u0000\u0000\u0000\u0002' \
              r'AllowOverlay\u0000([\u0000\u0001])\u0000\u0000\u0000\u0002' \
              r'OpenVR\u0000([\u0000\u0001])\u0000\u0000\u0000\u0002' \
              r'Devkit\u0000([\u0000\u0001])\u0000\u0000\u0000\u0001' \
              r'DevkitGameID\u0000(.*)\u0000\u0002' \
              r'LastPlayTime\u0000(.*)\u0000' \
              r'tags\u0000(.*)'
    regex = re.match(pattern, string)

    return Shortcut(
        AppName=regex.groups()[0],
        Exe=regex.groups()[1],
        StartDir=regex.groups()[2],
        icon=regex.groups()[3],
        ShortcutPath=regex.groups()[4],
        LaunchOptions=regex.groups()[5],
        IsHidden=regex.groups()[6],
        AllowDesktopConfig=regex.groups()[7],
        AllowOverlay=regex.groups()[8],
        OpenVR=regex.groups()[9],
        Devkit=regex.groups()[10],
        DevkitGameID=regex.groups()[11],
        # TODO: fix LastPlayTime
        LastPlayTime=regex.groups()[12],
        tags=parse_tags(regex.groups()[13]),
    )


class ShortcutParser(object):
    def parse(self, path, require_exists=False):
        if not os.path.exists(path):
            if not require_exists:
                return []
            raise IOError("Shortcuts file '%s' does not exist" % path)

        file_contents = open(path, "r").read()
        pattern = '(?:' + x00 + r')([0-9]+)(.+?)(?:' + x08 + x08 + ')'
        matches = re.findall(pattern, file_contents)
        shortcuts = []
        for match in matches:
            shortcuts.append(match_contents(match[1]))

        return shortcuts
