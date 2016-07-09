import datetime

class Track(object):
	def __init__(self, rawTrack):
		self.rawTrack = rawTrack
		self.title = Track.cleanStr(self.rawTrack['title'])
		self.artist = Track.cleanStr(self.rawTrack['artist'])
		self.playCount = rawTrack.get('playCount', 0)
		self.album = Track.cleanStr(self.rawTrack['album'])
		self.id = self.rawTrack['id']
		self.date = datetime.datetime.fromtimestamp(int(rawTrack['creationTimestamp'])/1000000.0)

		if 'nid' in rawTrack:
			self.nid = rawTrack['nid']

	@staticmethod
	def cleanStr(text):
		return text.replace(u"\u2018", "'").replace(u"\u2019", "'").replace( "e" + u"\u0301", "").encode('utf-8').strip()

	def __str__(self):
		return self.title + " - " + self.artist + " (" + self.album + ")"

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		if not other:
			return False

		if (self.id == other.id):
			return True
