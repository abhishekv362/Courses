# Opening a xml file

import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect("Library.sqlite")
cur = conn.cursor()

cur.executescript('''
	DROP TABLE IF EXISTS Artist;
	DROP TABLE IF EXISTS Genre;
	DROP TABLE IF EXISTS Album;
	DROP TABLE IF EXISTS Track;

	CREATE TABLE Artist (
    	id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    	name    TEXT UNIQUE );

	CREATE TABLE Genre (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		name    TEXT UNIQUE
	);

	CREATE TABLE Album (
		id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		artist_id  INTEGER,
		title   TEXT UNIQUE
	);

	CREATE TABLE Track (
		id  INTEGER NOT NULL PRIMARY KEY 
			AUTOINCREMENT UNIQUE,
		title TEXT  UNIQUE,
		album_id  INTEGER,
		genre_id  INTEGER,
		len INTEGER, rating INTEGER, count INTEGER
	);	

''')


def lookup(element, key):
	found = False
	for each in element:
		if found:
			return each.text
		if each.tag == 'key' and each.text == key:
			found = True
	return None


file = ET.parse("Library.xml")
Songs = file.findall("./dict/dict/dict")

for song in Songs:
	if (lookup(song, "Track ID") is None): continue

	TrackName = lookup(song, 'Name')
	ArtistName = lookup(song, 'Artist')
	AlbumName = lookup(song, 'Album')
	GenreName = lookup(song, "Genre")
	Length = lookup(song, "Total Time")
	Rating = lookup(song, "Rating")
	Count = lookup(song, "Play Count")

	if TrackName is None or ArtistName is None or AlbumName is None or GenreName is None:
		continue

	#	print(TrackName, "\n", ArtistName, "\n", AlbumName, "\n", GenreName, "\n", Length, "\n", Rating, "\n", Count)

	cur.execute('''
		INSERT OR IGNORE INTO Artist ('name') VALUES (?) ''', (ArtistName,))
	cur.execute('''
		SELECT id FROM Artist WHERE name =  ? ''', (ArtistName,))
	artist_id = cur.fetchone()[0]

	cur.execute('''
			INSERT OR IGNORE INTO Genre ('name') VALUES (?) ''', (GenreName,))
	cur.execute('''
			SELECT id FROM Genre WHERE name = ? ''', (GenreName,))
	genre_id = cur.fetchone()[0]

	cur.execute('''
			INSERT OR IGNORE INTO Album ('artist_id','title') VALUES (?,?) ''', (artist_id, AlbumName,))
	cur.execute('''
			SELECT id FROM Album WHERE title = ? ''', (AlbumName,))
	album_id = cur.fetchone()[0]

	cur.execute('''
		INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)''',
				(TrackName, album_id, genre_id, Length, Rating, Count,))
	cur.execute('''
		SELECT id FROM Track WHERE title = ? ''', (TrackName,))

conn.commit()

Query = '''
	SELECT Track.title, Artist.name, Album.title, Genre.name 
    FROM Track JOIN Genre JOIN Album JOIN Artist 
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name LIMIT 3
    '''

b = cur.execute(Query)

for list in b.fetchall():
	print(list)
cur.close()