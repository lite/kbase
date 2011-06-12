TextMate (Pete's notes)
 
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
