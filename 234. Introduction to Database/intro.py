# Standard createion and insert

# C:\Users\MGorb\Desktop\Python\STUDY_Python>sqlite3
# SQLite version 3.41.0 2023-02-21 18:09:37
# Enter ".help" for usage hints.
# Connected to a transient in-memory database.
# Use ".open FILENAME" to reopen on a persistent database.
# sqlite> .headers on
# sqlite> create table contacts (name text, phone integer, email text);
# sqlite> insert into contacts (name, phone, email) values ('Tim', 6545678, 'tim@email.com');
# sqlite> SELECT * FROM contacts;
# name|phone|email
# Tim|6545678|tim@email.com
# sqlite> SELECT email FROM contacts
#    ...> ;
# email
# tim@email.com
# sqlite>

"""
C:\Users\MGorb\Desktop\Python\STUDY_Python>sqlite3 test.db
SQLite version 3.41.0 2023-02-21 18:09:37
Enter ".help" for usage hints.
sqlite> create table contacts (name text, phone integer, email text);
sqlite> INSERT INTO contacts VALUES('Brian', 1234, 'brian@email.com');
sqlite> INSERT INTO contacts VALUES('Tim', 6545678, 'tim@email.com');
sqlite> SELECT * FROM contacts
   ...> ;
Brian|1234|brian@email.com
Tim|6545678|tim@email.com
sqlite> INSERT INTO contacts VALUES('Avril', '+61 087654321', 'avril@email.com');
sqlite> SELECT * FROM contacts
   ...> ;
Brian|1234|brian@email.com
Tim|6545678|tim@email.com
Avril|+61 087654321|avril@email.com
sqlite> SELECT * FROM contacts
   ...> ;
Brian|1234|brian@email.com
Tim|6545678|tim@email.com
Avril|+61 087654321|avril@email.com
sqlite> .backup testbackup
sqlite> UPDATE contacts SET email='steve@isemail.com';
sqlite> SELECT * FROM contacts
   ...> ;
Brian|1234|steve@isemail.com
Tim|6545678|steve@isemail.com
Avril|+61 087654321|steve@isemail.com
sqlite> .restore testbackup
sqlite> SELECT * FROM contacts
   ...> ;
Brian|1234|brian@email.com
Tim|6545678|tim@email.com
Avril|+61 087654321|avril@email.com
sqlite> UPDATE contacts SET email='steve@hisemail.com' WHERE name = "Steve"
   ...> ;
Parse error: no such column: Steve
  tacts SET email='steve@hisemail.com' WHERE name = "Steve" ;
                                      error here ---^
sqlite> UPDATE contacts SET email='steve@hisemail.com' WHERE name = 'Steve';
sqlite> SELECT * FROM contacts
   ...> ;
Brian|1234|brian@email.com
Tim|6545678|tim@email.com
Avril|+61 087654321|avril@email.com
sqlite> UPDATE contacts SET email='steve@hisemail.com' WHERE name = 'Avril';
sqlite> SELECT * FROM contacts;
Brian|1234|brian@email.com
Tim|6545678|tim@email.com
Avril|+61 087654321|steve@hisemail.com
sqlite>
"""

# sqlite> .tables
# contacts
# sqlite> .schema
# CREATE TABLE contacts (name text, phone integer, email text);
# sqlite> .dump
# PRAGMA foreign_keys=OFF;
# BEGIN TRANSACTION;
# CREATE TABLE contacts (name text, phone integer, email text);
# INSERT INTO contacts VALUES('Brian',1234,'brian@email.com');
# INSERT INTO contacts VALUES('Tim',6545678,'tim@email.com');
# INSERT INTO contacts VALUES('Avril','+61 087654321','steve@hisemail.com');
# COMMIT;
# sqlite> .exit

# sqlite> .schema
# CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
# CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
# CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
# sqlite>

# sqlite> .headers on
# sqlite> SELECT * FROM albums WHERE _id = 367;
# _id|name|artist
# 367|Permanent Vacation|152
# sqlite> .backup music-backup1
# sqlite>

# C:\Users\MGorb\Desktop\Python\STUDY_Python>sqlite3 music.db
# SQLite version 3.41.0 2023-02-21 18:09:37
# Enter ".help" for usage hints.
# sqlite> SELECT songs.track, songs.title, album.name FROM songs JOIN albums ON songs.album = album._id;

"""
sqlite> CREATE VIEW artist_list AS
   ...> SELECT artists.name, albums.name, songs.track, songs.title FROM songs
   ...> INNER JOIN albums ON songs.album = album._id
   ...> INNER JOIN artists ON albums.artist = artists._id
   ...> ORDER BY artists.name, albums.name, songs.track;

sqlite> .schema
CREATE TABLE songs (_id INTEGER PRIMARY KEY, track INTEGER, title TEXT NOT NULL, album INTEGER);
CREATE TABLE albums (_id INTEGER PRIMARY KEY, name TEXT NOT NULL, artist INTEGER);
CREATE TABLE artists (_id INTEGER PRIMARY KEY, name TEXT NOT NULL);
CREATE VIEW artist_list1 AS
SELECT artists.name, albums.name, songs.track, songs.title FROM songs
INNER JOIN albums ON songs.album = albums._id
INNER JOIN artists ON albums.artist = artists._id
ORDER BY artists.name, albums.name, songs.track;
sqlite>
"""

# sqlite> SELECT * FROM artist_list1 WHERE name LIKE 'jefferson%';
# Jefferson Airplane|Surrealistic Pillow|1|She Has Funny Cars
# Jefferson Airplane|Surrealistic Pillow|2|Somebody To Love
# Jefferson Airplane|Surrealistic Pillow|3|My Best Friend
# Jefferson Airplane|Surrealistic Pillow|4|Today
# Jefferson Airplane|Surrealistic Pillow|5|Comin' Back To Me
# Jefferson Airplane|Surrealistic Pillow|6|3 5 Of A Mile In 10 Seconds
# Jefferson Airplane|Surrealistic Pillow|7|D.C.B.A. - 25
# Jefferson Airplane|Surrealistic Pillow|8|How Do You Feel
# Jefferson Airplane|Surrealistic Pillow|9|Embryonic Journey
# Jefferson Airplane|Surrealistic Pillow|10|White Rabbit
# Jefferson Airplane|Surrealistic Pillow|11|Plastic Fantastic Lover
# Jefferson Airplane|Surrealistic Pillow|12|In The Morning
# Jefferson Airplane|Surrealistic Pillow|13|J.P.P. McStep B. Blues
# Jefferson Airplane|Surrealistic Pillow|14|Go To Her (Version Two)
# Jefferson Airplane|Surrealistic Pillow|15|Come Back Baby
# Jefferson Airplane|Surrealistic Pillow|16|Somebody To Love (Mono Single Version)
# Jefferson Airplane|Surrealistic Pillow|17|White Rabbit (Mono Single Version)
# Jefferson Starship|Dragon Fly|1|Ride The Tiger
# Jefferson Starship|Dragon Fly|2|That's For Sure
# Jefferson Starship|Dragon Fly|3|Be Young You
# Jefferson Starship|Dragon Fly|4|Caroline
# Jefferson Starship|Dragon Fly|5|Devils Den
# Jefferson Starship|Dragon Fly|6|Come To Life
# Jefferson Starship|Dragon Fly|7|All Fly Away
# Jefferson Starship|Dragon Fly|8|Hyperdrive
# sqlite>
