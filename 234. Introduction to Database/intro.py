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

"""
C:\Users\MGorb>cd c:\users\MGorb\Desktop\Python\STUDY_Python

c:\Users\MGorb\Desktop\Python\STUDY_Python>DIR
 Том в устройстве C имеет метку Windows
 Серийный номер тома: D8ED-EB8D

 Содержимое папки c:\Users\MGorb\Desktop\Python\STUDY_Python

26.02.2023  04:20    <DIR>          .
26.02.2023  04:20    <DIR>          ..
26.02.2023  04:19    <DIR>          234. Introduction to Database
26.02.2023  03:18           190 464 music-backup1
26.02.2023  04:20           190 464 music.db
23.02.2023  01:32             8 192 test.db
23.02.2023  01:29             8 192 testbackup
               4 файлов        397 312 байт
               3 папок  429 582 770 176 байт свободно

c:\Users\MGorb\Desktop\Python\STUDY_Python>SQLITE3 music.db
SQLite version 3.41.0 2023-02-21 18:09:37
Enter ".help" for usage hints.
sqlite> .backup music-backup2
sqlite> DELTE FROM songs WHERE track < 50;
Parse error: near "DELTE": syntax error
  DELTE FROM songs WHERE track < 50;
  ^--- error here
  
sqlite> DELETE FROM songs WHERE track < 50;
sqlite> SELECT * FROM songs;

198|60|Turkeys|177
912|53|My Brother Makes The Noises For The Talkies|177
1116|59|The Strain|177
1690|61|King Of Scurf|177
1994|67|Fresh Wound|177
2135|63|Straight From The Heart|177
2434|57|Mr. Apollo (Single Version) (German Version)|177
2535|50|I Want To Be With You|177
2583|68|Bad Blood|177
2621|69|Slush|177
2679|65|Rawlinson End|177
2736|54|I'm Going To Bring A Watermelon To My Girl Tonight|177
2794|66|Don't Get Me Wrong|177
3010|58|Ready Mades|177
3358|64|Rusty (Champion Thrust)|177
3618|72|Trouser Freak - Roger Ruskin Spear & His Giant Orchestral Wardrobe|177
3712|62|Waiting For The Wardrobe|177
3797|70|Labio-Dental Fricative - Vivian Stanshall Sean Head Showband|177
3959|55|Alley Oop|177
4308|52|Busted|177
4881|51|Noises For The Leg|177
4991|56|Button Up Your Overcoat|177
5256|50|Closer To You|254
5312|71|Re-Cycled Vinyl Blues - Neil Innes|177

sqlite> SELECT * FROM artist_list1;
Bonzo Dog Band|Cornology|50|I Want To Be With You
Bonzo Dog Band|Cornology|51|Noises For The Leg
Bonzo Dog Band|Cornology|52|Busted
Bonzo Dog Band|Cornology|53|My Brother Makes The Noises For The Talkies
Bonzo Dog Band|Cornology|54|I'm Going To Bring A Watermelon To My Girl Tonight
Bonzo Dog Band|Cornology|55|Alley Oop
Bonzo Dog Band|Cornology|56|Button Up Your Overcoat
Bonzo Dog Band|Cornology|57|Mr. Apollo (Single Version) (German Version)
Bonzo Dog Band|Cornology|58|Ready Mades
Bonzo Dog Band|Cornology|59|The Strain
Bonzo Dog Band|Cornology|60|Turkeys
Bonzo Dog Band|Cornology|61|King Of Scurf
Bonzo Dog Band|Cornology|62|Waiting For The Wardrobe
Bonzo Dog Band|Cornology|63|Straight From The Heart
Bonzo Dog Band|Cornology|64|Rusty (Champion Thrust)
Bonzo Dog Band|Cornology|65|Rawlinson End
Bonzo Dog Band|Cornology|66|Don't Get Me Wrong
Bonzo Dog Band|Cornology|67|Fresh Wound
Bonzo Dog Band|Cornology|68|Bad Blood
Bonzo Dog Band|Cornology|69|Slush
Bonzo Dog Band|Cornology|70|Labio-Dental Fricative - Vivian Stanshall Sean Head Showband
Bonzo Dog Band|Cornology|71|Re-Cycled Vinyl Blues - Neil Innes
Bonzo Dog Band|Cornology|72|Trouser Freak - Roger Ruskin Spear & His Giant Orchestral Wardrobe
J.J. Cale|Anyway The Wind Blows - The Anthology|50|Closer To You

sqlite> SELECT * FROM songs WHERE track <> 71;
198|60|Turkeys|177
912|53|My Brother Makes The Noises For The Talkies|177
1116|59|The Strain|177
1690|61|King Of Scurf|177
1994|67|Fresh Wound|177
2135|63|Straight From The Heart|177
2434|57|Mr. Apollo (Single Version) (German Version)|177
2535|50|I Want To Be With You|177
2583|68|Bad Blood|177
2621|69|Slush|177
2679|65|Rawlinson End|177
2736|54|I'm Going To Bring A Watermelon To My Girl Tonight|177
2794|66|Don't Get Me Wrong|177
3010|58|Ready Mades|177
3358|64|Rusty (Champion Thrust)|177
3618|72|Trouser Freak - Roger Ruskin Spear & His Giant Orchestral Wardrobe|177
3712|62|Waiting For The Wardrobe|177
3797|70|Labio-Dental Fricative - Vivian Stanshall Sean Head Showband|177
3959|55|Alley Oop|177
4308|52|Busted|177
4881|51|Noises For The Leg|177
4991|56|Button Up Your Overcoat|177
5256|50|Closer To You|254
sqlite>
"""
# sqlite> SELECT count(*) FROM songs;
# 24
# sqlite> SELECT count(*) FROM albums;
# 439
# sqlite> SELECT count(*) FROM artists;
# 202
# sqlite>
"""
sqlite> .restore music-backup2
sqlite> SELECT count(*) FROM songs;
5350
sqlite> SELECT count(*) FROM albums;
439
sqlite> SELECT count(*) FROM artists;
202
sqlite>
"""

