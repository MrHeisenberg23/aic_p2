#!/bin/bash
trap contador=$((contador+1)) SIGUSR1
if [ -f "auxiliar1" ]; then
	rm auxiliar*
	rm aux
fi
muestras=$1
contador=0
touch aux
sortpid=$$
echo "PID de la terminal original: $sortpid"
for i in `seq 1 1 $muestras`; do
	touch auxiliar$i
	./volcado.sh auxiliar$i $sortpid
done
while [ $contador -ne $muestras ]; do
	echo "esperando finalizacion: contador a $contador."
	sleep 1
done
echo "Tareas finalizadas"
./columna_Joules.sh
