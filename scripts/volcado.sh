#!/bin/bash
gnome-terminal --tab --title="Script" --working-directory="/home/cristian/p2_AIC/scripts" -- /bin/sh -c "pwd; do perf stat -e power/energy-cores/ stress -c 1 -t 10 2> $1; grep Joules $1 >> aux"
