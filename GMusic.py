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
	def sortPlaylist(playlist, orderedTracks):
		if playlist in GMusic.getPlaylists():
			tracks = playlist.tracks[:]

			api = GMusic.__getApi()

			trackIds = [t.playlistInfo['id'] for t in tracks]
			api.remove_entries_from_playlist(trackIds)
			trackIds = [t.playlistInfo['trackId'] for t in orderedTracks]
			api.add_songs_to_playlist(playlist.id, trackIds)

			# for num in range(0, len(orderedTracks)):
			# 	if orderedTracks[num] != tracks[num]:
			# 		if (num == 0):
			# 			GMusic.__sortPlaylistHelper(tracks, orderedTracks[num], to_follow_entry=None, to_precede_entry=tracks[num])
			# 			raw_input('Please move ' + str(tracks[num]) + ' to the top of playlist ' + str(playlist) + ' then press enter:')
			# 		elif (num == len(orderedTracks) -1 ):
			# 			GMusic.__sortPlaylistHelper(tracks, orderedTracks[num], to_follow_entry=tracks[num], to_precede_entry=None)
			# 			raw_input('Please move ' + str(tracks[num]) + ' to the bottom of playlist ' + str(playlist) + ' then press enter:')
			# 		else:
			# 			GMusic.__sortPlaylistHelper(tracks, orderedTracks[num], to_follow_entry=tracks[num-1], to_precede_entry=tracks[num])

	@staticmethod
	def __sortPlaylistHelper(unorderedTracks, entry, to_follow_entry=None, to_precede_entry=None):
		api = GMusic.__getApi()

		if to_precede_entry is None:
			i = unorderedTracks.index(entry)
			unorderedTracks.insert(-1, unorderedTracks.pop(i))
		elif to_follow_entry is None:
			i = unorderedTracks.index(entry)
			unorderedTracks.insert(0, unorderedTracks.pop(i))
		else:
			tf = unorderedTracks.index(to_follow_entry)
			tp = unorderedTracks.index(to_precede_entry)
			i = unorderedTracks.index(entry)
			unorderedTracks.insert(tf+1, unorderedTracks.pop(i))

		if not to_follow_entry:
			tfe = None
		else:
			tfe = to_follow_entry.playlistInfo

		if not to_precede_entry:
			tpe = None
		else:
			tpe = to_precede_entry.playlistInfo

		api.reorder_playlist_entry(entry.playlistInfo, to_follow_entry=tfe, to_precede_entry=tpe)

	@staticmethod
	def printer(org, sor, curr):
		print '---------------------------------------------------------------------------'

		for num in range(0, len(org)):
			print str(org[num]).ljust(50) + ' | ' + str(sor[num]).ljust(50) + ' | ' + str(curr[num]).ljust(50)

		print '---------------------------------------------------------------------------'


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





















