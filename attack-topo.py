#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='127.0.0.1',
                      protocol='tcp',
                      port=6633)

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)

    info( '*** Add hosts\n')
    att = net.addHost('att', cls=Host, ip='10.0.0.1', defaultRoute=None)
    leg = net.addHost('leg', cls=Host, ip='10.0.0.2', defaultRoute=None)
    vic = net.addHost('vic', cls=Host, ip='10.0.0.3', defaultRoute=None)

    info( '*** Add links\n')
    net.addLink(leg, s1)
    net.addLink(s1, vic)
    net.addLink(s1, att)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])

    info( '*** Post configure switches and hosts\n')
    vic.cmd("/etc/init.d/xinetd restart")
    vic.cmd("/usr/sbin/sshd -D &")
    vic.cmd("python -m SimpleHTTPServer 80 &")
    att.cmd("wireshark -i att-eth0 -k -Y '''ip.src == 10.0.0.0/24 or ip.dst == 10.0.0.0/24''' &")
    CLI(net, script='xterm.sh')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

