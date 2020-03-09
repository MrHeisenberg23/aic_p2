#!/bin/bash

captura_trap(){
	contador=$((contador+1))
	echo "Capturada la señal"
}

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

trap captura_trap USR1

muestras=$1
touch aux volcado_datos
sortpid=$$
echo "PID de la terminal original: $sortpid"
for i in `seq 1 1 $muestras`; do
	touch auxiliar$i
	./volcado.sh auxiliar$i $sortpid
done
until [ $contador -eq $muestras ]; do
	: #busy-wait
done
echo "Tareas finalizadas"
./columna_Joules.sh
