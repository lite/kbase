
+ args

args abbreviation

  echo "hello" "word"
  !! !-1 !4000 # echo "hello" "word"
  !vim # last command with vim
  echo !^
  echo !$
  cp ~/temp{,.bak} #cp ~/temp ~/temp.bak

+ scutil

change hostname

    sudo scutil --set HostName larryx.local

+ sshuttle 

Install sshuttle

    brew install sshuttle
    sshuttle -r root@fssle.com 0.0.0.0/0 -vv

+ coreutils

Install sed and awk.

  	brew install coreutils gnu-sed gawk findutils --default-names
    sed -e '/^$/d' $filename
    echo "123:abc:ce" | sed 's/123/ddd;/s/abc/dde' 
    sed -n '2,6p' /etc/passwd 
    gawk -F: '{ print $1 }' /etc/passwd
    echo "123:abc:ce" | awk 'BEGIN{FS=":"}{OFS="+"} {print $1,$2}'
    echo "123:abc:ce" | awk -F: 'length()>5 {print $1,$2}'
    git status | grep -n "Untacked" | awk -F: '{print $1}'
    ps aux| grep firefox| awk '{print $2}' | xargs kill -9    
 
+ tutti

Interactively run Javascript on multiple browsers

	https://github.com/airportyh/Tutti/

  	brew install nod npm
  	curl http://npmjs.org/install.sh | sh
  	npm install tutti
  	tutti http://tuttijs.com:46071

+ virtualbox

use VBoxHeadless as the front-end to the internal virtualization engine

  	VBoxManage startvm $vm --type headless
  	VBoxHeadless --startvm $vm

+ sysctl

reducing in case of available port bottleneck.

  	sudo sysctl -w net.inet.tcp.msl=1000

+ utils

install tools for sys admin

  	brew install axel iftop wget git lsof bmon unrar htop p7zip w3m watch ragel iperf monit

+ lsof 

replacement netstat cmd to find ports used by apps on OS X

	sudo lsof -i -P

+ diskutil 

To create an image of a CD (or DVD or anything else…) use the following:

	diskutil unmount /Volumes/Untitled\ UDF\ Volume/
	diskutil mountDisk disk1
	dd if=/dev/disk1s0 of=20110601.iso bs=64k
	
+ sips 

Resample image so height and width aren't greater than specified size, e.g. 100x100

	sips -Z 100x100 image.jpg

+ keymap

> + Ctrl-a moves to the start of the line
> + Ctrl-e moves to the end of the line
> + Ctrl-b move back on character
> + Ctrl-f move forward one character
> + Esc-b move back one word
> + Esc-f move forward one word
> + Esc-t arg1 arg2 => arg2 arg1
> + Ctrl-u delete from the cursor to the beginning of the line
> + Ctrl-k delete from the cursor to the end of the line

+ hdiutil 

```
hdiutil mount file.dmg"
hdiutil detach /Volumes/<mountpoint>"
```

+ top

```
top -o vsize
top -o cpu
```

+ mdfind to use spotlight from the command line

```
mdfind -name .ipsw
mdfind -name models.py |xargs mate
```

+ uses DTrace to show you all of the files that are being accessed on your system

```
sudo opensnoop -n WineBottler
```

+ base64 decode 

```
echo "M2dtSRnQAwAF0AMA+McDAEZ0YWJFUFlUIAAAAAQAAABGdGFiAAAAAAAAAAAA" | openssl enc -a -d | hexdump -n 32 -C
```

+ enter iDevice's recovery mode

```
idevice_id -l | awk -F= '{print "ideviceenterrecovery " $1}' |bash
```

+ Install autoconf and tsocks

```
sudo brew install https://github.com/adamv/homebrew-alt/raw/master/duplicates/autoconf.rb
sudo brew install https://github.com/adamv/homebrew-alt/raw/master/other/tsocks.rb
```

+ Enable "path view" in Finder

```
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES 
```

+ Find file and text

```
find .. -name "example*"
grep -r -i "message" *
grep -i -e "\bprint" *.py
```

+ Install ruby-debug

```
rvm gem install ruby-debug19 -- --with-ruby-include="$rvm_src_path/$(rvm tools identifier)/"
```

+ Install haml and sass bundle

```
cd ~/Library/Application\ Support/TextMate/Bundles
svn co http://svn.textmate.org/trunk/Bundles/Ruby%20Haml.tmbundle
svn co http://svn.textmate.org/trunk/Review/Bundles/Ruby%20Sass.tmbundle
```

+ Utility like lsusb 

```
open -a "USB prober"
```

+ View the I/O Kit Registry

```
open -a IORegistryExplorer
```

+ xargs
[cool-but-obscure-unix-tools](http://kkovacs.eu/cool-but-obscure-unix-tools)

```
idevice_id -l| xargs -I% echo "This is :[%]"
```

+ iftop & iptraf

+ htop & iotop

+ ack

```
ack layout
ack -ai '\bzone[-_ ]id' .
```

+ dstat & sar

+ siege & tsung

run command in shell 
	
	siege -c50 http://yourserver.com

+ socat

```
socat TCP-LISTEN:5555,reuseaddr,fork EXEC:"ls -l" &
```

+ mtr

+ slurm

```
slurm -i eth0
```

+ screen

```
screen -ls 
screen -r [session]
Ctrl-a-d (detaches)
Command-k
```

+ Create a new directory and enter it:

```
md() { mkdir -p "$@" && cd "$@"; }
```

+ transfer a working directory from one Terminal window to another

```
alias cwd='pwd | pbcopy'
alias gowd='cd "`pbpaste`"'
```

+ Use "!$" to repeat the last parameter in the last command you entered

```
touch /tmp/README 
mate !$
```

+ play songs from the commandline

```
afplay ~/path/to/file.mp3
```
