# Pyfik

A simple and basic monitoring tool made in Tkinter

![](https://github.com/angel99ab/pyfik/blob/main/images/app.png)

## Requisites
- [Python](https://www.python.org/downloads/ "Python") 3.8.1 or above

## Modules
- [customtkinter](https://github.com/TomSchimansky/CustomTkinter "customtkinter")
- [psutil](https://github.com/giampaolo/psutil "psutil")
- [py-cpuinfo](https://github.com/workhorsy/py-cpuinfo "py-cpuinfo")

> **_NOTE:_**  See [requirements.txt](https://github.com/angel99ab/pyfik/blob/main/requirements.txt "requirements.txt") for specific version.

## Installation
1. Download the repository
	1. Using [git clone](https://www.git-scm.com/docs/git-clone "git clone") command
	`git clone https://github.com/angel99ab/pyfik.git`
	2. Download zip file from Code > Download ZIP
2. Cd to the path of the project
3. Create a [virtual environment](https://docs.python.org/3/tutorial/venv.html "virtual environment") to manage the dependencies
	`python -m venv venv` or `python3 -m venv venv`
4. Activate the virtual environment
	1. On Windows cmd
	`venv\Scripts\activate.bat`
	2. On Windows powershell
	`.\venv\Scripts\Activate.ps1`
	3. On Linux/Mac terminal
	`. venv/Scripts/Activate` or `source venv/Scripts/Activate`
5. Install dependencies from requirements.txt
	`pip install -r .\requirements.txt`