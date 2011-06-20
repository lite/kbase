+ To create an image of a CD (or DVD or anything else…) use the following:

```                                             
diskutil unmount /Volumes/Untitled\ UDF\ Volume/
dd if=/dev/disk1s0 of=20110601.iso bs=64k
```

+ Resample image so height and width aren't greater than specified size, e.g. 100x100

```
sips -Z 100x100 image.jpg
```

+ keymap

```
Ctrl-a moves to the start of the line
Ctrl-e moves to the end of the line
Ctrl-b move back on character
Ctrl-f move forward one character
Esc-b move back one word
Esc-f move forward one word
Esc-t arg1 arg2 => arg2 arg1
Ctrl-u delete from the cursor to the beginning of the line
Ctrl-k delete from the cursor to the end of the line
```

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
```

+ dstat & sar

+ siege & tsung

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
