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

## Usage

```python
Edit the IPs.txt file to have a host on each line with just their IP
Create a commands for each host, it must be in the format of the ip_address.txt.

EG: IP.txt contains 192.168.1.3, commands file needs to be called 192.168.1.3.txt

We are using input arguments to save time, Arg 1 is USERNAME arg 2 is Before or After

To execute a Before: python3 Changes.py USERNAME Before
To execute an After: python3 Changes.py USERNAME After

You will be shown the list of commands this script is going to execute, if there is an issue, exit the script.

You will then be prompted for your password

The script will run through the host and its commands.

Upon completion it will write the config to start-up and print the status.

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
