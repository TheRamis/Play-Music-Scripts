from Track import Track
import datetime

class Playlist(object):

	def __init__(self, rawPlaylist):
		self.rawPlaylist = rawPlaylist
		self.name = Playlist.cleanStr(self.rawPlaylist['name'])
		self.id = self.rawPlaylist['id']
		self.date = datetime.datetime.fromtimestamp(int(rawPlaylist['creationTimestamp'])/1000000.0)
		self.trackIds = [t['trackId'] for t in self.rawPlaylist['tracks']]

	@staticmethod
	def cleanStr(text):
		return text.replace(u"\u2018", "'").replace(u"\u2019", "'").replace( "e" + u"\u0301", "").encode('utf-8').strip()

	def __str__(self):
		return self.name + " - " + str(len(self.trackIds))

	def __repr__(self):
		return self.__str__()