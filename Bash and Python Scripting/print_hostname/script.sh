#!/bin/bash

#check if input file name is provided or not

if [ -z $1 ]; then
    echo "please provide the input file name"
    exit 1
fi



hostname_value=$(hostname)

echo $hostname_value >> $1

echo "$hostname_value is included in the $1 file"
