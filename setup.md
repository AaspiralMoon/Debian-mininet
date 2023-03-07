- Download [Debian 11](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso).
- Import the .iso into [UTM](https://github.com/utmapp/UTM/releases/latest/download/UTM.dmg), VirtualBox, or VMware Fusion, and install Debian 11 (use default settings during the installation process, set root password: lab3, username: student, password: lab3).
- After entering the OS, enable [auto login](https://help.ubuntu.com/stable/ubuntu-help/user-autologin.html.en).
- Add user “student” to sudo list, and enable no password for sudo commands:
```python
su -i  # input the root password: lab3, switch to root user
sudo visudo
student ALL=(ALL) NOPASSWD: ALL  # add this line below root ALL=(ALL:ALL) ALL
```
- install packages
```python
sudo apt update
sudo apt install git mininet wireshark netwox netcat python python3 telnetd telnet libreoffice xterm -y
```
- install [ifconfig](https://www.how2shout.com/linux/install-ifconfigon-debian-11-or-10-if-command-not-found/)
- make sure the default python is python3.9:
```python
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1
```
- download Pox in home directory
```python
cd ~
git clone http://github.com/noxrepo/pox
cd pox
git checkout dart
```

- enable rc.local service 
```python
sudo nano /etc/rc.local # put the following lines in this file
```

```python
#!/bin/bash
/home/student/pox/pox.py log.level --DEBUG misc.of_tutorial &
exit 0
```


```python
chmod +x /etc/rc.local
sudo systemctl daemon-reload
sudo systemctl start rc-local  # start the rc-local service
sudo systemctl status rc-local # check if the service is active and running
```
- create xterm.sh in home directory
```python
cd ~
touch xterm.sh
nano xterm.sh
xterm leg vic att  # put this line in it
```
- create a startup script start_mininet.sh in home directory
```python
cd ~
touch start_mininet.sh
nano start_mininet.sh   # put the following lines in it
```
```python
#!/bin/bash
cd ~
sudo mn -c    # clean up current mininet settings
sudo python /home/student/attack-topo.py     # put attack-topo.py in home directory
```
- run the startup script and test everything
```python
cd ~
chmod +x ./start_mininet.sh
./start_mininet.sh
```
- test exporting and importing the virtual machine
