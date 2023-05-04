import os
import shutil

actdir = input("Ordner zum machen:")
os.chdir(actdir)

mykorr=["Team 1", "Team 2"]

for (dirpath, dirnames, filenames) in os.walk("."):
	for name in dirnames:
		if name not in mykorr:
			shutil.rmtree(os.path.join(os.getcwd(),name))
	break #to stop recursive
