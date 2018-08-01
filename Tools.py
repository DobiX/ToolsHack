import os, sys, time
from time import sleep as timeout
def restart_program():
        python = sys.executable
        os.execl(python, python, * sys.argv)
        curdir = os.getcwd()

#banner

os.system("clear")
os.system("figlet Tools Hack")
print "instsll all tools for hacking"
print
print "	[01]> FB_like	[02]> RedHawk"
print "	[03]> Weeman	[04]> Ngrok"
print "	[99]> Donate"
print "	[00]> Exit"
print

A = raw_input("install : ")

def FB_like():
	os.system("apt-get upgrade && apt-get update")
	os.system("apt-get install git")
	os.system("apt-get install python python2")
	os.system("git clone https://github.com/krittakon357/FB_like.git")
	os.system("cp -rf FB_like ~")
	os.system("rm -rf FB_like")
	
def RedHawk():
    os.system("apt-get upgrade -y && apt-get update -y")
    os.system("apt-get install git -y")
    os.system("apt-get install php -y")
    os.system("git clone https://github.com/jota01234/Vbug.g")
    os.system("cp -rf RED_HAWK ~ ")
    os.system("rm -rf RED_HAWK")
    
def Weeman():
    os.system("apt update && apt upgarde")
    os.system("apt install python2")
    os.system("apt install git")
    os.system("git clone https://github.com/evait-security/weeman")
    os.system("cp -rf weeman ~ ")
    os.system("rm -rf weeman")
    
def Ngrok():
    os.system("apt install python2")
    os.system("apt install git")
    os.system("git clone https://github.com/DobiX/ngrok")
    os.system("cp -rf ngrok ~ ")
    os.system("rm -rf ngrok")


#options

if A == "1" or A == "01":
	FB_like()
	
elif A == "2" or A == "02":
    RedHawk()
    
elif A == "3" or A == "03":
    Weeman()
    
elif A == "4" or A == "04":
    Ngrok()

elif A == "99":
	os.system("clear")
	print"Creator : GG HACKER TEME"
	print"Donate : 0809577679"
	timeout(8)
        restart_program()


elif A == "00":
	sys.exit()

else:
	print "input errer"
	timeout(4)
	restart_program()
    