### Project: Data Warehouse

#### Introduction
A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app. We need to build an ETL pipeline that extracts their data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights in what songs their users are listening to. Test your database and ETL pipeline by running queries given by the analytics team from Sparkify and compare results with expected results.

#### Project Description
Build an ETL pipeline for a database hosted on Redshift. Load data from S3 to staging tables on Redshift and execute SQL statements that create the analytics tables from these staging tables.

#### Project Datasets

Song data: s3://udacity-dend/song_data
Log data: s3://udacity-dend/log_data
Log data json path: s3://udacity-dend/log_json_path.json

Data is originally from the [Million songs dataset](http://millionsongdataset.com/)


## Project steps:

### Create Table Schemas
* Design schemas for fact and dimension tables
* Write SQL CREATE statement for each of the tables in sql_queries.py
* Complete the logic in create_tables.py to connect to the database and create these tables
* Write SQL DROP statements to drop tables in the beginning of create_tables.py if the tables already exist. 
* Launch a redshift cluster and create an IAM role that has read access to S3.
* Add redshift database and IAM role info to dwh.cfg.
* Test by running create_tables.py and checking the table schemas in your redshift database.

#### Build ETL Pipeline
* Load data from S3 to staging tables on Redshift.
* Load data from staging tables to analytics tables on Redshift.
* Test etl.py after running create_tables.py and then run the analytic queries on the Redshift database
* Delete redshift cluster when finished.

##### README contents
* Explain the purpose of the database, schema design and ETL pipe
* Discuss the purpose of this database in context of the startup, Sparkify, and their analytical goals.
* State and justify your database schema design and ETL pipeline.
* optional - Provide example queries and results for song play analysis.
