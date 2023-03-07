- Download [Debian 11](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso).
- Import the .iso into VirtualBox or VMware Fusion, and install Debian 11 (use default settings during the installation process, set username: student, password: lab3).
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
