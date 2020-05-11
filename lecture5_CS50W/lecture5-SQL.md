# Lecture5 - SQL

- [Lecture5 - SQL](#lecture5---sql)
  - [Introduction](#introduction)
    - [Data](#data)
    - [SQLite Types:](#sqlite-types)
    - [MySQL Types:](#mysql-types)
    - [SQL Commands](#sql-commands)

## Introduction

Python Classes are referred ti as Models in SQL!
Migrations are techniques that allow us to make changes to the underlying database! 

### Data
A relational database will have rows and columns.  

SQLite is the Django default! 
Each database can store its own type depending on its use. 

### SQLite Types:
- Text
- Numeric
- Integer
- Real
- Blob (Binary Large Object)

### MySQL Types:
- CHAR(size) => Fixed size of characters
- VARCHAR(size) => Variable size of characters (up to 'size')
- SMALLINT
- INT
- BIGINT
- FLOAT
- DOUBLE

### SQL Commands
Let's have a look at how we would represent this table in SQLite

|origin   |destination|duration|
|---------|-----------|--------|
|New York |London     |415     |
|New York |Paris      |450     |
|London   |Dubai      |500     |
|Vienna   |Warsaw     |120     | 

Here is how you would create a SQLite table:
```
CREATE TABLE flights(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    origin TEXT NOT NULL
    destination TEXT NOT NULL
    duration INTEGER NOT NULL
);
```