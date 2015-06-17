from Track import Track
import datetime

class Playlist(object):

	def __init__(self, playlistInfo, library):
		self.playlistInfo = playlistInfo
		self.name = Playlist.cleanStr(self.playlistInfo['name'])
		self.id = self.playlistInfo['id']
		self.date = datetime.datetime.fromtimestamp(int(playlistInfo['creationTimestamp'])/1000000.0)
		self.tracks = []
		self.tracksNotInLibrary = []
		self.mapTracks(library)

	def mapTracks(self, library):
		for track in self.playlistInfo['tracks']:
			result = Playlist.findSongInLibrary(library, track['trackId'])
			if result:
				result.playlistInfo = track
				self.tracks.append(result)
			else:
				self.tracksNotInLibrary.append(track)
		if len(self.tracksNotInLibrary):
			print str(len(self.tracksNotInLibrary)) + " tracks not found for " + self.name
		return self

	@staticmethod
	def findSongInLibrary(library, trackId):
		for s in library:
			if s.id == trackId:
				return s
			if s.aaTrack:
				if s.nid == trackId:
					return s
		return None

	@staticmethod
	def cleanStr(text):
		return text.replace(u"\u2018", "'").replace(u"\u2019", "'").replace( "e" + u"\u0301", "").encode('utf-8').strip()

	def __str__(self):
		return self.name + " - " + str(len(self.tracks))

	def __repr__(self):
		return self.__str__()