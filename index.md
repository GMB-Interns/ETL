# **ETL Python Pipeline to Google Cloud SQL**

## **Table of Contents**
1. [**Introduction**](#introduction)
2. [**Pre-requisites**](#pre-requisites)
3. [**Creating Your Own User in Google Cloud SQL**](#creating-your-own-user-in-google-cloud-sql)
4. [**Connecting to the PostgreSQL Database**](#connecting-to-the-postgresql-database)
5. [**Executing SQL Queries**](#executing-sql-queries)
6. [**Conclusion**](#conclusion)

<a name='introduction'></a>
## **Introduction**

This guide provides detailed instructions on how to extract, transform, and load (ETL) data into a Google Cloud SQL PostgreSQL database using Python. The steps outlined will help you establish a secure connection to a Cloud SQL instance from a Python environment such as Jupyter Notebook or Google Colab, and then execute SQL queries to interact with the data.

<a name='pre-requisites'></a>
## **Pre-requisites**

Before you can start working with Google Cloud SQL, make sure that you have the following:

1. A Google Cloud project with billing enabled.
2. A Google Cloud SQL instance set up.
3. The necessary Python packages installed: `psycopg2` and `sqlalchemy`.

<a name='creating-your-own-user-in-google-cloud-sql'></a>
## **Creating Your Own User in Google Cloud SQL**

To access the Google Cloud SQL instance, each person should create their own user for security purposes. 

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Select your project.
3. Navigate to SQL from the left navigation menu.
4. Click on the SQL instance you want to connect to.
5. Go to the "Users" section.
6. Click "Create user account".
7. Fill in the "User details" form with your preferred username and password.
8. Click "Create".

Now you have your own user credentials to connect to the database.

<a name='connecting-to-the-postgresql-database'></a>
## **Connecting to the PostgreSQL Database**

Once your user is created, you can use the following Python script to connect to the PostgreSQL database, named 'gmb' in this case:

```python
import psycopg2

# replace with your actual details
username = 'your_username'
password = 'your_password'
public_ip_address = 'your_public_ip_address'
db_name = 'gmb'

# create a connection
conn = psycopg2.connect(
    dbname=db_name,
    user=username,
    password=password,
    host=public_ip_address
)

# create a cursor
cur = conn.cursor()
```

## **Executing SQL Queries**
With a connection established, you can now execute SQL queries on your database:

```python
# SQL query to get all table names in the 'gmb' database
query = """
SELECT tablename 
FROM pg_catalog.pg_tables 
WHERE schemaname != 'pg_catalog' AND 
      schemaname != 'information_schema';
"""

# execute the query
cur.execute(query)

# fetch all the results
tables = cur.fetchall()

# print the table names
for table in tables:
    print(table[0])
```
Don't forget to close the cursor and connection after you're done:

```
# close the cursor and the connection
cur.close()
conn.close()
```
