#!/bin/bash

directory_path=$1
file_extension=$2

file_count=$(find $directory_path -type f -name "*.$file_extension" | wc -l)

echo "The file count is $file_count"

