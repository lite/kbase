putty for cygwin
----

    puttycyg

sshd on cygwin
----
   
http://kt2t.us/cygrunsrv.htm
   
    ssh-host-config -y  # tty ntsec
    ssh-user-config
    cygrunsrv -S sshd

apt on cygwin
----
    $ mv setup.exe /usr/bin
    $ setup.exe -q -P  wget,tar,qawk,bzip2,subversion,vim
    $ svn --force export http://apt-cyg.googlecode.com/svn/trunk/ /bin/ 
    $ chmod +x /bin/apt-cyg