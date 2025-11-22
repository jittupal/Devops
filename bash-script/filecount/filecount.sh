dir_to_check=$1
i=1
while [ "$(ls $dir_to_check)" ] #it will check until the file count is zero
do
	file_count=$(ls -l $dir_to_check | wc -l)
	echo "file count in current directory is: $file_count"
	sleep 2
	del_file=$(rm file"$i".txt)
	i=$((i+1))
	
	if [ $file_count -eq 2 ]; then
		echo "exit from loop"
		break
	fi
done

echo "Now the directory is empty"
