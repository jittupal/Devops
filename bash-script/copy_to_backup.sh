mkdir /e/backup_dir


for file in /e/bash-script/*.txt
do
	name=$(basename "$file")
	cp "$file" "/e/backup_dir/${name%.txt}_$(date +%Y-%m-%d_%H-%M).txt"
done
