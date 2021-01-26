#   Musical Track Database
This application will read an iTunes export file in XML and produce a properly normalized database with this structure:

>CREATE TABLE Artist (
>    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
>    name    TEXT UNIQUE
>);
>
>CREATE TABLE Genre (
>    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
>    name    TEXT UNIQUE
>);

>CREATE TABLE Album (
>    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
>    artist_id  INTEGER,
>    title   TEXT UNIQUE
>);

>CREATE TABLE Track (
>    id  INTEGER NOT NULL PRIMARY KEY 
>        AUTOINCREMENT UNIQUE,
>    title TEXT  UNIQUE,
>    album_id  INTEGER,
>    genre_id  INTEGER,
>    len INTEGER, rating INTEGER, count INTEGER
>);

-   If you run the program multiple times in testing or with different files, make sure to empty out the data before each run.

**Step 1:** Parse Library.xml file 
**Step 2:** Extract the desired data and create a database.
**Step 3:** Run the following query on the DB.

>SELECT Track.title, Artist.name, Album.title, Genre.name 
>    FROM Track JOIN Genre JOIN Album JOIN Artist 
>    ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
>        AND Album.artist_id = Artist.id
>    ORDER BY Artist.name LIMIT 3