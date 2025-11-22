view_tasks(){
	echo
	if [ ! -s todo.txt ]; then
		echo "There is NO Tasks"
	else
                echo "-------***Your All Tasks Are As Below***--------"
                cat -n todo.txt
		echo
		echo "-------********--------********---------********"
	fi
	echo
}

add_task(){
	echo
	echo "Enter The Task To Add"
	read Task
	echo "$Task" >> todo.txt
	echo "Task Added Successfully"
	echo
	view_tasks
}

remove_task(){
	echo
	if [ ! -s todo.txt ]; then
                echo "There is NO Tasks"
        else
	        view_tasks
	        echo -n "Enter Task Number To Remove:  "
	        read taskno
	        sed -i ${taskno}d todo.txt
	        echo "Task Deleted Successfully"
		echo
		view_tasks
	fi
	echo
}

show_menu(){
	echo
	echo "==================="
	echo "TO-DO LIST MENU"
	echo "==================="
	echo "1. View Task"
	echo "2. Add Task"
	echo "3. Remove Task"
	echo "4. Exit"
	echo -n "Choose An Option (1-4):  "
}

while true; do
	echo
	show_menu
	read option
	case $option in
		1) view_tasks;;
		2) add_task;;
		3) remove_task;;
		4) exit 0;;
		*) echo "Invalid Option";;
	esac
done
