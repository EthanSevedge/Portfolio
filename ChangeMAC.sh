#!/bin/bash
#
# ChangeMAC.sh
#requires macchanger, setsid, wmctrl, firefox, nmcli, loadingFunction.sh

#TODO: -make sure opening the tab in firefox is not time dependent (see 
# last line of code, right now is jimmy-rigged with a sleep 2)
# -make sure the firefox program isn't running when program starts;
# it can happen that firefox is running but window hasn't opened yet,
# and right now the code just checks to see if a window is open

#trying to debug code to make sure timing is the only reason firefox
#doesn't open when the sleep 2 at end of file isn't executed.
#To that end, trying to run test.sh from desktop file, which
#ought to tee output both to terminal and ChangeMacOutput for
#debugging purposes. However, this changes the $PPID from the
# PPID of the terminal to the PPID of test.sh (I think);
#and since test.sh doesn't have a window, it can't find it in the line
#of code looking for the window with the procID variable.
#So trying to be able to walk up the parent tree up to the terminal.
#There is a difference between the PGID (Process Group ID) and the
#ID of the process that started the group, because if the subprocess
#starts a group of its own, it assumes a new PGID (which its subprocesses
#assume as well), thus making it harder to walk up the parent tree.
#However, unless this program ends up making any subprocesses, you
#can probably use them interchangeably. ps -ejH lists processes in tree
#form.

connectionName="e1"
networkDeviceName="enp9s0"

firefoxOpen="$(wmctrl -l | grep Firefox)"


#checks if a firefox window is open yet
if [[  "" = $firefoxOpen  ]]
then
	procID=$PPID
	
	#waits until terminal window is open, then finds it by its PID
	#and stores whole line of output in winOut
	winOut="$(wmctrl -lp | grep $procID)"
	while [[ "" = $winOut ]]
	do
		winOut="$(wmctrl -lp | grep $procID)"
	done
	
	#stores first token (delimited by spaces; first token is window ID)
	#in the variable winID
	read -ra winID <<< $winOut
		
	#opens firefox in new process & sends error and output to /dev/null
	#this appears to avoid having the sighup signal sent to firefox, shutting it down
	setsid firefox 1>/dev/null 2>/dev/null &
	
	#waits until firefox opens, with pretty loading output
	while [[ "" = $firefoxOpen ]]
	do
		firefoxOpen="$(wmctrl -l | grep Firefox)"
		echo -e -n "\r\\" 
		sleep $time 
		echo -e -n "\r/" 
		sleep $time
		echo -e -n "\r-"
		sleep $time
		echo -e -n "\r \r"
	done
	clear
	#makes terminal window active again after firefox starts
	wmctrl -ia $winID
	
fi

answer=null

until [[ $answer == "1" || $answer == "2" || $answer == "3" ]]; do
	echo Are you randomizing your MAC, or using the MAC for Gmail, or using the MAC for Outlook? 1/2/3
	read answer
	if [[ $answer != null && $answer != "1" && $answer != "2" && $answer != "3" ]]
	then
		clear
		echo Invalid Input
		sleep 1s
		clear
	fi
done

nmcli connection down $connectionName
 
#Random
if [ $answer == "1" ]
then
	sudo macchanger -r $networkDeviceName
#Gmail
elif [ $answer == "2" ]
then
	sudo macchanger --mac=90:82:60:4a:c7:f6 $networkDeviceName
#Outlook
elif [ $answer == "3" ]
then
	sudo macchanger --mac=56:65:03:cc:7f:e0 $networkDeviceName
else
	echo Incorrect input given for question
fi

#nohup firefox &> /dev/null &
nmcli connection up $connectionName

if [ $answer == "1" ]
then
	:
elif [ $answer == "2" ]
then
	nohup firefox gmail.com &> /dev/null &
	disown
	#pause to let firefox open before terminal closes
	sleep 2
elif [ $answer == "3" ]
then
	nohup firefox outlook.office.com &> /dev/null &
	disown
	#pause to let firefox open before terminal closes
	sleep 2
else
	echo Incorrect input given for question
fi

