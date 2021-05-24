import sqlite3

conn = sqlite3.connect('tracks.sqlite')

print(type(conn))

cur = conn.cursor()
print(type(cur))