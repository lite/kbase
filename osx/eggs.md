+ mitm

An interactive SSL-capable intercepting HTTP proxy for penetration testers and software developers

	https://github.com/cortesi/mitmproxy
	
	
+ multi-mechanize

A few enhancements to Multi-Mechanize (http://code.google.com/p/multi-mechanize/)

	https://github.com/jasongrout/multi-mechanize
	
+ pygtk

Download script from: https://raw.github.com/jralls/gtk-osx-build/master/gtk-osx-build-setup.sh


    sh gtk-osx-build-setup.sh

.jhbuildrc-custom

    build_policy = "updated-deps"
    os.environ["ARCHFLAGS"] = "-arch x86_64 -arch i386"

    $ ~/.local/bin/jhbuild shell

    $ jhbuild bootstrap --ignore-system
    $ jhbuild build meta-gtk-osx-bootstrap
    $ jhbuild build meta-gtk-osx-core
    $ jhbuild build meta-gtk-osx-python