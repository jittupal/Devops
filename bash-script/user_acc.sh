USER_DATA=credentials.txt
while read -r username;
do
	#genrate a random password
	password=$(openssl rand -base64 8)
	
	#create new user for each username
	sudo useradd $username
	echo "$username: $password" >> $USER_DATA
done < /mnt/e/bash-script/user_list.txt

