import pandas as pd
import sqlite3

database = 'database.sqlite'
conn = sqlite3.connect(database)

tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

match = pd.read_sql("SELECT * FROM Match;", conn)
print(match.head())

matches = pd.read_sql("""SELECT AVG(Match_Id) AS AVG_Id, Match_Winner
                         FROM Match
                         Where Season_Id = 5
                         GROUP BY Match_Winner
                         ORDER BY AVG(Match_Id);""", conn)

print(matches)

min_margin = pd.read_sql(""" SELECT MIN (Match_Id) AS Min_Id
                             FROM MATCH;""", conn)

print(min_margin)

max_margin = pd.read_sql(""" SELECT MAX(Match_Id) AS Max_Id
                             FROM Match;""", conn)

print(max_margin)

count = pd.read_sql("""SELECT COUNT(DISTINCT Man_of_the_Match) AS Count_Table
    FROM Match;""", conn)

print(count)