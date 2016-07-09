from Track import Track
import datetime

class Library(object):

	def __init__(self, rawLibrary):
		self.rawLibrary = rawLibrary
		self.tracks = [Track(s) for s in self.rawLibrary]

	def getTrack(self, trackId):
		tracksFound = []

		for t in self.tracks:
			if trackId == t.id:
				tracksFound.append(t)
			else:
				if hasattr(t, 'nid') and t.nid == trackId:
					tracksFound.append(t)

		if len(tracksFound) == 1:
			return tracksFound[0]
		else:
			return None

	def __str__(self):
		return 'Library' + " - " + str(len(self.tracks))

	def __repr__(self):
		return self.__str__()