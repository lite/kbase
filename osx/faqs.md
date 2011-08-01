mysql
====

Q: No such file or directory - /tmp/mysql.sock
A: 
    mysql -e "status"
    UNIX socket:		/usr/local/var/mysql/mysql.sock
    ln -sf /usr/local/var/mysql/mysql.sock /tmp/mysql.sock

buildr
====
Q: "cross-thread violation on rb_gc" rvm, rjb & buildr
A: 
    export JAVA_HOME="/System/Library/Frameworks/JavaVM.framework/Home"
    gem install rjb -v 1.3.3 --platform ruby
    
capybara
====
Q:  ajax timeout
A:
    Capybara::Selenium::Driver::DEFAULT_OPTIONS[:resynchronize] = false
    page.driver.options[:resynchronize] = false
