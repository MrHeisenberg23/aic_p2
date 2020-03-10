import random
import math
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

		print("Plotting data from file: ", directorio)
		fich = open (directorio,'r')
		data = {i:[[],[]] for i in range(200, 3400, 200)}
		frecuencias_aceptadas = [i for i in range(200, 3400, 200)]
		X = []
		Y = []
		F = []
		alturas = []
		valores_leidos = 0

		#Structure has been established: reading
		fich = open(directorio, 'r')

		array = []
		for lines in fich.readlines():
			bifurcacion = lines.split(":")
			hz_usado = int(bifurcacion[0])

			if hz_usado in frecuencias_aceptadas:
				array.append(len(bifurcacion[1].split()))
				array.append(len(bifurcacion[2].split()))

		pruebas = min(array)
		print("PRUEBAS: ", pruebas)

		fich.seek(0)
		for lines in fich.readlines():

			bifurcacion = lines.split(":")
			hz_usado = int(bifurcacion[0])

			if hz_usado in frecuencias_aceptadas:

				potencia = bifurcacion[1].split()[:pruebas]
				tiempo = bifurcacion[2].split()[:pruebas]

				for i in tiempo:
					Y.append(int(i))

				for i in potencia:
					X.append(int(i))
					F.append(int(hz_usado))
					alturas.append(int(i))

				data[int(hz_usado)][0] = potencia
				data[int(hz_usado)][1] = tiempo
				valores_leidos = valores_leidos + 1

		fich.close()

		#Structure has been filled with data: graphics
		fig = plt.figure(figsize=(5, 4))
		ax = fig.add_subplot(111, projection='3d')

		dx = 30
		dy = 1
		dz = 0

		colores = ['r', 'g', 'c', 'b', 'm', 'y', 'lime', 'hotpink', 'khaki', 'peru', 'navy', 'silver', 'thistle', 'grey', 'tomato', 'k']
		colors = colores[:valores_leidos]

		x = 0
		for i in range(len(X)):
			x = math.floor(i/pruebas)
			ax.bar3d(F[i], Y[i], 0, dx, dy, alturas[i],color=colors[x],shade=False)

		ax.set_xlabel("Frecuencia")
		ax.set_ylabel("Tiempo")
		ax.set_zlabel("Potencia")

		print("Frecuencia: ", F)
		print("X: ", X)
		print("Y: ", Y)

		plt.show()
	else:
		print("Unknown destination / not a file")
