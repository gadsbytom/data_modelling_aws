import configparser
import boto3
import os


# CONFIG
config = configparser.ConfigParser()
config.read('dwh.cfg')

# DROP STAGING TABLES
staging_events_table_drop = "DROP TABLE IF EXISTS events;"
staging_songs_table_drop = "DROP TABLE IF EXISTS songs;"

# DROP FINAL TABLES
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"


# CREATE STAGING
staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS events (artist VARCHAR, auth VARCHAR, firstName VARCHAR, gender VARCHAR, itemInSession INT, lastName VARCHAR, length REAL, level VARCHAR, location VARCHAR, method VARCHAR, page VARCHAR, registration REAL, sessionId INT, song VARCHAR, status INT, ts BIGINT, userAgent VARCHAR, userId INT);
""")

staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS songs (num_songs INT, artist_id VARCHAR, artist_latitude REAL, artist_longitude REAL, artist_location VARCHAR, artist_name VARCHAR, song_id VARCHAR, title VARCHAR, duration REAL, year INT);
""")

# CREATE FINAL
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id INT PRIMARY KEY, start_time BIGINT, user_id VARCHAR, \
                        level VARCHAR, song_id VARCHAR, artist_id VARCHAR, session_id INT, location VARCHAR, user_agent VARCHAR);
""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users \
                        (user_id INT PRIMARY KEY, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR);
""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs \
                        (song_id VARCHAR PRIMARY KEY, title VARCHAR, artist_id VARCHAR, year INT, duration REAL);
""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists  \
                        (artist_id VARCHAR, name VARCHAR, location VARCHAR, latitude REAL, longitude REAL);
""")

time_table_create =  ("""CREATE TABLE IF NOT EXISTS time  \
                        (start_time TIMESTAMP WITH TIME ZONE, hour INT, day INT, week INT, month INT, year INT, weekday VARCHAR);
""")


# INSERT FROM S3 TO STAGING TABLES

ARN_ROLE = config.get("IAM_ROLE","ARN")

staging_events_copy = ("""copy events from 's3://udacity-dend/log_data/2018/11/2018' 
credentials 'aws_iam_role={}'
region 'us-west-2'
format as json 'auto';
""").format(ARN_ROLE)

# staging_songs_copy = ("""copy songs from 's3://udacity-dend/song_data' 
# credentials 'aws_iam_role={}'
# region 'us-west-2'
# format as json 'auto';
# """).format(ARN_ROLE)

redshift-cluster-1.cxyldcznxe9e.eu-west-1.redshift.amazonaws.com:5439/sparkify

s3 = boto3.resource('s3',
                       region_name="eu-west-1",
                       aws_access_key_id=os.getenv("AWS_KEY"),
                       aws_secret_access_key=os.getenv("AWS_SECRET")
                   )

songs = s3.Bucket()

s3 = boto3.resource('s3')
bucket = s3.Bucket('prod')
object = bucket.Object('prod2/..')

# INSERT FROM S3 TO FINAL TABLES

# staging_songs_table_create = ("""CREATE TABLE IF NOT EXISTS songs (num_songs INT, artist_id VARCHAR, artist_latitude REAL, artist_longitude REAL, artist_location VARCHAR, artist_name VARCHAR, song_id VARCHAR, title VARCHAR, duration REAL, year INT);
# """)

# staging_events_table_create= ("""CREATE TABLE IF NOT EXISTS events (artist VARCHAR, auth VARCHAR, firstName VARCHAR, gender VARCHAR, itemInSession INT, lastName VARCHAR, length REAL, level VARCHAR, location VARCHAR, method VARCHAR, page VARCHAR, registration REAL, sessionId INT, song VARCHAR, status INT, ts BIGINT, userAgent VARCHAR, userId INT);
# """)

# songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (songplay_id INT PRIMARY KEY, start_time BIGINT, user_id VARCHAR, \
#                         level VARCHAR, song_id VARCHAR, artist_id VARCHAR, session_id INT, location VARCHAR, user_agent VARCHAR);
# """)


# FROM LOG
songplay_table_insert = (""" INSERT INTO songplays \
                    SELECT  ON CONFLICT DO NOTHING;
""")

# FROM LOG
user_table_insert = (""" INSERT INTO users \
                    VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FROM SONG
song_table_insert = (""" INSERT INTO songs \
                    VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FROM SONG
artist_table_insert = (""" INSERT INTO artists \
                    VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")

# FROM LOG
time_table_insert = (""" INSERT INTO time \
                    VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING;
""")


songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")

time_table_insert = ("""
""")

# QUERY LISTS
create_table_queries = [staging_events_table_create, staging_songs_table_create, songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [staging_events_table_drop, staging_songs_table_drop, songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
copy_table_queries = [staging_events_copy, staging_songs_copy]
insert_table_queries = [songplay_table_insert, user_table_insert, song_table_insert, artist_table_insert, time_table_insert]
