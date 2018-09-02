#!/usr/bin/env bash

if [ $1 = "ui" ]; then
	for i in views/ui/*.ui; do
		base=$(basename ${i%.*})
		
		output=views/compiled/${base}.py
		pyuic5 -x -o $output $i

	done

fi
