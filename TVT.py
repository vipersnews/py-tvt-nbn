from getpass import getpass
import netmiko
import re
import difflib
import sys

def make_connection (ip, username, password):
		return netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)

def get_ip (input):
	return(re.findall(r'(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)', input))

def get_ips (file_name):
	for line in open(file_name, 'r').readlines():
		line = get_ip(line)
		for ip in line:
			ips.append(ip)

def to_doc_a(file_name, varable):
	f=open(file_name, 'a')
	f.write(varable)
	f.write('\n')
	f.close()


def to_doc_w(file_name, varable):
	f=open(file_name, 'w')
	f.write(varable)
	f.close()

#This will be a list of the devices we want to SSH to
ips = []

#Pull the IPs.txt is a list of the IPs we want to connect to
#This function pulls those IPs out of the txt file and puts them into a list
get_ips("IPs.txt")
print('#' * 50)
print('#' * 50, '\n HOSTS', ips, '\n', "COMMAND LIST", '\n')

print("IF INCORRECT QUIT NOW CTRL^C ", '\n', '#' * 50)
print('#' * 50)

#Prompt user for account info
username = sys.argv[1]
password = getpass()
#This is required for our Diff Loop, pre-tvt store in Before, Post in After
file_name = (sys.argv[2] + ".txt" )
#Clearing all the old info out of the results.csv file
to_doc_w(file_name, "")
#Commands To Use


#Make a for loop to hit all the devices, for this we will be looking at the IOS it's running
for ip in ips:
	#Connect to a device
	net_connect = make_connection(ip, username, password)
	#Run all our commands and append to our file_name
	commands_list = []
	# Get the commands from commands.txt and append to our list
	with open(ip + '.txt', 'r') as f:
		for line in f:
			commands_list.append(line)

	for commands in commands_list:
		output = net_connect.send_command_expect(commands)
		results = output + '\n'
        #Next we will append the output to the results file
		to_doc_a(file_name, results)

#Loop to determine actions for Pre-TVT or Post-TVT
if file_name == "Before.txt":
	print('Completed')
elif file_name == "After.txt":
	fromfile = "Before.txt"
	tofile = "After.txt"
	fromlines = open(fromfile, 'U').readlines()
	tolines = open(tofile, 'U').readlines()
	diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile)
	f = open("changes.html", "w")
	f.write(diff)
	f.close
	print("Open changes.html to see difference")
else:
	print('Before or After not detected')
