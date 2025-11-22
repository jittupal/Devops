packeges=/mnt/e/bash-script/packeges.txt

while read -r packege; do
	echo "package is installing...."
	sudo apt install -y $packege
	echo "package is installed"
done < $packeges
