import ConfigParser
from API.PlayMusic import API

api = API()

config = ConfigParser.ConfigParser()
config.read('config.cfg')
username = config.get('Login', 'username')
password = config.get('Login', 'password')

api.login(username, password)

playlists = api.getPlaylists()
lib = api.getLibrary()

playlistTrackIds = []

for p in playlists:
	playlistTrackIds.extend(p.trackIds)

trackIdsNotInLibrary = [t for t in playlistTrackIds if not lib.getTrack(t)]

print 'Adding ' + str(len(trackIdsNotInLibrary)) + ' tracks to library'

for trackId in trackIdsNotInLibrary:
	api.addTrackToLibrary(trackId)

api.logout()



