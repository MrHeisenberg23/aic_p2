#!/bin/bash

#gnome-terminal --tab  --working-directory=$PWD -- /bin/sh -c "pwd; do perf stat -e power/energy-cores/ stress -c 1 -t 3 2> $1; grep -e Joules -e seconds $1 >> aux; kill -USR1 $2"


perf stat -e power/energy-cores/ $2 2> $1 
grep -e Joules -e seconds $1 $2 >> aux 
