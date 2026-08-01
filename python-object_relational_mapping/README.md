# Python - Object-relational mapping

## Description
This project introduces Object-Relational Mapping (ORM) in Python. It covers using `MySQLdb` (mysqlclient) for raw SQL queries from Python scripts, and `SQLAlchemy` for object-oriented database interactions and mapping Python classes to MySQL tables.

## Tasks Overview
0. **Get all states**: List all states from `hbtn_0e_0_usa` ordered by `states.id` ASC.
1. **Filter states**: List states with name starting with `N` ordered by `states.id` ASC.
2. **Filter states by user input**: Display state records matching user input argument.
3. **SQL Injection...**: Safe filter for states preventing SQL injection attacks.
4. **Cities by states**: List all cities with state name from `hbtn_0e_4_usa` sorted by `cities.id` ASC.
5. **All cities by state**: List all cities of a specific state given as argument.
6. **First state model**: Class definition of `State` mapping to MySQL table `states`.
7. **All states via SQLAlchemy**: Fetch and print all `State` objects using SQLAlchemy.
8. **First state**: Print the first `State` object sorted by `id`.
9. **Contains a**: List all `State` objects containing the letter `a`.
10. **Get a state**: Search and print `State` object by name.
11. **Add a new state**: Insert state "Louisiana" into database.
12. **Update a state**: Update state name where `id = 2` to "New Mexico".
13. **Delete states**: Delete all `State` objects containing letter `a`.
14. **Cities in state**: Class `City` model and fetch all cities by state using SQLAlchemy.
