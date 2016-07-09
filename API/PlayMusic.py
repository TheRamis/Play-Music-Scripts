from gmusicapi import Mobileclient
from Track import Track
from Library import Library
from Playlist import Playlist

class API(object):

	def __init__(self):
		self.loggedIn = False
		self.api = None

	def login(self, username, password):
		if not self.loggedIn:
			api = self.__getApi()
			success = api.login(username, password, Mobileclient.FROM_MAC_ADDRESS)
			self.loggedIn = success
			return success

	def logout(self):
		if self.loggedIn:
			success = self.api.logout()
			self.loggedIn = not success
			return success
		return False

	def getLibrary(self):
		if self.loggedIn:
			rawTracks = self.api.get_all_songs()
			library = Library(rawTracks)
			return library

	def addTrackToLibrary(self, trackId):
		if self.loggedIn:
			self.api.add_store_track(trackId)
			return True
		return False

	def getPlaylists(self):
		if self.loggedIn:
			rawPlaylists = self.api.get_all_user_playlist_contents()
			playlists = [Playlist(p) for p in rawPlaylists]
			return playlists

	def __getApi(self):
		if self.api is None:
			self.api = Mobileclient()
		return self.api

