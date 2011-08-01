RVM
====
rvm wrapper rbx@mate textmate
TM_RUBY `which textmate_ruby`

Plugins
====

MissingDrawer

	$ curl -L https://github.com/downloads/jezdez/textmate-missingdrawer/MissingDrawer-0.4.0.tmplugin.zip | tar -xf - && open MissingDrawer.tmplugin

NiceFind2

	http://cloud.github.com/downloads/briancollins/nice_find/NiceFind2.1.tmplugin.zip

HTML CSS

	http://minimaldesign.net/downloads/tools/textmate-css-bundle
	http://minimaldesign.net/downloads/tools/textmate-html-bundle
	
HAML SASS
	
	$ cd ~/Library/Application\ Support/TextMate/Bundles/
	$ git clone git://github.com/handcrafted/handcrafted-haml-textmate-bundle.git HAML-Handcrafted.tmbundle
	$ git clone git://github.com/seaofclouds/sass-textmate-bundle.git "Ruby Saas.tmbundle"
	$ osascript -e 'tell app "TextMate" to reload bundles'

The Hidden Magic in TextMate
====

http://thinkvitamin.com/code/the-hidden-magic-in-textmate/

⌘T – Go to File – This shortcut is truly second to none. Instead of trawling through your project drawer or going through the folders in your finder, use this to quickly jump straight to any file you wish to be in.
⇧⌘T – Go to Symbol – This works in the same way as Go to File but for within a specific file. Trying to find a set method or a global variable? Look no further good sir, this is what you need. Especially useful for when you’re working with a massive user model!
⌘L – Go to Line – If you’re debugging a stack trace, you’ll want to remember this one. Jump to an exact point within a file to squash that nasty bug!
⇧⌘L – Select Line – Select the entire line of code you’re working on. Chances are you may want to follow it up with…
⌃⌘ + ARROW – Move Code – Move the selected code around the file, helps when doing some refactoring of that nasty functional code.
⇧⌃⌥V – Send selected to Pastie – This one is pretty unknown but handy. Send the selected code over to Pastie with a private URL for sharing the code – great when you need some feedback from a fellow developer.
⌃S – Simple Search – Most folks know about ⌘F as it’s the same in most applications. However in TextMate it loads up an additional window for find and replace which isn’t always what you want. This shortcut allows you to do a quick search in the current file iteratively.
⌘] and ⌘[ – Block indentation – Indenting manually can be a pain – use these functions to indent blocks of code quickly and easily.
⇧⌃T – To-do list – This feature scans the project for code marked as ‘FIXME’, ‘TODO’ and ‘CHANGED’. It provides an informative list of them along with comments.


TextMate (Pete's notes)
====
 
http://nets.ucar.edu/nets/intro/staff/siemsen/tools/editors/textmate/

FileType:
ctrl+alt+shift + r

Tabs and spaces

My standard is to us 4-space indenting and no tabs. To get this in TextMate, at the bottom of the window, in the gutter, set the Tabs field to "Soft Tabs" and "4".
Key binding

Use Control-Command-T and Control-Alt-Command-K to get lists of the current key bindings.

Edit in TextMate

I turned on "Edit in TextMate" by clicking the gear menu in the status bar (inside TextMate), navigating to the TextMate submenu and selecting Install "Edit in TextMate". Now I can use TextMate from Safari or Mail. Very cool.

Expanding HTML tags

When in HTML mode, I typed "html" followed by ^< to expand it into <html></html> but intead I got "env: ruby: No such file or directory". After wasting time, I fixed it by making a link to /usr/local/bin/ruby from /usr/bin.

Filling/wrapping tags

TextMate doesn't have Emacs's smart auto-fill mode or the fill-paragraph-or-region function. Instead, it has a limited "reformat paragraph" command which just removes whitespace, and a "column selection" concept which forces text to stay in a box. So you can sorta fix a paragraph by:

Making it one long string with Text->Unwrap Paragraph
Indent it with Text->Indent Line
Select the first line up to where you want the line break to be
Hit Alt/Option once, then Control-Q.
This is inconvenient compared to Emacs, but it sorta works.

Indenting HTML

To indent an HTML file, you select the whole buffer with Command-A, then do Text->Indent Selection. For this to work, you have to have balanced paragraph tags, sigh.

Syntax highlighting (Themes)

I did TextMate->Preferences... and Font & Colors, then copied "Mac Classic" to create "Pete's".

I wrote a Textmate grammar for Juniper config files. While doing it, I learned that Control-shift-P will show you what parser element Textmate is under the cursor.

Bundles

CiscoIOS, CiscoCATOS and JUNOS bundles

I wrote these to get syntax highlighting and IP address lookups when I edit router config files. When I edit them, I try to remember to save them in the directory next to this web page, in /usr/web/nets/intro/staff/siemsen/tools/editors/textmate/. To save them, I have to drag the bundle name to my Desktop, Then run my ~/bin/synchronize-petes-accounts.sh to copy them to galway, where I have to load them by finding them in the Finder and double-clicking them.
ANTLR bundle

You probably want to develop ANTLR grammars with ANTLRWorks, but load the ANTLR bundle to get syntax highlighting anyway:

			cd ~/Library/Application\ Support/TextMate/Bundles
			svn co http://macromates.com/svn/Bundles/trunk/Bundles/ANTLR.tmbundle
		
You'll also be able to compile ANTLR grammars from within TextMate using Command-B.
