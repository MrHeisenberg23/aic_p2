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
		pruebas = 7
		print("Plotting data from file: ", directorio)
		fich = open (directorio,'r')
		data = {i:[[],[]] for i in range(200, 3400, 200)}
		print("Our dictionary is empty:", data)
		data_x_y = []
		data_y_z = []
		X = []
		Y = []
		F = []

		#Structure has been established: reading
		fich = open(directorio, 'r')
		for lines in fich.readlines():
			potencia_int = []
			tiempo_int = []
			bifurcacion = lines.split(":")
			hz_usado = bifurcacion[0]
			potencia = bifurcacion[1].split()[:pruebas]
			tiempo = bifurcacion[2].split()[:pruebas]

			for i in potencia:
				potencia_int.append(int(i))
				Y.append(int(i))

			for i in tiempo:
				tiempo_int.append(int(i))
				X.append(int(i))
				F.append(int(hz_usado))


			data[int(hz_usado)][0] = potencia_int
			data[int(hz_usado)][1] = tiempo_int
			data_x_y.append(potencia_int)
			data_y_z.append(tiempo_int)
		print("Our dictionary once filled: ", data)

		#Structure has been filled with data: graphics
		fig = plt.figure()
		ax = fig.add_subplot(111, projection='3d')

		frecuencias = []
		frecuencias_3d = []
		for i in range(200, 3400, 200):
			frecuencias.append(i)

		#for i in range(200, 3400, 200):
		#	frecuencias_3d.append(frecuencias)
		frecuencias_3d = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200]
		dx = dy = dz = 25
		ax.bar3d(F, X, Y, dx, dy, dz,color='#00ceaa')

		ax.set_xlabel("Frecuencia")
		ax.set_ylabel("Tiempo")
		ax.set_zlabel("Potencia")
#		ax.set_xlim(2000)
#		ax.set_ylim(50)
#		ax.set_zlim(50)
		print(len(X))
		print(len(Y))
		print(len(F))

		plt.show()
	else:
		print("Unknown destination / not a file")
