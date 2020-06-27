import os
import shutil

"""
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

#global variables ========================================================================
main_db_location = "database/main.txt"
currentdb=None
#global variables ========================================================================


#the error ===============================================================================

#these are the database errors
def errDatabaseAlreadyExist(name):
	raise Exception(f"database of the name '{name}' already exist ")

def errDatabaseNotFound(name):
	raise Exception(f"database of the name '{name}' not found")

def errDatabaseNotSelected():
	raise Exception("No database selected for operation or in current DB view")


#these are the option errors
def errInvalidOptionSelected():
	raise Exception("please select a valid option")

#these are the table errors


#the error ===============================================================================

	

# changes the global view of selected db
def select_database(name=None):
	global currentdb
	if name==None:
		raise Exception("Please enter a Database Name")
	else:
		list_of_db = open(main_db_location,"r")
		if name+"\n" in list_of_db:
			list_of_db.close()
			currentdb = name
		else:
			raise Exception("Database name not found")



#create the table in the database 
def create_table(names,database=None):
	global currentdb
	if database == None:
		if currentdb != None:
			database = currentdb
		else:
			errDatabaseNotSelected()
	
	if check_databaseName_in_mainDatabase(database)==True:
		for attribute_name in names:
			open("database/"+currentdb+"/"+attribute_name+".txt","x")
			list_modify = open("database/"+currentdb+"/"+"main.txt","a")
			list_modify.write(attribute_name+"\n")
			list_modify.close()
	else:
		errDatabaseNotFound(database)



# creates the database folder

def create_database(name):
	if check_databaseName_in_mainDatabase(name) == True:
		errDatabaseAlreadyExist(name)
	else:
		db_list_modify = open(main_db_location,"a")
		db_list_modify.write(name+"\n")
		os.mkdir("database/"+name)
		db_list_modify.close()
		open("database/"+name+"/main.txt","x")



# default check for basic setup
def check(option=0):
	global main_db_location
	if option == 0:
		try:
			main_db_open = open(main_db_location,"r")
		except FileNotFoundError:
			check(1)

	elif option==1:
		os.mkdir("database")
		main_db_create = open(main_db_location,"x")
		main_db_create.close()
		main_db_open = open(main_db_location,"r")
	else:
		check(0)



# drops the database
def delete_database(database=None):
	global currentdb
	if database == None:
		if currentdb != None:
			database = currentdb
		else:
			errDatabaseNotSelected()
	if check_databaseName_in_mainDatabase(database)==True:
		#this if if database name found then delete operations here
		shutil.rmtree("database/"+database)
		#TODO : to make a mechasim of reading the master main.txt and remove the current 
		#name from it
	else:
		errDatabaseNotFound(database)



# checks for a name in the main database
def check_databaseName_in_mainDatabase(name=currentdb):
	global main_db_location
	list_of_db = open(main_db_location,"r")
	if (name+"\n") in list_of_db:
		list_of_db.close()
		return True
	else:
		list_of_db.close()
		return False


#the main import default check============================================================
if __name__ != "__main__":
	check(0)
#the main import default check============================================================