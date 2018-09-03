#!/usr/bin/env bash

if [ $1 = "ui" ]; then
	for i in views/ui/*.ui; do
		base=$(basename ${i%.*})
		
		output=views/compiled/${base}.py
		pyside2-uic -x -o $output $i

	done

fi
