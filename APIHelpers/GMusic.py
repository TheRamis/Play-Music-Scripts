from gmusicapi import Mobileclient
import ConfigParser
from Track import Track
from Playlist import Playlist
import requests, os
requests.packages.urllib3.disable_warnings()

class GMusic(object):

	api = None
	library = None
	playlists = None
	username = None
	password = None
	loggedIn = False
	rawLibrary = None
	rawPlaylists = None

	@staticmethod
	def login():
		if not GMusic.loggedIn:
			api = GMusic.__getApi()
			config = ConfigParser.ConfigParser()
			config.read('config.cfg')
			api.login(config.get('Login', 'username'), config.get('Login', 'password'))
			GMusic.loggedIn = True

	@staticmethod
	def logout():
		if GMusic.loggedIn:
			api = GMusic.__getApi()
			api.logout()
			GMusic.loggedIn = False

	@staticmethod
	def getLibrary():
		GMusic.login()

		if GMusic.rawLibrary is None or GMusic.rawPlaylists is None:
			GMusic.__getData()

		if GMusic.library is None:
			if GMusic.__addSongsToLibrary():
				GMusic.__getData()
			GMusic.library = [Track(s) for s in GMusic.rawLibrary]

		return GMusic.library

	@staticmethod
	def getPlaylists():
		GMusic.login()

		if GMusic.rawLibrary is None or GMusic.rawPlaylists is None:
			GMusic.getLibrary()

		if GMusic.playlists is None:
			GMusic.playlists = [Playlist(p, GMusic.getLibrary()) for p in GMusic.rawPlaylists]

		return GMusic.playlists

	@staticmethod
	def sortAllPlaylists():
		playlists = GMusic.getPlaylists()
		api = GMusic.__getApi()

		for p in playlists:
			orderedTracks = sorted(p.tracks, key=lambda pp : pp.title)
			tracks = p.tracks[:]
			trackIds = [t.playlistInfo['trackId'] for t in orderedTracks]
			api.delete_playlist(p.id)
			newPlaylistId = api.create_playlist(p.name)
			api.add_songs_to_playlist(newPlaylistId, trackIds)

		GMusic.rawLibrary = None

	@staticmethod
	def __getData():
		api = GMusic.__getApi()
		GMusic.rawLibrary = api.get_all_songs()
		GMusic.rawPlaylists = api.get_all_user_playlist_contents()

	@staticmethod
	def __addSongsToLibrary():
		api = GMusic.__getApi()
		libraryUpdated = False
		for playlist in GMusic.rawPlaylists:
			for track in playlist['tracks']:
				exists = False
				for song in GMusic.rawLibrary:
					if song['id'] == track['trackId']:
						exists = True
						break

					if 'nid' in song:
						if song['nid'] == track['trackId']:
							exists = True
							break
				if exists == False:
					if track['trackId'].startswith('T'):
						api.add_aa_track(track['trackId'])
						libraryUpdated = True
		return libraryUpdated

	@staticmethod
	def __getApi():
		if GMusic.api is None:
			GMusic.api = Mobileclient()

		return GMusic.api





















