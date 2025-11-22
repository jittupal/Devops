./sc.sh

stats1=$?

./com_inst.sh

stats2=$?

if [ $stats1 -eq 0 ] && [ $stats2 -eq 0 ]; then
	echo "both script run successfully"
elif [ $stats1 -eq 0 ] && [ $stats2 -ne 0 ]; then
	echo "only sc.sh script run successfully"
elif [ $stats1 -ne 0 ] &&[ $stats2 -eq 0 ]; then
	echo "only com_inst script run successfully"
else
	echo "both script did not run"
fi
