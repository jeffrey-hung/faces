#!/usr/bin/python
import os
import sys
import vlc

import time
from PyQt5.QtWidgets import QApplication, QFrame, QMacCocoaViewContainer

Instance = vlc.Instance('--fullscreen')
player = Instance.media_player_new()
video = Instance.media_new("test.mp4")
video.get_mrl()
player.set_media(video)




vlcApp =QApplication(sys.argv)
vlcWidget = QFrame()
vlcWidget.resize(700,700)
vlcWidget.show()
player.set_nsobject(int(vlcWidget.winId()))

player.play()

time.sleep(5)