#!/bin/bash

cd ./papers
for i in *;
	do
		echo $i
		python3 ../test.py "$i" >> ../res.txt
done
