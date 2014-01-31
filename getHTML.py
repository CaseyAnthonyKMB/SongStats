import http.client

def getHTML(baseurl, geturl):

	conn = http.client.HTTPConnection(baseurl)
	conn.request("GET", geturl)
	r1 = conn.getresponse()
	print(r1.status, r1.reason)
	htmltext = r1.read().decode("utf-8")
	conn.close()
	return htmltext