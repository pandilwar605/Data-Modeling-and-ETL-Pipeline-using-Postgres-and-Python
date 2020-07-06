# DROP TABLES

songplay_table_drop = "drop table if exists songplays"
user_table_drop = "drop table if exists users"
song_table_drop = "drop table if exists songs"
artist_table_drop = "drop table if exists artists"
time_table_drop = "drop table if exists time"

# CREATE TABLES
# Fact Table
# songplays - records in log data associated with song plays i.e. records with page NextSong
# songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
# Dimension Tables
# users - users in the app
# user_id, first_name, last_name, gender, level
# songs - songs in music database
# song_id, title, artist_id, year, duration
# artists - artists in music database
# artist_id, name, location, latitude, longitude
# time - timestamps of records in songplays broken down into specific units
# start_time, hour, day, week, month, year, weekday

songplay_table_create = ("""create table if not exists songplays(songplay_id varchar, start_time varchar, user_id varchar, level varchar, song_id varchar, artist_id varchar, session_id varchar, location varchar, user_agent varchar) 
""")

user_table_create = ("""create table if not exists users(user_id varchar, first_name varchar, last_name varchar, gender varchar, level varchar)
""")

song_table_create = ("""create table if not exists songs(song_id varchar, title varchar, artist_id varchar, year int, duration float)
""")

artist_table_create = ("""create table if not exists artists(artist_id varchar, name varchar, location varchar, latitude float, longitude float)
""")

time_table_create = ("""create table if not exists time(start_time varchar, hour int, day int, week int, month varchar, year int, weekday varchar)
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into songplays(songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""insert into users(user_id, first_name, last_name, gender, level) values(%s,%s,%s,%s,%s)
""")

song_table_insert = ("""insert into songs(song_id, title, artist_id, year, duration) values(%s,%s,%s,%s,%s)
""")

artist_table_insert = ("""insert into artists(artist_id, name, location, latitude, longitude) values(%s,%s,%s,%s,%s)
""")


time_table_insert = ("""insert into time(start_time, hour, day, week, month, year, weekday) values(%s,%s,%s,%s,%s,%s,%s)
""")

# FIND SONGS
# Implement the song_select query in sql_queries.py to find the song ID and artist ID based on the title, artist name, and duration of a song.
# Select the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to songplay_data

song_select = (""" select s.song_id,a.artist_id from songs s join artists a on a.artist_id=s.artist_id where (s.title,a.name,s.duration)=(%s,%s,%s)
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]