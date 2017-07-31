
import sqlite3
import csv

with sqlite3.connect('Apps.db') as connection:
	csvWriter = csv.writer(open('Remaining.csv', 'w'))
	c = connection.cursor()
	c.execute('SELECT  * FROM AppData')
	rows = c.fetchall()
	csvWriter.writerows(rows)

