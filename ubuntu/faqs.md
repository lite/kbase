/etc/rc.local 
====

backgrounded script in /etc/rc.local not working 

    exec 2> /tmp/rc.local.debug
    set -x

Wifi
====

wifi can not start

    rfkill unblock all

gem 
====

no such file to load zlib

    cd ext/zlib
    ruby ./extconf.rb
    make
    sudo make install