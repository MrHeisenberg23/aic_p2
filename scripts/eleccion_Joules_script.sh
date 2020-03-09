
#!/bin/bash

if [ $# -ne 1 ]; then
	echo "necesita dos parametros"
	exit 1
fi

if [ -f "auxiliar1" ]; then
	rm auxiliar*
	rm aux
	rm volcado_datos
fi

contador=0

trap "contador=$((contador+1))" USR1

muestras=$1
touch aux volcado_datos
sortpid=$$
echo "PID de la terminal original: $sortpid"
for i in `seq 1 1 $muestras`; do
	touch auxiliar$i
	./volcado.sh auxiliar$i $sortpid
	sleep 1
done
until [ $contador -eq $muestras ]; do
	echo "Waiting, count: $contador"
	sleep 1
done
echo "Tareas finalizadas"
./columna_Joules.sh
