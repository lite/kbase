Repeat
====

The "." command repeats the last change made in normal mode. For example, if you press dw to delete a word, you can then press . to delete another word (. is dot, aka period or full stop).

The "@:" command repeats the last command-line change (a command invoked with ":", for example :s/old/new/).

You can move the cursor before using either of the repeat commands.

Suppose you press dd to delete a line. Next, you might move the cursor, then press 5. (5 then dot). That will delete 5 lines.

In normal mode, press J to join the next line onto the current line. Press . to join more lines.

Or, you might use insert mode to type "hello ". Press Esc for normal mode, then move the cursor, and press . to insert "hello " again.

Key binding on Vim
====

http://vim.wikia.com/wiki/Mapping_keys_in_Vim_-_Tutorial_(Part_1)

:nmap - Display normal mode maps
:imap - Display insert mode maps
:vmap - Display visual and select mode maps
:smap - Display select mode maps
:xmap - Display visual mode maps
:cmap - Display command-line mode maps
:omap - Display operator pending mode maps

n  Normal mode map. Defined using ':nmap' or ':nnoremap'.
i  Insert mode map. Defined using ':imap' or ':inoremap'.
v  Visual and select mode map. Defined using ':vmap' or ':vnoremap'.
x  Visual mode map. Defined using ':xmap' or ':xnoremap'.
s  Select mode map. Defined using ':smap' or ':snoremap'.
c  Command-line mode map. Defined using ':cmap' or ':cnoremap'.
o  Operator pending mode map. Defined using ':omap' or ':onoremap'.

<Space>  Normal, Visual and operator pending mode map. Defined using
         ':map' or ':noremap'.
!  Insert and command-line mode map. Defined using 'map!' or

:redir! > vim_maps.txt
:map
:map!
:redir END

Sudo in Vim
===

Save a file you edited in vim without the needed permissions
http://vim.wikia.com/wiki/Su-write

+ :w !sudo tee % 

Cursor movement
====

+ h - move left
+ j - move down
+ k - move up
+ l - move right
+ w - jump by start of words (punctuation considered words)
+ W - jump by words (spaces separate words)
+ e - jump to end of words (punctuation considered words)
+ E - jump to end of words (no punctuation)
+ b - jump backward by words (punctuation considered words)
+ B - jump backward by words (no punctuation)
+ 0 - (zero) start of line
+ ^ - first non-blank character of line
+ $ - end of line
+ G - Go To command (prefix with number - 5G goes to line 5)

Note: Prefix a cursor movement command with a number to repeat it. For example, 4j moves down 4 lines.

Insert Mode - Inserting/Appending text
====

+ i - start insert mode at cursor
+ I - insert at the beginning of the line
+ a - append after the cursor
+ A - append at the end of the line
+ o - open (append) blank line below current line (no need to press return)
+ O - open blank line above current line
+ ea - append at end of word
+ Esc - exit insert mode

Editing
====
+ r - replace a single character (does not use insert mode)
+ J - join line below to the current one
+ cc - change (replace) an entire line
+ cw - change (replace) to the end of word
+ c$ - change (replace) to the end of line
+ s - delete character at cursor and subsitute text
+ S - delete line at cursor and substitute text (same as cc)
+ xp - transpose two letters (delete and paste, technically)
+ u - undo
+ . - repeat last command

Marking text (visual mode)
====

+ v - start visual mode, mark lines, then do command (such as y-yank)
+ V - start Linewise visual mode
+ o - move to other end of marked area
+ Ctrl+v - start visual block mode
+ O - move to Other corner of block
+ aw - mark a word
+ ab - a () block (with braces)
+ aB - a {} block (with brackets)
+ ib - inner () block
+ iB - inner {} block
+ Esc - exit visual mode

Visual commands
====

+ > - shift right
+ < - shift left
+ y - yank (copy) marked text
+ d - delete marked text
+ ~ - switch case

Cut and Paste
====

+ yy - yank (copy) a line
+ 2yy - yank 2 lines
+ yw - yank word
+ y$ - yank to end of line
+ p - put (paste) the clipboard after cursor
+ P - put (paste) before cursor
+ dd - delete (cut) a line
+ dw - delete (cut) the current word
+ x - delete (cut) current character

Exiting
====

+ :w - write (save) the file, but don't exit
+ :wq - write (save) and quit
+ :q - quit (fails if anything has changed)
+ :q! - quit and throw away changes

Search/Replace
====

+ /pattern - search for pattern
+ ?pattern - search backward for pattern
+ n - repeat search in same direction
+ N - repeat search in opposite direction
+ :%s/old/new/g - replace all old with new throughout file
+ :%s/old/new/gc - replace all old with new throughout file with confirmations

Working with multiple files
====

+ :e filename - Edit a file in a new buffer
+ :bnext (or :bn) - go to next buffer
+ :bprev (of :bp) - go to previous buffer
+ :bd - delete a buffer (close a file)
+ :sp filename - Open a file in a new buffer and split window
+ ctrl+ws - Split windows
+ ctrl+ww - switch between windows
+ ctrl+wq - Quit a window
+ ctrl+wv - Split windows vertically

Fuzzy Finder
====

+ map <leader>F :FufFile<CR>
+ map <leader>f :FufTaggedFile<CR>
+ map <leader>g :FufTag<CR>
+ map <leader>b :FufBuffer<CR>  