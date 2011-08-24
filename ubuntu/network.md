# /etc/network/

dhcp to static ip address

    #sudo vi /etc/network/interface
    iface eth0 inet static
        address 172.16.98.100
        netmask 255.255.255.0
        gateway 172.16.98.1
    
    
    #sudo vi /etc/resolv.conf
    nameserver 172.16.98.2
        
    #sudo /etc/init.d/networking restart
    #sudo ifconfig eth0 down
    #^down^up
    