#!/bin/bash
file=$1
lines=$(cat $file)
for line in $lines
do
	echo -n $line | sha256sum | awk '{print $1}' >> hashes.txt
done