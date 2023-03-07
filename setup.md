- Download [Debian 11](https://cdimage.debian.org/debian-cd/current/amd64/iso-cd/debian-11.6.0-amd64-netinst.iso).
- Import the .iso into VirtualBox or VMware Fusion, and install Debian 11 (use default settings during the installation process, set username: student, password: lab3).
- After entering the OS, enable [auto-login](https://help.ubuntu.com/stable/ubuntu-help/user-autologin.html.en).
- Add user “student” to sudo list, and enable no password for sudo commands:
```python
su -i  # input the root password: lab3, switch to root user
sudo visudo
student ALL=(ALL) NOPASSWD: ALL  # add this line below root ALL=(ALL:ALL) ALL
```


sudo apt update
sudo apt install git mininet wireshark netwox netcat python telnetd telnet -y

git clone https://github.com/AaspiralMoon/temp
cp temp/attack-topo.py /home/student/
cp temp/start_mininet.sh /home/student/
