command="curl"
if command -v $command &> /dev/null ;then
	echo "curl command is exist"
else
	echo "curl command is not exist"
fi
