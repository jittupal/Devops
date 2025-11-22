greet() {
	echo "you called a function in linux"
}

greet

square() {
	v=$1
	echo "The square of $v is: $((v*v))"
}

echo "Enter the number for knowing square"
read num

square $num

echo "Enter number to check even or odd"
read num1

is_even() {
	if [ $(($num1 % 2 )) -eq 0 ]; then
		echo "Number is Even"
	else
		echo "Number is Odd"
	fi
	return $num1
}

check_number=$(is_even)

echo "$check_number"
