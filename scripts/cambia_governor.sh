#!/bin/bash
if [ $# -eq 1 ]; then
	sudo modprobe msr
	sudo wrmsr -a 0x1a0 0x4000850089
	sudo cpupower frequency-set -g userspace
	sudo cpupower frequency-set -f $1GHz
fi
