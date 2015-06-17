from GMusic import GMusic

playlists = GMusic.getPlaylists()

# counter = 0
# for p in playlists:
# 	print str(counter) + '  ' + str(p)
# 	counter = counter + 1

# choice = raw_input('Choose the playlist: ')

# p = playlists[int(choice)]

# print p.tracks[0].playlistInfo
for p in playlists:
	with open( p.name + '.txt', 'w') as f:
		for t in p.tracks:
			f.write(str(t) + '\n')

for p in playlists:
	print '---------------------------------------------'
	print 'Playlist ' + str(p)
	s = sorted(p.tracks, key=lambda pp : pp.title)

	GMusic.sortPlaylist(p,s)
	print '---------------------------------------------'

GMusic.logout()





# def reorder_playlist_entry(p, entry, to_follow_entry=None, to_precede_entry=None):
# 	if to_precede_entry == None:
# 		i = p.index(entry)
# 		p.insert(-1, p.pop(i))
# 	elif to_follow_entry == None:
# 		i = p.index(entry)
# 	else:
# 		tf = p.index(to_follow_entry)
# 		tp = p.index(to_precede_entry)
# 		i = p.index(entry)
# 		p.insert(tf+1, p.pop(i))

# from random import shuffle
# lines = []
# with open('t.txt', 'r') as f:
# 	lines = f.readlines()

# # lines = [l.strip('\n') for l in lines]

# shuffle(lines)
# print lines

# sortedList = sorted(lines)

# print len(sortedList)


# for num in range(0, len(sortedList)):
# 	if sortedList[num] != lines[num]:
# 		if (num == 0):
# 			reorder_playlist_entry(lines, sortedList[num], to_follow_entry=None, to_precede_entry=lines[num])
# 		elif (num == len(sortedList) -1 ):
# 			reorder_playlist_entry(lines, sortedList[num], to_follow_entry=lines[num], to_precede_entry=None)
# 		else:
# 			reorder_playlist_entry(lines, sortedList[num], to_follow_entry=lines[num-1], to_precede_entry=lines[num])

# with open('t3.txt', 'w') as f:
# 	f.writelines(lines)



# prev = None
# for num in range(0, len(sortedList)):
# 	print num
# 	if sortedList[num] != playTracks[0]:
# 		if num == len(sortedList) - 1:
# 			api.reorder_playlist_entry(sortedList[num]['entry'], prev, None)
# 		else:
# 			api.reorder_playlist_entry(sortedList[num]['entry'], prev, playTracks[0]['entry'])
# 		print sortedList[num]['name'] + "  " + playTracks[0]['name'] + "  " + str(num)
# 	playTracks.remove(sortedList[num])

# 	prev = sortedList[num]['entry']



