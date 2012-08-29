import urllib.request
import sys

if (sys.argv[1] == "-i" and len(sys.argv) == 4):
	fileHandler = open (sys.argv[2], 'r')
	outputfile = sys.argv[3]
	artisturls = fileHandler.readlines()
else:
	artisturls = []
	artisturls.append(sys.argv[1])
	outputfile = sys.argv[2]

for artisturl in artisturls:
	startid = artisturl.find("/artist/")
	endid = artisturl.find("/",startid+8)
	artistid = artisturl[startid+8:endid]
	print (artistid)

	fetchalbums = urllib.request.urlopen("http://api.jamendo.com/get2/id+name/album/plain?n=all&artist_id="+artistid)
	albums = fetchalbums.readlines()
	i = 0
	albumids =  []
	albumnames = []
	for album in albums:
		album = album.decode('utf8')
		if i < len(albums)-1:
			album = album[0:album.rfind("\n")]
		album = album.split('\t')
		albumids.append(album[0])
		albumnames.append(album[1])
		print (str(i) + ": " + albumids[i] + " " +  albumnames[i])
		i += 1
	downloadlinks = []
	fileHandle = open (outputfile,'a')
	for i in range(len(albumids)):
		downloadlinks.append("http://storage-new.newjamendo.com/download/a" +
		albumids[i] +
		"/mp32/")
		redirect = urllib.request.urlopen(downloadlinks[i])
		downloadlinks[i] = redirect.url
		print (downloadlinks[i])
		fileHandle.write(downloadlinks[i] + "\n")
	fileHandle.close()
