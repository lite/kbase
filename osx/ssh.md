ssh
====

copy ssh id_rsa to remote host

	ssh-keygen
	scp ~/.ssh/id_rsa.pub root@fssle.com:/root/.ssh/authorized_keys

autossh
====

ssh -D in autossh    

	autossh -M 21010 -N root@fssle.com -D 127.0.0.1:1080
	autossh -M 21011 root@fssle.com -t 'screen -Rd'

