#python2 get all videos from a playlist
import urllib
import json
import pafy
playListId = "PL81IOJraanDKweCZeg87h-YrI62zNcQaa" #Nima Onta music list
playListId = "UUXIyz409s7bNWVcM-vjfdVA" #majestic uploads
key = "Your Google API Key here"
maxResults = 50
url = "https://www.googleapis.com/youtube/v3/playlistItems?part=snippet%2C+id&maxResults="+str(maxResults)+"&playlistId="+playListId+"&key="+key
response = urllib.urlopen(url)
data = json.loads(response.read())
pos = 0
x = 0
last = data["pageInfo"]["totalResults"]-1
currentLast = 0
playListSize = 0

print last
while(pos != last):

	#print link
	vidUrl = "https://www.youtube.com/watch?v="+data["items"][x]["snippet"]["resourceId"]["videoId"]
	print str(pos)+": "+ vidUrl
	#try exception in case pafy cant get the data
	#for example if the video isnt available in your country
	try:
		video = pafy.new(vidUrl)
		audio = video.getbestaudio()
		playListSize = playListSize + (audio.get_filesize()*10**-9)
		#to the power of 10^-6 so we get the total size in MB
		#to the power of 10^-9 so we get the total size in GB
	except:
		print("Oops! Something went wrong with this video")

	pos = data["items"][x]["snippet"]["position"]
	x = x+1
	if(x == maxResults):
		x = 0
		#calc length of items in json
		currentLast = currentLast + maxResults
		if(currentLast > last):
			 maxResults = maxResults-(currentLast -last)-1
		#load next page
		url1 = url+"&pageToken="+data["nextPageToken"]
		response = urllib.urlopen(url1)
		data = json.loads(response.read())
	
print str(playListSize) + " GB"


