import http.client
import re

baseurl = "www.azlyrics.com"

conn = http.client.HTTPConnection(baseurl)
conn.request("GET", "/b/brandnew.html")
r1 = conn.getresponse()
print(r1.status, r1.reason)
htmltext = r1.read().decode("utf-8")

#print (data1)
# file = open("sample.html", "w")
# file.write(data1.decode("utf-8"))
# file.close()

songlist = re.findall('{s:"(.+)", h:"(.+)", c', htmltext)
urllist = []
for song in songlist:
	urllist.append((song[0], baseurl + song[1][2:]))
print (urllist)
