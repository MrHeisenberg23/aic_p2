import plotly.graph_objects as go
import random
import math
import sys
import pathlib
import os.path

if len(sys.argv) != 2:
	print("The arguments passed: ", str(sys.argv), "are incorrect")
else:
	directorio = pathlib.Path.cwd().joinpath('ficheros', sys.argv[len(sys.argv)-1])
	if(os.path.isfile(directorio)):
		pruebas = 7
		print("Plotting data from file: ", directorio)
		frecuencias_aceptadas = [i for i in range(200, 3400, 200)]

		#Structure has been established: reading
		fich = open(directorio, 'r')

		tiempos = []
		energias = []
		porcentaje_ceros = []
		hz_usado = int(fich.readline())

		if hz_usado not in frecuencias_aceptadas:
			sys.exit()

		contador = 0

		for lines in fich.readlines():
			separacion=lines.split(":")
			porcentaje_ceros.append(separacion[0])
			tiempo=separacion[1].split()
			energia=separacion[2].split()

			if len(tiempo) != len(energia):
				sys.exit()

			for i in range(len(energia)):
				tiempo[i]=int(tiempo[i])
				energia[i]=int(energia[i])

			contador = contador + 1
			tiempos.append(tiempo)
			energias.append(energia)

		fich.close()

		fig = go.Figure()

		for i in range(len(tiempos)):
			fig.add_trace(go.Scatter(x=tiempos[i], y=energias[i], mode='lines+markers',name=str(porcentaje_ceros[i]) + "percent of zeros"))

		fig.show()

	else:
		print("Unknown destination / not a file")
