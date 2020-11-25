x00 = u'\x00'
x01 = u'\x01'
x08 = u'\x08'
x0a = u'\x0a'


class ShortcutGenerator(object):

    def to_string(self, shortcuts):
        """
        Fill with the first "shortcuts" section and the two x08 characters at the end of files.
        Pass shortcuts to
        :param shortcuts:
        :return:
        """
        return f'{x00}shortcuts{x00}{self.generate_array_string(shortcuts)}{x08}{x08}'

    def generate_array_string(self, shortcuts):
        string = ""
        for index, value in enumerate(shortcuts):
            string += x00 + str(index) + x00 + self.generate_shortcut_string(value)
        return string

    def generate_shortcut_string(self, shortcut):
        string = f'\u0001' \
                 f'AppName\u0000{shortcut.AppName}\u0000\u0001' \
                 f'Exe\u0000{shortcut.Exe}\u0000\u0001' \
                 f'StartDir\u0000{shortcut.StartDir}\u0000\u0001' \
                 f'icon\u0000{shortcut.icon}\u0000\u0001' \
                 f'ShortcutPath\u0000{shortcut.ShortcutPath}\u0000\u0001' \
                 f'LaunchOptions\u0000{shortcut.LaunchOptions}\u0000\u0002' \
                 f'IsHidden\u0000{shortcut.IsHidden}\u0000\u0000\u0000\u0002' \
                 f'AllowDesktopConfig\u0000{shortcut.AllowDesktopConfig}\u0000\u0000\u0000\u0002' \
                 f'AllowOverlay\u0000{shortcut.AllowOverlay}\u0000\u0000\u0000\u0002' \
                 f'OpenVR\u0000{shortcut.OpenVR}\u0000\u0000\u0000\u0002' \
                 f'Devkit\u0000{shortcut.Devkit}\u0000\u0000\u0000\u0001' \
                 f'DevkitGameID\u0000{shortcut.DevkitGameID}\u0000\u0002' \
                 f'LastPlayTime\u0000{shortcut.LastPlayTime}\u0000'
        string += self.generate_tags_string(shortcut.tags)
        string += x08 + x08
        return string

    def generate_tags_string(self, tags):
        string = "tags" + x00
        string += self.generate_tag_array_string(tags)
        return string

    def generate_tag_array_string(self, tags):
        string = ""
        for index, value in enumerate(tags):
            string += x01 + str(index) + x00 + value + x00
        return string
