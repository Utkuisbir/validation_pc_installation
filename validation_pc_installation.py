import subprocess

cmd = "sudo apt install sshpass ;wget http://ataweb.corp.airties.com/files/ssh_git.sh;chmod a+x ssh_git.sh;./ssh_git.sh;install_certification.sh 1.0.5;sudo apt autoremove;sudo apt install python3-pip -y;sudo apt install python3-httplib2 -y;sudo apt install apache2 -y;sudo apt install lynx -y;sudo apt install subversion -y;sudo apt install git -y;sudo apt install python3-setuptools -y;sudo apt install moreutils -y;sudo apt install iperf3 -y;sudo apt install sshpass -y;sudo apt install python3-numpy -y;sudo apt install ifupdown -y;sudo apt install net-tools -y;sudo apt install dhtest -y;python3 -m pip install fire;python3 -m pip install paramiko;python3 -m pip install packaging;python3 -m pip install coloredlogs;python3 -m pip install netifaces;python3 -m pip install requests;python3 -m pip install xmltodict;python3 -m pip install pyshark;python3 -m pip install Flask;python3 -m pip install pycurl;python3 -m pip install pyserial;python3 -m pip install mysql-connector-python"

def subprocess_cmd(command):
    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    proc_stdout = process.communicate()[0].strip()
    for line in proc_stdout.decode().split('\n'):
        print (line)

subprocess_cmd(cmd)