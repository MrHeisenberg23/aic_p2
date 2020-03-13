#!/usr/bin/env bash
sudo cpufreq-set -f $1GHz -c 0
sudo cpufreq-set -f $1GHz -c 1
sudo cpufreq-set -f $1GHz -c 2
sudo cpufreq-set -f $1GHz -c 3
sudo cpufreq-set -f $1GHz -c 4
sudo cpufreq-set -f $1GHz -c 5
sudo cpufreq-set -f $1GHz -c 6
sudo cpufreq-set -f $1GHz -c 7

cpufreq-info
