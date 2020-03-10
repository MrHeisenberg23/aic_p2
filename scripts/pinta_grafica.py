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
		array_x = []
		array_y = []
		comprobacion = []
		indice = 0
		her = [i for i in range(200, 3400, 200)]

		for line in fich.readlines():

			media = 0
			contador = 0
			bifurcacion = line.strip().split(":")
			hz = int(bifurcacion[0])

			if hz in her:
				array_x.append(int(bifurcacion[0]))
				for add in bifurcacion[1].split():
					media = media + int(add)
					contador = contador + 1
				array_y.append(media/contador)
				comprobacion.append(contador)

		fich.close()
		print("Datos: ", array_y)
		print("Ejecucion: ", array_x)

		aux = comprobacion[0]
		for i in comprobacion[1:]:
			if aux != comprobacion[i]:
				print("Descuadre en los datos")
				sys.exit()

		explode = []
		scatter = []
		#Once data has been collected, plotting must be done
		for i in range(len(array_x)):
			explode.append(0)
			scatter.append(0.5)

		numero_graficas = 2
		fig, axs = plt.subplots(1, numero_graficas)
		axs[0].plot(array_x, array_y)
		axs[1].pie(array_y, explode, array_x, autopct='%1.1f%%', startangle=90)
		axs[1].legend(title='Freq (Hz)', loc=8, ncol=len(array_x))

		fig.suptitle(sys.argv[-1])
		for ax in range(0, numero_graficas):
			axs[ax].set(xlabel="x - Frequency", ylabel="y - Power")
		for ax in axs.flat:
    			ax.label_outer()
		axs[0].set_title("Graph 1 (Plot)")
		axs[1].set_title("Graph 2 (Pie)")
		plt.axis('equal')
		plt.tight_layout()
		axs[0].grid()
		axs[1].grid()
		plt.show()

	else:
		print("Unknown destination / not a file")

