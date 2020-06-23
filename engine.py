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

def select_database(mode="select",name=None):
	if mode =="select":
		if name==None:
			raise Exception("Please enter a Database Name")
		else:
#TODO make method to check the main db list and set a global varaible
			pass



def check(option=0):
	global main_db_location
	if option == 0:
		try:
			main_db_open = open(main_db_location,"r")
#            main_db_open.close()
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
	def table(Database,collum_amount,names):
		list_of_db = open(main_db_location,"r")
		if Database+"\n" in list_of_db:
			list_of_db.close()
#TODO start with error handling if file already exist


			for attribute_name in names:
				open("database/"+Database+"/"+attribute_name+".txt","x")
				list_modify = open("database/"+Database+"/"+"main.txt","a")
				list_modify.write(attribute_name+"\n")
				list_modify.close()

		else:
			raise Exception("Database name not found")

	#this creates the database folder
	def database(name):
		list_of_db = open(main_db_location,"r")
		if (name+"\n") in list_of_db:
			#throw errir
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