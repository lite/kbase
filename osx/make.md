otool
----
```
otool -L libusbmuxd.dylib
```

pkg-config
----
```
pkg-config --modversion libusbmuxd
```

GDB
----
http://www.delorie.com/gnu/docs/gdb/gdb_58.html

```
$i sharedlibrary
$b iproxy.c:197
$i breakpoints
$d breakpoints
$add-symbol-file ../src/libusbmuxd.o
$directory ../src 
$b libusbmuxd.c:793
$r 2222 32498

$p/d port
$p payload_size
$set print elements 300
$x/s payload
```

Makefile
----

[A Simple Makefile Tutorial](http://www.cs.colby.edu/maxwell/courses/tutorials/maketutor/)

```
IDIR =../include
CC=gcc
CFLAGS=-I$(IDIR)

ODIR=obj
LDIR =../lib

LIBS=-lm

_DEPS = hellomake.h
DEPS = $(patsubst %,$(IDIR)/%,$(_DEPS))

_OBJ = hellomake.o hellofunc.o 
OBJ = $(patsubst %,$(ODIR)/%,$(_OBJ))


$(ODIR)/%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

hellomake: $(OBJ)
	gcc -o $@ $^ $(CFLAGS) $(LIBS)

.PHONY: clean

clean:
	rm -f $(ODIR)/*.o *~ core $(INCDIR)/*~ 
```