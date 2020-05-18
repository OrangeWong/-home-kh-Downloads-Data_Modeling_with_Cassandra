# drop keyspace
drop_keyspace_query = "DROP KEYSPACE IF EXISTS project2"

# create keyspace
create_keyspace_query = """
    CREATE KEYSPACE project2 WITH replication = {
        'class': 'SimpleStrategy', 
        'replication_factor' : 1
        };
    """
# drop tables
music_history_1_drop = "DROP TABLE IF EXISTS music_history_1"
music_history_2_drop = "DROP TABLE IF EXISTS music_history_2"
music_history_3_drop = "DROP TABLE IF EXISTS music_history_3"

# create tables
music_history_1_create = "CREATE TABLE IF NOT EXISTS music_history_1 "
music_history_1_create += """
    (artist_name text, 
     first_name text,
     gender text,
     item_in_session int,
     last_name text,
     length float,
     level text,
     location text, 
     session_id int,
     song_title text,
     user_id int,
     PRIMARY KEY ((session_id, item_in_session), artist_name, song_title)
        )
"""
music_history_2_create = "CREATE TABLE IF NOT EXISTS music_history_2 "
music_history_2_create += """
    (artist_name text, 
     first_name text,
     gender text,
     item_in_session int,
     last_name text,
     length float,
     level text,
     location text, 
     session_id int,
     song_title text,
     user_id int,
     PRIMARY KEY ((user_id, session_id), item_in_session, song_title)
        )
"""

music_history_3_create = "CREATE TABLE IF NOT EXISTS music_history_3 "
music_history_3_create += """
    (artist_name text, 
     first_name text,
     gender text,
     item_in_session int,
     last_name text,
     length float,
     level text,
     location text, 
     session_id int,
     song_title text,
     user_id int,
     PRIMARY KEY (song_title, user_id, session_id, item_in_session)
        )
"""

# select records
query_1 = """
    SELECT artist_name, song_title, length from music_history_1 where 
        session_id=338 and item_in_session=4;
"""                   
query_2 = """
    SELECT artist_name, song_title, first_name FROM music_history_2
        WHERE user_id=10 and session_id=182;
"""
query_3 = """
    SELECT first_name, last_name FROM music_history_3
        WHERE song_title='All Hands Against His Own';
"""
                    
    
# insert records
music_history_1_insert = """INSERT INTO music_history_1 
    (artist_name, first_name, gender, item_in_session, last_name,
     length, level, location, session_id, song_title, user_id) 
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
     """
music_history_2_insert = """INSERT INTO music_history_2 
    (artist_name, first_name, gender, item_in_session, last_name,
     length, level, location, session_id, song_title, user_id) 
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
     """
music_history_3_insert = """INSERT INTO music_history_3 
    (artist_name, first_name, gender, item_in_session, last_name,
     length, level, location, session_id, song_title, user_id) 
     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
     """

# list of queries
create_table_queries = [music_history_1_create, music_history_2_create, music_history_3_create]
drop_table_queries = [music_history_1_drop, music_history_2_drop, music_history_3_drop]
insert_table_queries = [music_history_1_insert, music_history_2_insert, music_history_3_insert]
select_table_queries = [query_1, query_2, query_3]
table_names = ['music_history_1', 'music_history_2', 'music_history_3']