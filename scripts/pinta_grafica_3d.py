import random
import sys
import pathlib
import os.path
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

if len(sys.argv) != 2:
	print("The arguments passed: ", str(sys.argv), "are incorrect")
else:
	directorio = pathlib.Path.cwd().joinpath('ficheros', sys.argv[len(sys.argv)-1])
	if(os.path.isfile(directorio)):
		pruebas = 4
		print("Plotting data from file: ", directorio)
		fich = open (directorio,'r')
		data = {i:[[],[]] for i in range(200, 3400, 200)}
		print("Our dictionary is empty:", data)
		data_x_y = []
		data_y_z = []

		#Structure has been established: reading
		fich = open(directorio, 'r')
		for lines in fich.readlines():
			potencia_int = []
			energia_int = []
			bifurcacion = lines.split(":")
			hz_usado = bifurcacion[0]
			potencia = bifurcacion[1].split()[:pruebas]
			energia = bifurcacion[2].split()[:pruebas]

			for i in potencia:
				potencia_int.append(int(i))

			for i in energia:
				energia_int.append(int(i))

			data[int(hz_usado)][0] = potencia_int
			data[int(hz_usado)][1] = energia_int
			data_x_y.append(potencia_int)
			data_y_z.append(energia_int)
		print("Our dictionary once filled: ", data)

		#Structure has been filled with data: graphics
		fig = plt.figure()
		ax = fig.gca(projection='3d')

		# Make data.
		X, Y = np.meshgrid(data_x_y, data_y_z)

		R = np.sqrt(X**2 + Y**2)
		Z = np.sin(R)

		# Plot the surface.
		graph = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

		ax.set_ylim(0,20)
		ax.set_xlim(0,20)

		# Customize the z axis.
		ax.set_zlim(0, 20)
		ax.zaxis.set_major_locator(LinearLocator(10))
		ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

		# Add a color bar which maps values to colors.
		fig.colorbar(graph, shrink=0.5, aspect=5)

		plt.show()
	else:
		print("Unknown destination / not a file")
