import shutil

try:
	shutil.rmtree("database")
	print("folder deleted")
except:
	print("folder to be deleted al ready deleted or error??")