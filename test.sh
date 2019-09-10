#!/bin/bash

#MADE BY MANUEL DUARTE MASCARENHAS - IST LEIC-T 2019

cd ./papers
for i in *;
	do
		echo $i
		python3 ../test.py "$i" >> ../res.txt
done
