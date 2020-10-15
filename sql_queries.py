# Drop Tables

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"


# Create Tables

songplay_table_create =("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id INT PRIMARY KEY,
        start_time TIMESTAMP NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR(10) NOT NULL,
        song_id VARCHAR(100),
        artist_id VARCHAR(100),
        session_id INT NOT NULL,
        location VARCHAR(256),
        user_agent VARCHAR
    );
    COMMENT ON COLUMN songplays.songplay_id is 'AutoIncrement Column';
    COMMENT ON COLUMN songplays.user_agent is 'No Specified limit for Headers according to HTTP specification. Web servers do have the limit and vary.';
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        gender VARCHAR(1) NOT NULL,
        level VARCHAR(20) NOT NULL
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR(100) PRIMARY KEY,
        title VARCHAR(256) NOT NULL,
        artist_id VARCHAR(100) NOT NULL,
        year SMALLINT,
        duration NUMERIC
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR(100) PRIMARY KEY,
        name VARCHAR(256) NOT NULL,
        location VARCHAR(256),
        latitude NUMERIC,
        longitude NUMERIC
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour SMALLINT NOT NULL,
        day SMALLINT NOT NULL,
        week SMALLINT NOT NULL,
        month SMALLINT NOT NULL,
        year SMALLINT NOT NULL,
        weekday SMALLINT NOT NULL
    );
    COMMENT ON COLUMN time.start_time is 'The value of log.ts';
""")

# Insert Records

songplay_table_insert = ("""
    INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING;
""")


user_table_insert = ("""
    INSERT INTO users(user_id, first_name, last_name, gender, level)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET 
        first_name = EXCLUDED.first_name, 
        last_name = EXCLUDED.last_name, 
        gender = EXCLUDED.gender, 
        level = EXCLUDED.level;
""")

song_table_insert = ("""
    INSERT INTO songs(song_id, title, artist_id, year, duration) 
    VALUES(%s, %s, %s, %s, %s) 
    ON CONFLICT (song_id) 
    DO UPDATE SET 
        title = EXCLUDED.title, 
        artist_id = EXCLUDED.artist_id, 
        year = EXCLUDED.year, 
        duration = EXCLUDED.duration;
""")

artist_table_insert = ("""
    INSERT INTO artists(artist_id, name, location, latitude, longitude) 
    VALUES(%s, %s, %s, %s, %s) 
    ON CONFLICT (artist_id) 
    DO UPDATE SET 
        name = EXCLUDED.name, 
        location = EXCLUDED.location, 
        latitude = EXCLUDED.latitude, 
        longitude = EXCLUDED.longitude;
""")

time_table_insert = ("""
    INSERT INTO time(start_time, hour, day, week, month, year, weekday) 
    VALUES(%s, %s, %s, %s, %s, %s, %s) 
    ON CONFLICT (start_time) 
    DO NOTHING;
""")

# Find songs

song_select = ("""
    SELECT songs.song_id, artists.artist_id 
    FROM songs JOIN artists 
    ON songs.artist_id = artists.artist_id
    WHERE songs.title = %s 
    AND artists.name = %s 
    AND songs.duration = %s;
""") 

# Analysis user activities for listening music

analysis_most_popular_song = ("""
    SELECT songs.title AS "Song Title", artists.name AS "Artist Name"
    FROM ( songs JOIN artists ON songs.artist_id = artists.artist_id )
    WHERE songs.song_id = (
        SELECT songplays.song_id
        FROM ( songplays JOIN time ON songplays.start_time = time.start_time )
        WHERE time.year = %s
        GROUP BY songplays.song_id
        ORDER BY COUNT(songplays.song_id) DESC
        LIMIT 1
    );
""")

analysis_most_popular_artist = ("""
    SELECT artists.name AS "Artist Name", artists.location AS "Location"
    FROM artists
    WHERE artists.artist_id = (
        SELECT songplays.artist_id
        FROM ( songplays JOIN time ON songplays.start_time = time.start_time )
        WHERE time.year = %s
        GROUP BY songplays.artist_id
        ORDER BY COUNT(songplays.artist_id) DESC
        LIMIT 1
    );
""")

analysis_mean_number_on_different_level = ("""
    SELECT users.level AS "User Level", CAST(AVG(total.count) AS DECIMAL(10,2)) as "Avarage Number of Songs"
    FROM users 
    JOIN 
        (
            SELECT songplays.user_id AS id, COUNT(songplays.user_id) AS count
            FROM ( songplays JOIN time ON songplays.start_time = time.start_time )
            WHERE time.year = %s
            GROUP BY songplays.user_id
            ORDER BY count DESC
        ) AS total
    ON users.user_id = total.id
    GROUP BY users.level;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]