# sqlite> SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = 'Forbidden';
# The Illusion of Power
# Sick and Tired
# Can't Get Close Enough
# Forbidden
# Shaking Off the Chains
# Get a Grip
# Kiss of Death
# Guilty as Hell
# Rusty Angels
# I Won't Cry for You
# sqlite>

# sqlite> SELECT songs.track, songs.title FROM songs INNER JOIN albums ON songs.album = albums._id WHERE albums.name = 'Forbidden' ORDER BY songs.track;
# 1|The Illusion of Power
# 2|Get a Grip
# 3|Can't Get Close Enough
# 4|Shaking Off the Chains
# 5|I Won't Cry for You
# 6|Guilty as Hell
# 7|Sick and Tired
# 8|Rusty Angels
# 9|Forbidden
# 10|Kiss of Death
# sqlite>

"""
sqlite> SELECT songs.title FROM songs INNER JOIN albums ON songs.album = albums._id INNER JOIN artists ON albums.artist = artists._id WHERE artists.name = 'Deep Purple';
Love Help Me (2000 Digital Remaster)
Might Just Take Your Life
And The Address (2000 Digital Remaster)
Fireball (Take 1 - Instrumental)
Maybe I'm a Leo
Fireball
No One Came
Mistreated
Smoke On The Water
Mary Long
Rat Bat Blue
What's Goin' On Here
I Need Love
Studio Chat
Hush
Shield
April (2000 Digital Remaster)
Wring That Neck
When a Blind Man Cries (B-Side)
Bird Has Flown (2000 Digital Remaster)
Highway Star
Pictures Of Home
Fools
Lazy
Smoke On The Water
You Fool No One
Speed King (Piano Version)
Black Night
Slow Train (Album Outtake)
Dealer
Mistreated
Pictures of Home
Space Truckin'
Our Lady ('99 Remix)
Child In Time
The Painter (2000 Digital Remaster)
Lady Luck
Sail Away
Bloodsucker
Painted Horse (studio out-take)
Prelude_ Happiness_I'm So Glad (Medley) (2000 Digital R
Woman From Tokyo ('99 Remix)
Black Night (Unedited Roger Glover Remix)
Hey Joe (BBC Top Gear Session)
Help (Alternate Take)
Listen Learn Read On
Love Don't Mean A Thing
I'm Alone (B-Side)
Burn
Space Truckin'
The Painter (BBC Radio Session)
Studio Chat
High Ball Shooter
Woman From Tokyo
You Fool No One
Studio Chat
The Bird Has Flown (Alternate A-Side Version) (1998 Dig
Third Movement- Vivace - Presto
Woman From Tokyo (alt.bridge)
River Deep Mountain High
Living Wreck
Shadows
Rat Bat Blue (writing session)
Studio Chat
'A' 200
Studio Chat
Jam Stew (Unreleased Instrumental)
Drifter
Lady Double Dealer
Super Trouper
No One Came (Remix 1996)
Exposition - We Can Work It Out
Lalena (2000 Digital Remaster)
Speed King
Lay Down Stay Down
Into The Fire
Flight Of The Rat (Roger Glover Remix)
Strange Kind Of Woman (A-Side Remix 1996)
You Can't Do It Right
Lalena (BBC Radio Session)
The Mule (Drum Solo)
Emmaretta (1998 Digital Remaster)
Backwards Piano
Lazy (Quadrophonic Mix)
No No No
Speed King
Black Night (Original Single Version)
Hey Joe (2000 Digital Remaster)
Smooth Dancer
Love Child
The Gypsy
Lazy
Anyone's Daughter
First Day Jam (instrumental)
The Noise Abatement Society Tapes
One More Rainy Day (2000 Digital Remaster)
Stormbringer
First Movement- Moderato - Allegro
Child In Time
Lady Double Dealer
Never Before
Demon's Eye (Remix 1996)
Wring That Neck
Fault Line (2000 Digital Remaster)
You Keep On Moving
Strange Kind Of Woman
It's All Over (BBC Top Gear Session Bonus Track)
Second Movement- Andante
Child In Time
Cry Free (Roger Glover Remix)
Hey Bop A Re Bop (BBC Top Gear Session Bonus Track)
Freedom (Album Outtake)
Why Didn't Rosemary_ (1999 Digital Remaster)
Place In Line
Maybe I'm a Leo (Quadrophonic Mix)
Studio Chat
Rat Bat Blue ('99 Remix)
Wring That Neck (BBC Top Gear Session Bonus Track)
Encore- Third Movement- Vivace - Presto (Part)
Love Help Me (Instrumental Version)
Flight Of The Rat
Playground (Remixed Instrumental Studio Out Take Bonus Track)
[Intro]
Smoke On The Water
Gettin' Tighter
Demon's Eye
Maybe I'm A Leo
Stormbringer
When A Blind Man Cries
Speed King (Roger Glover Remix)
Anthem
Oh No No No (Studio Out Take Bonus Track)
Burn
Soldier Of Fortune
This Time Around Owed To 'G' (Instrumental)
Hush (Live US TV)
Lazy
Mandrake Root (1998 Digital Remaster)
Comin' Home
Hold On
Highway Star
Kentucky Woman
Hush (1998 Digital Remaster)
Highway Star
Blind (2000 Digital Remaster)
Our Lady
Never Before
Hard Lovin' Man
Holy Man
Emmaretta (BBC Top Gear Session)
Help (2000 Digital Remaster)
Chasing Shadows (2000 Digital Remaster)
The Mule
Lucille
Space Truckin'
sqlite>
"""

