#!/bin/bash
perf stat -e r412E  l1-load-misses cycles instructions ./programa
