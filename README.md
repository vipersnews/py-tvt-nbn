# Py-tvt
Python Config Command Sender with unique commands for each host.

## Installation

Requires the following libraries
getpass
netmiko
re
difflib

Use the package manager pip to install
```bash
pip install getpass
pip install netmiko
pip install difflib
pip install re
```

## Usages

```python
USER CONFIGURATIONS:

You can delete the contents of the output folder before beginning, but you must keep the folder itself.

Under folder input:
Edit the IPs.txt file to have a host on each line with just their IP
Create a commands for each host, it must be in the format of the ipaddress.txt.

EG: IP.txt contains hosts 192.168.1.3, 192.168.1.4, 192.168.1.5. 3 commands files need to be created called 192.168.1.3.txt, 192.168.1.4.txt and 192.168.1.5.txt

RUNNING SCRIPT:

To execute a Before check to establish a working baseline: python3 TVT.py
At the prompts:-
Enter Username
Enter Password
Enter Before.txt


To execute an After check post your router changes: python3 TVT.py
At the prompts:-
Enter Username
Enter Password
Enter After.txt

You will be shown the list of IP's you are connecting to, perform due dillegence by double checking each individual commands file to ensure you know the commands the script will run

The script will run through the host and its commands.

If there is an error connecting to an individual host, it will print and error and continue on.

Under Folder output:
Upon completion of the Before script option, it will write Completed.

Upon completion of the After script option, it will run a diff and generate you a HTML file to compare the Before & After of each host

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
Copyright (c) [2020] [Doran McGregor]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
