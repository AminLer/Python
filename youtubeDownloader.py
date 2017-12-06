#youtube downloader
#for more info see: np1.github.io/pafy/
import pafy

url = 'https://www.youtube.com/watch?v=3O1_3zBUKM8'

video = pafy.new(url)
print("Video:")
print(video.streams)

streams = video.streams
for s in streams:
	print(s.resolution, s.extension)#,s.url)

best = video.getbest()
print("Best Resolution:" )
print(best.resolution, best.extension)
#filename = best.download(filepath="/home/user/Documents/Python")

print("Audio:")
audiostreams = video.audiostreams
for a in audiostreams:
	print(a.bitrate, a.extension, a.get_filesize())

bestaudio = video.getbestaudio()
print("Best Audio:")
print(bestaudio.bitrate, bestaudio.get_filesize())
aud = video.getbestaudio()
print(aud.get_filesize()+2)
#get_filesize() is in bytes
#filename = bestaudio.download(filepath="/home/user/Documents/Python")
