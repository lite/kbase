+ rvm

run command in shell

	$ bash < <(curl -s https://rvm.beginrescueend.com/install/rvm)

+ vagrant

run command in shell

	gem install vagrant
	vagrant box add base http://files.vagrantup.com/lucid32.box
	vagrant init
	vagrant up
	vagrant ssh
	
	boxes: http://www.vagrantbox.es/

+ brew

run command in shell

	ruby -e "$(curl -fsSL https://raw.github.com/gist/323731)"

+ pow

run command in shell

	curl get.pow.cx | sh
	cd ~/.pow
	ln -s /path/to/myapp
	
  $ curl get.pow.cx/uninstall.sh | sh #if you have pow installed
  $ echo 'export POW_DST_PORT=88' >> ~/.powconfig
  $ curl get.pow.cx | sh
  $ sudo curl https://raw.github.com/gist/1058580/zzz_pow.conf -o /etc/apache2/other/zzz_pow.conf
  $ sudo apachectl restart

	
+ buildr

+ capybara

https://github.com/jnicklas/capybara

+ cucumber

http://cukes.info/

+ webrat

Webrat - Ruby Acceptance Testing for Web applications 

	https://github.com/brynary/webrat

+ webmock

Library for stubbing and setting expectations on HTTP requests in Ruby.

	https://github.com/bblimke/webmock

+ mechanize

you should be able to fetch pages, click links, fill out and submit forms, scrape data, and many other hopefully useful things

	http://mechanize.rubyforge.org/GUIDE_rdoc.html


