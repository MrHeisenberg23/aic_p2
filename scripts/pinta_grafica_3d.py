import sys
import pathlib
import os.path
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv) != 2:
	print("The arguments passed: ", str(sys.argv), "are incorrect")
else:
	directorio = pathlib.Path.cwd().joinpath('ficheros', sys.argv[len(sys.argv)-1])
	if(os.path.isfile(directorio)):
		print("Plotting data from file: ", directorio)
		fich = open (directorio,'r')
        	data =
			{k : for k in range(200, 3600, 200):
				listoflists = []
				for i in range(0,2):
					sublist = []
					for j in range(0,10)
						sublist.append((i,j))
						listoflists.append(sublist)
        	}
	else:
		print("Unknown destination / not a file")
