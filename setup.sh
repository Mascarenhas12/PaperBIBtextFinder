#!/bin/bash
#MADE BY MANUEL DUARTE MASCARENHAS - IST LEIC-T 2019

pip3 install bs4
pip3 install requests
pip3 install Selenium
sudo apt install chromium-chromedriver

cd ./example
for i in *;
	do
		echo $i
		python3 ../test.py "$i" >> ../setup.txt
done
