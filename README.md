# ETL project

## Purpose of the database
More ETL work from Udacity's Data Engineering Nanodegree. Ficticious firm Sparkify want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. The repo is tasked with building an ETL pipeline that extracts the data from S3, stages it in Redshift, and transforms data into a set of dimensional tables.  

## Assumption of the pipeline
Redshift cluster has been created and IAM role and endpoint details are added to the config file, `dwh.cfg`

## Analytic goals
Sparkify's analytics team will analyze the data they've been collecting on songs and user activity on their new music streaming app.

## Data
Data is from the [million songs dataset](http://millionsongdataset.com/)

## Database design
The database is split into two schemas, staging and final.

### Staging schema
The staging schema loads events data into one event staging table, and song data into one song table.

### Staging tables:

#### events - colname, datatype, constraint:
* artist VARCHAR 
* auth VARCHAR 
* firstName VARCHAR
* gender VARCHAR
* itemInSession INT
* lastName VARCHAR
* length REAL
* level VARCHAR
* location VARCHAR
* method VARCHAR
* page VARCHAR
* registration REAL
* sessionId INT
* song VARCHAR
* status INT
* ts BIGINT
* userAgent VARCHAR
* userId INT

#### songs - colname, datatype, constraint:
* num_songs INT
* artist_id VARCHAR
* artist_latitude REAL
* artist_longitude REAL
* artist_location VARCHAR
* artist_name VARCHAR
* song_id VARCHAR
* title VARCHAR
* duration REAL
* year INT

### Final schema. 
The final schema follows the star schema principle. The tables are listed below:

### Fact tables:

#### songplays - colname, datatype, constraint:
* songplay_id INT PRIMARY KEY
* start_time BIGINT
* user_id VARCHAR
* level VARCHAR
* song_id VARCHAR
* artist_id VARCHAR
* session_id INT
* location VARCHAR
* user_agent VARCHAR

### Dimension tables:

#### users - colname, datatype, constraint:
* user_id INT PRIMARY KEY
* first_name VARCHAR
* last_name VARCHAR
* gender VARCHAR
* level VARCHAR

#### songs  - colname, datatype, constraint:
* song_id VARCHAR PRIMARY KEY
* title VARCHAR
* artist_id VARCHAR
* year INT
* duration REAL

#### artists - colname, datatype, constraint:
* artist_id VARCHAR
* name VARCHAR
* location VARCHAR
* latitude REAL
* longitude REAL

#### time - colname, datatype, constraint:
* start_time TIMESTAMP WITH TIME ZONE
* hour INT
* day INT
* week INT
* month INT
* year INT
* weekday VARCHAR

## Code:

### Functional content
* create_tables.py - connects to redshift, drops and creates schemas, dbs and tables
* etl.py - copies json data from s3 buckets into redshift staging, transforms and loads into the final (star) schema. DUPLICATE ENTRIES are handled with ON CONFLICT DO NOTHING. 
* sql_queries - all sql code resides here and is called from the above two modules.

## How to use:
* create a redshift cluster via AWS, note its endpoint details
* open dwh.cfg and overwrite CLUSTER>HOST, DB_NAME, DB_USER, DB_PASSWORD, and DB_PORT, with the relevant details.
* in a terminal in `/home/workspace`, run `python etl.py`


# TO-DO:
* boto3 - create cluster, IAM role, and assign endpoint and ARN to the pipeline
* `INSERT INTO final.users SELECT DISTINCT userId, firstName, lastName, gender, level from staging.events WHERE userId IS NOT NULL;` should be replaced with `...WHERE userId NOT IN (SELECT DISTINCT userId from final.users)` - first statement if any details about the user change they will assume to have a new identity - e.g. if level changes, it doesn't mean the user is new, but our insert will assume these two rows are different.
* speed up s3 insert statement
