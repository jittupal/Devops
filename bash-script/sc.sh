x=10
y=20
c=$(expr $x + $y)
if [ $c -lt 20 ]; then
	echo "10 and 20 is less than 40"
elif [ $c -eq 30 ]; then
	echo "10 and 20 are 30"
else
        echo "10 and 20 is greater then 25"
fi
