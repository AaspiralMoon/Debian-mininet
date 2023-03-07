#!/bin/bash

sudo apt update
sudo apt install git mininet wireshark netwox netcat python telnetd telnet -y

git clone https://github.com/AaspiralMoon/temp
cp temp/attack-topo.py /home/student/
cp temp/start_mininet.sh /home/student/
