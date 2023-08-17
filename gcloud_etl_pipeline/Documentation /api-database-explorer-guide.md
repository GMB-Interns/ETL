# **API Database Explorer Guide**
A user-friendly interface for exploring tables in a Google Cloud Platform database. This guide explains the step-by-step process of creating a web application that enables users to easily view the tables and sample data.

## **Table of Contents**
1. [**Introduction**](#introduction)
2. [**Connecting to Google Cloud Platform**](#connecting-to-google-cloud-platform)
3. [**Building the Web Application**](#building-the-web-application)
   - [**Setting Up the Environment**](#setting-up-the-environment)
   - [**Creating the FastAPI Application**](#creating-the-fastapi-application)
   - [**Designing the Templates**](#designing-the-templates)
4. [**Deploying the Application**](#deploying-the-application)
5. [**Conclusion**](#conclusion)

<a name='introduction'></a>
## **Introduction**
The purpose of this project is to allow users, especially non-technical stakeholders, to easily view and explore the tables in a database hosted on Google Cloud Platform (GCP). This includes viewing the table names and previewing sample data.

<a name='connecting-to-google-cloud-platform'></a>
## **Connecting to Google Cloud Platform**
### **Establishing the Connection**
We use the psycopg2 library to connect to the PostgreSQL database hosted on GCP. The connection requires specifying the username, password, public IP address, and database name.

```python
username = 'gmb'
password = 'your-password' 
public_ip_address = 'xxxxxxxxxxxx'
db_name = 'gmb'

conn = psycopg2.connect(
    dbname=db_name,
    user=username,
    password=password,
    host=public_ip_address
)
```
<a name='building-the-web-application'></a>

## **Setting Up the Environment**
We use FastAPI, a modern web framework, to build the web application. Templates are rendered using the Jinja2 templating engine.


< a name='Creating the FastAPI Application'></a>

## **Defining the Endpoints**
**Welcome Page:** A welcome page to greet the users.
**Tables Page:** Lists all the tables in the database.
**Sample Data Page:** Displays a sample of data from the selected table.
Here's how the endpoints are defined:

```python 
@app.get("/tables", response_class=HTMLResponse)
def get_tables(request: Request, cursor=Depends(get_cursor)):
  ...

@app.get("/sample-data/{table_name}", response_class=HTMLResponse)
def sample_data(request: Request, table_name: str, cursor=Depends(get_cursor)):
  ...
```

<a name='designing-the-templates'></a>

We use HTML templates with Jinja2 to render the pages. For example, the tables.html file lists all the available tables, and users can select a table to view its sample data.

<a name='deploying-the-application'></a>

The application can be run locally for development and can be deployed to a suitable hosting platform for production use.

<a name='conclusion'></a>

This project simplifies the process of exploring tables within a database. By connecting to a GCP-hosted PostgreSQL database and utilizing FastAPI and Jinja2, we create an accessible web interface for users to view and understand their data.
