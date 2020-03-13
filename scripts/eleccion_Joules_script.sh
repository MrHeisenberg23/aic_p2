#!/bin/bash


#tipos de resultados
#1 	frecuencia:energia:tiempo

#2 	frecuencia
#	porcentaje_ceros:tiempo:potencia/energia

#3	frecuencia:potencia

freq=200
contador=0
muestras=$2

sortpid=$$
echo "PID de la terminal original: $sortpid"

captura_trap(){
	contador=$((contador+1))
	echo "Capturada la señal"
}

if [ $# -ne 4 ]; then
	echo "necesita 3 parametros"
	echo "tipo_salida numero_ejecuciones comando"
	exit 1
fi

if [ -f "auxiliar1" ]; then
	touch aux2
	touch resultado
	rm auxiliar*
	rm aux
	rm aux2
	rm volcado_datos
	rm resultado
fi


trap captura_trap USR1

cpu.sh $freq

touch aux volcado_datos

for i in `seq 1 1 $muestras`; do
	touch auxiliar$i
	sudo ./volcado.sh auxiliar$i $3 $4 &>/dev/null &
done

wait

echo "Tareas finalizadas"

./columna_Joules.sh

#sudo apt-get install num-utils
tiempo=$(awk 'NR % 2 == 0' volcado_datos | numaverage)

perf stat -e power/energy-cores/ sleep $tiempo 2> aux

grep -e Joules aux >> aux2

energia=$(awk '{print $1}' aux2)

muestras=$(($muestras*2))
nejec=1
for i in `seq 1 2 $muestras`;do
	var=$(cat -n volcado_datos | tr -s ' ' | grep -w '^ '$i | awk '{print $2}')
	resultado=$(./resta $var $energia)
	j=$(($i+1))
	tiempo=$(cat -n volcado_datos | tr -s ' ' | grep -w '^ '$j | awk '{print $2}')

	if [$1=1];then
		echo "$freq:$resultado:$tiempo"
		echo "$freq:$resultado:$tiempo" >> resultado
	fi
	if [$1=2];then
		if[$i=1];then+
			echo "$freq"
		fi
		echo "ejecucion $nejec: $resultado	$tiempo"
		echo "ejecucion $nejec: $resultado	$tiempo" >> resultado
	fi
	if [$1=3];then
		potencia=$(($resultado/$tiempo))
		echo "$freq:$potencia"
		echo "$freq:$potencia" >> resultado
	fi

	nejec=$(($nejec+1))
done
