
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

<img src="https://user-images.githubusercontent.com/69240351/265285425-6d3ed1e6-78ff-4aae-94db-6ca9c6ab76dc.png" align="center" width="40%" height="40%"/>

# Installation
```
colorama==0.4.6
```
To install the requirements run:
```
pip install -r requirements.txt
```


# Commands and Syntax

Data Buddy Commands

```

├── table
│   ├── create <table_name>
│   ├── add
│   │   ├── row <table_name> <row_name>
│   │   └── value <table_name> <row_name> <value>
│   ├── delete table <table_name>
│   ├── list
│   │   ├── table
│   │   ├── row <table_name>
│   │   └── values <table_name> <row_name>
│   ├── remove
│   │   ├── row <table_name> <row_name>
│   │   └── value (Coming Soon)
│   ├── rename
│   │   ├── row <table_name> <old_row_name> <new_row_name>
│   │   └── table <old_table_name> <new_table_name>
│   └── export (Coming Soon)
└── exit

```