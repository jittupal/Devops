while read -r username
do
	sudo userdel -r $username
done < /mnt/e/bash-script/user_list.txt
