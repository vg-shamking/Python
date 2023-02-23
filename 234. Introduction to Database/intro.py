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
