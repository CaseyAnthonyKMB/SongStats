import re

def getLyrics(songhtml):
	
	#print(songhtml)
	songarray = re.findall('([\w ]+)<br />', songhtml)
	songtext = ''
	for line in songarray:
		songtext = songtext + line + " "
	
	return songtext
