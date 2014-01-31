import re
from getHTML import getHTML
from getLyrics import getLyrics
import time

#band name and base url
baseurl = "www.azlyrics.com"
bandname = "Brand New"

#create get url from band name
geturl= "/" + bandname[0].lower() + "/" + bandname.lower().replace( " ", "") + ".html"

#get html text
htmltext = getHTML(baseurl, geturl)

#parse song urls from html
songlist = re.findall('{s:"(.+)", h:"(.+)", c', htmltext)

#create list of tuples with song name and get url
urllist = []
for song in songlist:
	urllist.append((song[0], song[1][2:]))
#print (urllist)

songlist = []
#get html text for all songs
for  url in urllist:

	songhtml = getHTML(baseurl, url[1])

	#get lyrics from song html text
	songlist.append((url[0], getLyrics(songhtml)))
	time.sleep(1)
	
	
for song in songlist:
	filename = "brandnew/"+song[0].replace("/","")+".txt"
	file = open(filename.replace(" ", ""), "w")
	file.write(song[1])
	file.close()

