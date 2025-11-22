echo "Enter The File Name:  "
read File

File_Line=$(wc -l $File)
echo "The Number Of Lines In The File:  $File_Line"

File_Word=$(wc -w $File)
echo "The Number Of Words In The File:  $File_Word"

File_Char=$(wc -m $File)
echo "The Number Of Character In The File:  $File_Char"


max=0
while read -r text; do
	length=$(expr length "$text")
	if [ $length -gt $max ]; then
		max=$length
		long_word=$text
	fi
done < $File

echo "The longest word is: $long_word"
