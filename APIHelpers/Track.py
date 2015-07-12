import datetime

class Track(object):

	def __init__(self, trackInfo):
		self.trackInfo = trackInfo
		self.title = Track.cleanStr(self.trackInfo['title'])
		self.artist = Track.cleanStr(self.trackInfo['artist'])
		self.playCount = trackInfo.get('playCount', 0)
		self.album = Track.cleanStr(self.trackInfo['album'])
		self.id = self.trackInfo['id']
		self.aaTrack = False;
		if 'nid' in self.trackInfo:
			self.nid = self.trackInfo['nid']
			self.aaTrack = True;
		self.date = datetime.datetime.fromtimestamp(int(trackInfo['creationTimestamp'])/1000000.0)

	@staticmethod
	def cleanStr(text):
		return text.replace(u"\u2018", "'").replace(u"\u2019", "'").replace( "e" + u"\u0301", "").encode('utf-8').strip()

	def __str__(self):
		return self.title + " - " + self.artist + " (" + self.album + ")"

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		# if (other == None):
		# 	return False

		if (self.id == other.id):
			return True

		# if (self.title == other.title):
		# 	if (self.artist == self.artist):
				# return True

		return False
