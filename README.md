
<h1 align="center">
    Data Buddy
    <br>
    <div align="center">
    <img src="https://img.shields.io/badge/Python-3.10.6-blue" align="center"/>
    <img src="https://img.shields.io/badge/Developing-Active-brightgreen" align="center"/>
    <img src="https://img.shields.io/badge/Version-0.0-green" align="center"/>
    </div>
</h1>

Data Buddy is a versatile command-line tool designed to simplify data management and processing tasks. It empowers users to effortlessly create, edit, and manipulate data tables, enabling seamless data input, processing, and export operations.

<img src="https://user-images.githubusercontent.com/69240351/265285425-6d3ed1e6-78ff-4aae-94db-6ca9c6ab76dc.png" width="40%" height="40%"/>

# Installation
```
discord.py==2.1.1
Flask==2.0.1
```
To install the requirements run:
```
pip install -r requirements.txt
```


# Commands and Syntax

Data Buddy provides a set of commands to manage and manipulate data tables efficiently. Below is a list of available commands along with their syntax and descriptions:

1. table create
Create a new data table.

Syntax:

lua
Copy code
table create <table_name>
<table_name>: The name of the table you want to create.
Example:

lua
Copy code
Data Buddy >> table create sales_data
2. table add row
Add a new row to an existing data table.

Syntax:

sql
Copy code
table add row <table_name> <row_name>
<table_name>: The name of the table where you want to add a row.
<row_name>: The name of the new row to add.
Example:

sql
Copy code
Data Buddy >> table add row sales_data Q1_2023
3. table add value
Add a new value to a specific row in a data table.

Syntax:

php
Copy code
table add value <table_name> <row_name> <value>
<table_name>: The name of the table where you want to add a value.
<row_name>: The name of the row to which you want to add a value.
<value>: The value you want to add.
Example:

sql
Copy code
Data Buddy >> table add value sales_data Q1_2023 55000
4. table delete table
Delete an entire data table.

Syntax:

sql
Copy code
table delete table <table_name>
<table_name>: The name of the table you want to delete.
Example:

sql
Copy code
Data Buddy >> table delete table sales_data
5. table list table
List all available data tables.

Syntax:

css
Copy code
table list table
Example:

css
Copy code
Data Buddy >> table list table
6. table list row
List all rows within a specific data table.

Syntax:

sql
Copy code
table list row <table_name>
<table_name>: The name of the table for which you want to list rows.
Example:

sql
Copy code
Data Buddy >> table list row sales_data
7. table list values
List all values within a specific row of a data table.

Syntax:

php
Copy code
table list values <table_name> <row_name>
<table_name>: The name of the table containing the row.
<row_name>: The name of the row for which you want to list values.
Example:

sql
Copy code
Data Buddy >> table list values sales_data Q1_2023
8. table remove row
Remove a specific row from a data table.

Syntax:

lua
Copy code
table remove row <table_name> <row_name>
<table_name>: The name of the table from which you want to remove a row.
<row_name>: The name of the row to remove.
Example:

lua
Copy code
Data Buddy >> table remove row sales_data Q1_2023
9. table rename row
Rename a specific row within a data table.

Syntax:

php
Copy code
table rename row <table_name> <old_row_name> <new_row_name>
<table_name>: The name of the table containing the row.
<old_row_name>: The current name of the row.
<new_row_name>: The new name for the row.
Example:

lua
Copy code
Data Buddy >> table rename row sales_data Q1_2023 Q2_2023
10. table rename table
Rename an existing data table.

Syntax:

lua
Copy code
table rename table <old_table_name> <new_table_name>
<old_table_name>: The current name of the table.
<new_table_name>: The new name for the table.
Example:

lua
Copy code
Data Buddy >> table rename table sales_data new_sales_data
These commands and their syntax make Data Buddy a powerful tool for managing and manipulating data tables with ease.
