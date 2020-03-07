#!/bin/bash
if [ -f "auxiliar1" ]; then
	rm auxiliar*
	rm aux
fi
muestras=$1
touch aux
for i in `seq 1 1 $muestras`; do
	touch auxiliar$i
	./volcado.sh auxiliar$i
done
sleep 11
./columna_Joules.sh
