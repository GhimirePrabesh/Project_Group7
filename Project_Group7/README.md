# Group7_Project

## Introduction to Project
> As per the DAB 111, this is the project for creating a website reflecting the database derived from the website in a legal manner. Our group has created a website of a supermarket database which includes Revenue with respect to the branches and product lines as well as customer behaviour and satisfaction during the purchase.

## Data Collection and Data Cleaning
> For the project, data was collected from Kaggle and the data is about the Sales revenue of three branches of Super Market in Myanmar.
> Under data cleaning, the column namely date, rating, gross margin percentage and gross income.  

## About Libraries
> For the project following libraries were imported:
>> SQLite3
>> csv
>> pandas
>> flask
>> pathlib

## Procedure followed 
> First of all, Flask was imported for creating the web page and render the templates and SQlite3 was imported for providing the path to connect the database with the help of pathlib. Flask application instances was created as well as three routes was defined namely root index("/") to render index_links.html, '/about' renders about.html template and '/data' to retrive data from supermarket_sales.
> Under "/data", SQlite database was connected to execute the SQL query to retrieve the data from supermarket_sales, fetch result, close database connection and render data.html template with retrieved data.

## About Template
> about.html:
>> The title of the web page was provided by <head><title>About Our Supermarket</title>
>> Two buttons were created namely Homepage and Datasets through <a href="{{ url_for('index') }}"><button>Homepage</button></a> and <a href="{{ url_for('data') }}"><button>Datasets</button></a>.
>> Under style, the alignment of the text was centered and used the Times New Roman font, Times, serif with background color.
>> Under body, various variables under the column head were described. 

> data.html:
>> Under body, column heads was introduced and table body was introduced from the SQlite.

>index_links.html:
>> This is the template for the homepage and various styles are used. <div> which stands for division represents a block-level of the homepage.
   
## Table Creation
> Table was created using SQLite3 providing the column name as per the database.   
