#Opening File and Extracting all mails where line is starting with From:
file = open("Assignment_file.txt")
collection = [line.rstrip() for line in file if line.startswith("From:")]
domain = list()
for line in collection:
	domain.append(line.split(": ")[1].split("@")[1])
file.close()

#Now creating a DB storing count of each emailID
import sqlite3
conn = sqlite3.connect("Mail_Count.sqlite")
cur = conn.cursor()

cur.execute('''
		DROP TABLE IF EXISTS Counts''')
cur.execute('''
		CREATE TABLE Counts ( email TEXT , count INTEGER)''')
for id in domain:
	cur.execute('''
		SELECT count FROM Counts WHERE email = ?''',(id,))
	row = cur.fetchone()
	if row is None:
		cur.execute('''
		INSERT INTO Counts( email, count) VALUES (?,1)''',(id,))
	else:
		cur.execute('''
		UPDATE Counts SET count = count+1 WHERE email = ?''',(id,))
cur.execute('ALTER TABLE Counts RENAME COLUMN "email" TO "org"')
conn.commit()

sqlQuery = ('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10')
CountOfId = cur.execute('SELECT MAX(count) FROM Counts')

print(CountOfId.fetchone()[0])
cur.close()
