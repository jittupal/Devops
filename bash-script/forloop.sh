for i in {1..6}
do
	if [ $(($i % 2)) -eq 0 ]; then
		echo "the number is divisible by 2: $i"
	else
		echo "the number is not divisible by 2: $i"
	fi
done

