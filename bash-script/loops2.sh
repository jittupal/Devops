i=1
while [ -f /e/bash-script/loops1.sh ]
do
	echo "File exist till $(date +%H-%M-%S)"
	sleep 2

	if [ $i -eq 3 ]; then
		dele=$(mv loops1.sh loops.sh)
	fi
	i=$((i+1))
done

echo "file is not exist after $(date +%H-%M-%S)"
