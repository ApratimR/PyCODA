import os

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

main_db_location = "database/main.txt"
currentdb=None

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




#default check for basic setup
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
		print("invalid option")


#the creating class
class create:
	global main_db_location
	global currentdb
	def table(names,database=None):
		#FIXME need some serious work here
		if database == None:
			database = currentdb
		if database == None:
			raise Exception("No database selected for creating tables operation")
		for attribute_name in names:
			open("database/"+currentdb+"/"+attribute_name+".txt","x")
			list_modify = open("database/"+currentdb+"/"+"main.txt","a")
			list_modify.write(attribute_name+"\n")
			list_modify.close()

		else:
			raise Exception("Database name not found")

	#this creates the database folder
	def database(name):
		list_of_db = open(main_db_location,"r")
		if (name+"\n") in list_of_db:
			#throw error
			list_of_db.close()
			raise Exception("Database name already exist")
		else:
			list_of_db.close()
			db_list_modify = open(main_db_location,"a")
			db_list_modify.write(name+"\n")
			os.mkdir("database/"+name)
			db_list_modify.close()
			open("database/"+name+"/main.txt","x")

if __name__ != "__main__":
	check(0)