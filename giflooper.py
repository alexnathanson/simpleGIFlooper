#!/usr/bin/env python3

import os
from os import system
from os import listdir
from omxplayer.player import OMXPlayer
from pathlib import path
from time import sleep

folder = 'media'

vidType = 'mp4'

files = os.listdir(path)

vids = []

for name in files:
	if vidType in name:
		vids.append(name)

print(vids)


#loop all videos in the folder

while True:
	for v in range(len(vids)):
		myPath = folder + vides[v]
		if v% 2 == 0:
			layer = 1
		else:
			layer = 2
		print layer
		player = OMXPlayer(myPath, args=['--layer',layer,'--blank'])
		#print(player.isplayer())
		tryThis= True
		while tryThis:
			try:
				player.is_playing()
			except:
				tryThis=False
