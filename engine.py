import os
import pandas as pd

"""
principal layout
*.  use database folder
*. use a main table handler table named "main"


    SELECT - extracts data from a database
    UPDATE - updates data in a database
    DELETE - deletes data from a database
    INSERT INTO - inserts new data into a database
    CREATE DATABASE - creates a new database
    ALTER DATABASE - modifies a database
    CREATE TABLE - creates a new table
    ALTER TABLE - modifies a table
    DROP TABLE - deletes a table
    CREATE INDEX - creates an index (search key)
    DROP INDEX - deletes an index

"""
def check(option):
    main_db_location = "database/main.txt"
    if option == 0:
        try:
            main_db_open = open(main_db_location,"r")
            main_db_open.close()
        except FileNotFoundError:
            check(1)
    elif option==1:
        os.mkdir("database")
        main_db_create = open(main_db_location,"w")
        main_db_create.close()
    else:
        print("invalid option")