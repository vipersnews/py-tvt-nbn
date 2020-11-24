from getpass import getpass
import netmiko
import re
import difflib

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
get_ips("input/IPs.txt")
print('#' * 50)
print('#' * 50, '\n HOSTS', ips, '\n', " Make sure you have checked your individual command files", '\n')

print("IF INCORRECT QUIT NOW CTRL^C ", '\n', '#' * 50)
print('#' * 50)

#Prompt user for account info
username = input("Username: ")
password = getpass()
#This is required for our Diff Loop, pre-tvt store in Before, Post in After
file_name_input = input("For Pre-TVT type Before.txt - For Post-TVT type After.txt : ")

#For each IP in our IPs.txt file, we will look for that IP.txt for the individual commands for the host
for ip in ips:
	#Connect to a device
	file_name_tup = ("output/" + ip, "-" + file_name_input )
	file_name = ''.join(file_name_tup)
	to_doc_w(file_name, "")
	commands_list = []
		# Get the commands from unique ipaddress.txt and append to our list
	with open("input/" + ip + '.txt', 'r') as f:
		for line in f:
			commands_list.append(line)

	try:

		net_connect = make_connection(ip , username, password)
		print("Completing " + ip )
		#Run all our commands and append to our file_name
		for commands in commands_list:
			output = net_connect.send_command_timing(commands)
			results = output + '\n'
        	#Next we will append the output to the individual results file
			to_doc_a(file_name, results)
	except:
		print( ip + " Failed to connect")

print('Completed')
