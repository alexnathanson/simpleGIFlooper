from os import system
from os import listdir


system('convert -delay 10 -loop 0 image*.jpg test.gif')

path = 'media'

vidType = 'mp4'

files = os.listdir(path)

vids = []

for name in files:
	if vidType in name:
		vids.append(name)

print(vids)