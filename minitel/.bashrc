# to add at the end of your .bashrc file in your user directory
# program launching every time you connect to your debian VM, create an user

    read -p "Enter username : " username
	read -s -p "Enter password : " password
	egrep "^$username" /etc/passwd >/dev/null
	if [ $? -eq 0 ]; then
		echo "$username exists!"
		exit 1
	else
		pass=$(perl -e 'print crypt($ARGV[0], "password")' $password)
		sudo useradd -m -p "$pass" "$username"
		[ $? -eq 0 ] && echo "User has been added to system!" || echo "Failed to add a user!"
        sudo python3 /home/lawrence/minitel/minitel/main.py
	fi
    
