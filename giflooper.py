#!/usr/bin/env python3

import os
from os import system
from os import listdir
from omxplayer.player import OMXPlayer
from pathlib import Path
from time import sleep

folder = 'media/'

vidType = 'mp4'

files = os.listdir(folder)

vids = []

for name in files:
	if vidType in name:
		vids.append(name)

print(vids)


#loop all videos in the folder

myPath = folder + vids[0]
player = OMXPlayer(myPath, args=['--layer',layer,'--blank'])

while True:
	for v in range(len(vids)):
		myPath = folder + vids[v]
		player.load(myPath)
		while True:
			try:
				player.is_playing()
			except:
				break;
