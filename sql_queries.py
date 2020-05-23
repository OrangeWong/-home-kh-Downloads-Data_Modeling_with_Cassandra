# drop keyspace
drop_keyspace_query = "DROP KEYSPACE IF EXISTS sparkify_event"

# create keyspace
create_keyspace_query = """
    CREATE KEYSPACE sparkify_event WITH replication = {
        'class': 'SimpleStrategy', 
        'replication_factor' : 1
        };
    """
# drop tables
artist_playlist_drop = "DROP TABLE IF EXISTS artist_playlist_session"
song_playlist_drop = "DROP TABLE IF EXISTS song_playlist_session"
user_playlist_drop = "DROP TABLE IF EXISTS user_playlist_session"

# create tables
artist_playlist_create = "CREATE TABLE IF NOT EXISTS artist_playlist_session "
artist_playlist_create += """
    (session_id int,
     item_in_session int,
     artist_name text,
     song_title text,
     length float,
     PRIMARY KEY (session_id, item_in_session)
        )
"""
song_playlist_create = "CREATE TABLE IF NOT EXISTS song_playlist_session "
song_playlist_create += """
    (user_id int,
     session_id int,
     item_in_session int,    
     artist_name text, 
     song_title text,
     first_name text,
     PRIMARY KEY ((user_id, session_id), item_in_session)
        )
"""

user_playlist_create = "CREATE TABLE IF NOT EXISTS user_playlist_session "
user_playlist_create += """
    (song_title text, 
     user_id int,
     first_name text,
     last_name text,
     PRIMARY KEY (song_title, user_id)
        )
"""

# select records
query_1 = """
    SELECT artist_name, song_title, length from artist_playlist_session where 
        session_id=338 and item_in_session=4;
"""                   
query_2 = """
    SELECT artist_name, song_title, first_name FROM song_playlist_session 
        WHERE user_id=10 and session_id=182;
"""
query_3 = """
    SELECT first_name, last_name FROM user_playlist_session
        WHERE song_title='All Hands Against His Own';
"""
                    
    
# insert records
artist_playlist_insert = """
    INSERT INTO artist_playlist_session 
    (session_id, item_in_session, artist_name, song_title, length)
     VALUES (%s, %s, %s, %s, %s);
     """
song_playlist_insert = """
    INSERT INTO song_playlist_session 
    (user_id, session_id, item_in_session, artist_name, song_title, first_name)
    VALUES (%s, %s, %s, %s, %s, %s)
     """
user_playlist_insert = """
    INSERT INTO user_playlist_session 
    (song_title, user_id, first_name, last_name)
    VALUES (%s, %s, %s, %s);
    """

# list of queries
create_table_queries = [artist_playlist_create, song_playlist_create, user_playlist_create]
drop_table_queries = [artist_playlist_drop, song_playlist_drop, user_playlist_drop]
insert_table_queries = [artist_playlist_insert, song_playlist_insert, user_playlist_insert]
select_table_queries = [query_1, query_2, query_3]
table_names = ['artist_playlist_session', 'song_playlist_session', 'user_playlist_session']