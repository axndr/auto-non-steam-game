import collections

x00 = u'\x00'
x01 = u'\x01'


class Shortcut:
    def __init__(self, AppName, Exe, StartDir, ShortcutPath='', LaunchOptions='',
                 DevkitGameID='', LastPlayTime=x00 + x00 + x00 + x00, tags=[], icon='', IsHidden=x00,
                 AllowDesktopConfig=x00,
                 AllowOverlay=x00, OpenVR=x00, Devkit=x00):
        self.AppName = AppName
        self.Exe = Exe
        self.StartDir = StartDir
        self.icon = icon
        self.ShortcutPath = ShortcutPath
        self.LaunchOptions = LaunchOptions
        self.IsHidden = IsHidden
        self.AllowDesktopConfig = AllowDesktopConfig
        self.AllowOverlay = AllowOverlay
        self.OpenVR = OpenVR
        self.Devkit = Devkit
        self.DevkitGameID = DevkitGameID
        self.LastPlayTime = LastPlayTime
        self.tags = tags


# Represents a Steam installation. Since we don't really care about where the
# actual guts of Steam are located, the only property on this object is the
# location of the userdata directory (much more interesting).
Steam = collections.namedtuple('Steam', [
    'userdata_directory',
])

# A simple composite object that encapsulates a local steam installation
# with a user id. Since basically everything that you would want pysteam to do
# is scoped within a single user on the system (set custom images, add/remove
# shortcuts, etc), most functions take this as a parameter so they dont need to
# take both a Steam installation and a user id.
LocalUserContext = collections.namedtuple('LocalUserContext', [
    'steam',
    'user_id',
])
