
"""
def _encodeBase64(s, maxlinelength=76):
    # copied from base64.encodestring(), with added maxlinelength argument
    maxbinsize = (maxlinelength//4)*3
    pieces = []
    for i in range(0, len(s), maxbinsize):
        chunk = s[i : i + maxbinsize]
        pieces.append(binascii.b2a_base64(chunk))
    return "".join(pieces)

class Data:
    def __init__(self, data):
        self.data = data

    def fromBase64(cls, data):
        # base64.decodestring just calls binascii.a2b_base64;
        # it seems overkill to use both base64 and binascii.
        return cls(binascii.a2b_base64(data))
    fromBase64 = classmethod(fromBase64)

    def asBase64(self, maxlinelength=76):
        return _encodeBase64(self.data, maxlinelength)

    def __cmp__(self, other):
        if isinstance(other, self.__class__):
            return cmp(self.data, other.data)
        elif isinstance(other, str):
            return cmp(self.data, other)
        else:
            return cmp(id(self), id(other))

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, repr(self.data))


The seconds between with 2000-12-31 xx:xx:xx

Float64         64 bit IEEE float:  1 sign bit, 11 exponent bits, 52 fraction bits  
0000-01-01  C2 2D 67 39 0A 9E 00 00 -63142921551
1904-01-01  C1 E6 CE 7E BB A0 00 00 -3061052893
1966-06-10  C1 D0 40 5F F9 80 00 00 -1090617318 
1970-01-01  C1 CD 27 1B BE 00 00 00 -978204540
1973-06-18  C1 C9 E5 F4 33 00 00 00 -869001318
1980-01-01  C1 C3 BF C8 D9 00 00 00 -662671794
1999-01-01  C1 8E 11 48 B0 00 00 00 -63056150
2000-01-01  C1 7E 0F 56 90 00 00 00 -31520105
2001-01-01  40 F8 FC E0 00 00 00 00 102350 =0x18FCE //0 +, 40F-3FF=0x10, 8FCE000000000=1.8FCE000000000<<0x10
2001-01-01  40 F8 FF 40 00 00 00 00 102388 
2001-01-02  41 07 10 C8 00 00 00 00 188953 
2001-02-01  41 45 37 5B 00 00 00 00 2780854
2001-02-02  41 45 E0 37 00 00 00 00 2867310
2001-12-31  41 7E 16 68 10 00 00 00 31549057
2007-09-13  41 A9 34 BA 16 00 00 00 211442955
2007-09-24  41 A9 50 2D 00 00 00 00 212342400
3000-12-31  42 1D 63 C1 DB 70 00 00 31556925148

   Example 2
What is the number which the double 1100000001100110111101000000000000000000000000000000000000000000 represents?
The first bit is 1, so the number is negative. The next 11 bits are 100000001102. Subtracting 011111111112 from this yields 1112, which equals 7. Thus, the result is multiplied by 27 = 128.
The mantissa is 1. followed by all bits after the 12th bit, that is:
              1.0110111101000000000000000000000000000000000000000000
This number is
               1 + 1/4 + 1/8 + 1/32 + 1/64 + 1/128 + 1/256 + 1/1024
which equals 1.4345703125. Thus, the number is -1.4345703125 * 128 = -183.625 (recalling that the number is negative).

Example 3
What is the decimal number which is represented by the the double 0011111111101000100000000000000000000000000000000000000000000000 ?
The first bit is 0, so the number is positive. The next 11 bits are 01111111110, which is one less than 01111111111. Thus, the result is multiplied by 2-1 (or divided by 2).
The mantissa is 
              1.1000100000000000000000000000000000000000000000000000
which is the number
               1 + 1/2 + 1/32
which equals 1.53125 . Thus, the number is 1.53125 / 2 = 0.765625

"""

"""
Offset(h) 00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F

00000000  62 70 6C 69 73 74 30 30 A2 01 02 5F 10 17 44 4C  bplist00..._..DL
00000010  4D 65 73 73 61 67 65 50 72 6F 63 65 73 73 4D 65  MessageProcessMe
00000020  73 73 61 67 65 D1 03 04 5F 10 14 42 61 63 6B 75  ssage..._..Backu
00000030  70 4D 65 73 73 61 67 65 54 79 70 65 4B 65 79 5F  pMessageTypeKey_
00000040  10 20 6B 42 61 63 6B 75 70 4D 65 73 73 61 67 65  . kBackupMessage
00000050  42 61 63 6B 75 70 46 69 6C 65 52 65 63 65 69 76  BackupFileReceiv
00000060  65 64 08 0B 25 28 3F 00 00 00 00 00 00 01 01 00  ed..%(?.........
00000070  00 00 00 00 00 00 05 00 00 00 00 00 00 00 00 00  ................
00000080  00 00 00 00 00 00 62                             ......b

62 70 6C 69 73 74 30 30                             HEADER magic number ("bplist") file format version -- bplist00
                        A2 01 02                    OBJECT TABLE array objref* objref*          - 08
                                 5F 10 17 44 4C     ascii  DLMessageProcessMessage              - 0B
4D 65 73 73 61 67 65 50 72 6F 63 65 73 73 4D 65
73 73 61 67 65 
               D1 03 04                             dict keyref* objref*                        - 25
                        5F 10 14 42 61 63 6B 75     ascii  BackupMessageTypeKey                 - 28
70 4D 65 73 73 61 67 65 54 79 70 65 4B 65 79 
                                             5F     ascii  kBackupMessageBackupFileReceived     - 3f 
10 20 6B 42 61 63 6B 75 70 4D 65 73 73 61 67 65
42 61 63 6B 75 70 46 69 6C 65 52 65 63 65 69 76
65 64 
      08 0B 25 28 3F                                OFFSET TABLE 08 0B 25 28 3F                 - 62
                     00 00 00 00 00 00              TRAILER unknown1[6]
                                       01           byte size of offset ints in offset table
                                          01        byte size of object refs in arrays and dicts    
                                             00     
00 00 00                                            unknown2[4]
         00 00 00 05                                number of offsets in offset table (also is number of objects)
                     00 00 00 00 00 00 00 00 00
00 00 00                                            unknown3[12]
         00 00 00 62                                element # in offset table which is top level object
"""
"""
HEADER
magic number ("bplist")
file format version

OBJECT TABLE
variable-sized objects

Object Formats (marker byte followed by additional info in some cases)
null	0000 0000
bool	0000 1000			// false
bool	0000 1001			// true
fill	0000 1111			// fill byte
int		0001 nnnn	...		// # of bytes is 2^nnnn, big-endian bytes
real	0010 nnnn	...		// # of bytes is 2^nnnn, big-endian bytes
date	0011 0011	...		// 8 byte float follows, big-endian bytes
data	0100 nnnn	[int]	...	// nnnn is number of bytes unless 1111 then int count follows, followed by bytes
string	0101 nnnn	[int]	...	// ASCII string, nnnn is # of chars, else 1111 then int count, then bytes
string	0110 nnnn	[int]	...	// Unicode string, nnnn is # of chars, else 1111 then int count, then big-endian 2-byte uint16_t
		0111 xxxx			// unused
uid		1000 nnnn	...		// nnnn+1 is # of bytes
		1001 xxxx			// unused
array	1010 nnnn	[int]	objref*	// nnnn is count, unless '1111', then int count follows
		1011 xxxx			// unused
		1100 xxxx			// unused
dict	1101 nnnn	[int]	keyref* objref*	// nnnn is count, unless '1111', then int count follows
		1110 xxxx			// unused
		1111 xxxx			// unused

OFFSET TABLE
list of ints, byte size of which is given in trailer
-- these are the byte offsets into the file
-- number of these is in the trailer

TRAILER
byte size of offset ints in offset table
byte size of object refs in arrays and dicts
number of offsets in offset table (also is number of objects)
element # in offset table which is top level object

"""

import struct
import ctypes
import datetime
import plistlib
import uuid
import binascii

#DT_EPOCH = datetime.datetime(2000,12,31)
DT_EPOCH = datetime.datetime(2001,1,1) #33 41 CC 40 66 84 00 00 00

uintfmt_byte_size = ['B','H','L','Q']
realfmt_byte_size = ['?','?','f','d']

class bplist:
    def __init__(self):
        #print("__name__")        
        self.objs = []
        self.byte_size_in_ofs = 0
        self.byte_size_obj_ref = 0
        self.number_of_objects = 0
        self.top_level_object_offset = 0
        self.ofs_tbl = []

    def _calcobjref(self, obj):
        idx = len(self.objs)
        t = type(obj).__name__
        #array to objref*, and dict to keyref* objref*
        if  t in ['tuple', 'list']:
            self.objs.append([])
            newobj = self.objs[-1]
            for o in obj: 
                objref = self._calcobjref(o)
                newobj.append(objref)            
        elif t == 'dict':    # dict
            self.objs.append({})
            newobj = self.objs[-1]
            for k,o in obj.items():
                keyref = self._calcobjref(k)
                objref = self._calcobjref(o)
                newobj[keyref] = objref
        else:
            # already existed?
            if t == 'str':
                for idx_found in range(len(self.objs)):
                    o = self.objs[idx_found]
                    if type(o).__name__ == 'str' and o == obj:
                        return idx_found
            # not found
            self.objs.append(obj)
        #print(idx)
        return idx
        
    def _calcbytesize(self, i):
        _I8_MIN = -128
        _I8_MAX = 127
        _UI8_MAX = 255
        _I16_MIN = -32768
        _I16_MAX = 32767
        _UI16_MAX = 65535
        _I32_MIN = -2147483648
        _I32_MAX = 2147483647
        _UI32_MAX = 4294967295
        _I64_MIN = -9223372036854775808
        _I64_MAX = 9223372036854775807
        _UI64_MAX = 18446744073709551615

        if 1:
            if i <= _UI8_MAX:
                return 0
            elif i <= _UI16_MAX:
                return 1
            elif i <= _UI32_MAX:
                return 2
            elif i <= _UI64_MAX:   # 8 bytes
                return 3
            else:    
                assert 0
        else:
            if _I8_MIN <= i <= _I8_MAX:
                return 0
            elif _I16_MIN <= i <= _I16_MAX:
                return 1
            elif _I32_MIN <= i <= _I32_MAX:
                return 2
            elif _I64_MIN <= i <= _I64_MAX:   # 8 bytes
                return 3
            else:    
                assert 0

    def _dumpobjlen(self, f_byte, obj_len):
        b = bytearray()
        if obj_len<0xF:
            b.append(f_byte | obj_len)
        else:
            b.append(f_byte | 0b00001111)
            b += self.dumps(obj_len)
        return b

    def dumps(self, obj): 
        b = bytearray()
        t = type(obj).__name__ 
        if repr(obj) == 'None':
            b.append(0b00000000)
        elif repr(obj) == 'False':
            b.append(0b00001000)
        elif repr(obj) == 'True':
            b.append(0b00001001)
        elif t == 'int': #type(0):  # int 
            #print("int")
            #int		0001 nnnn	...		// # of bytes is 2^nnnn, big-endian bytes
            b_cnt = self._calcbytesize(obj)
            b.append(0b00010000 | b_cnt)
            b += struct.pack('!%s'%(uintfmt_byte_size[b_cnt]), obj)
        elif t == 'float':#type(0.0): # float
            #print("float")
            #real	0010 nnnn	...		// # of bytes is 2^nnnn, big-endian bytes
            b.append(0b00100000 | 3)
            b += struct.pack('!d', obj) #'!f'
        elif t == 'datetime': #type(datetime.datetime.now()):    # datetime.datetime
            #print("datetime.datetime")
            #date	0011 0011	...		// 8 byte float follows, big-endian bytes
            delta = obj - DT_EPOCH
            b.append(0b00010000 | 3)
            b += struct.pack('!d', delta.days*24*60*60+delta.seconds) #'!f'            
        elif t == 'Data': #type(plistlib.Data(b'')):        # not plistlib.Data
            #print("plistlib.Data")
            #data	0100 nnnn	[int]	...	// nnnn is number of bytes unless 1111 then int count follows, followed by bytes
            obj_len = len(obj.data)
            b += self._dumpobjlen(0b01000000, obj_len)
            b += obj.data
        elif t == 'str': #type(""):      
            if len(obj.encode()) == len(obj):   # ascii
                #print("ascii")
                #string	0101 nnnn	[int]	...	// ASCII string, nnnn is # of chars, else 1111 then int count, then bytes
                obj_len = len(obj)
                b += self._dumpobjlen(0b01010000, obj_len)
                b += bytes(obj, "utf_8")
            else:                           # unicode
                #print("unicode")
                #string	0110 nnnn	[int]	...	// Unicode string, nnnn is # of chars, else 1111 then int count, then big-endian 2-byte uint16_t
                obj_len = len(obj)
                b += self._dumpobjlen(0b01100000, obj_len)
                b.append(bytes(obj, "utf16_le"))
        elif t == 'uuid.UUID':        #uid type(uuid.uuid4()
            #print("uid")
            #uid		1000 nnnn	...		// nnnn+1 is # of bytes
            obj_len = len(obj)
            b += self._dumpobjlen(0b10000000, obj_len)
            b += obj.bytes
        elif t in ['tuple', 'list']: #type([]) or type(obj) == type(()): # tuple or list
            #print("array")
            #array	1010 nnnn	[int]	objref*	// nnnn is count, unless '1111', then int count follows 
            obj_len = len(obj)          
            b += self._dumpobjlen(0b10100000, obj_len)
            # objref*
            #binascii.a2b_hex(("%%0%dx"%(2*2))%0x123)
            for objref in obj:
                b += binascii.a2b_hex(("%%0%dx"%(2*self.byte_size_obj_ref))%objref)
        elif t == 'dict':#type({}):    # dict
            #print("dict")
            #dict	1101 nnnn	[int]	keyref* objref*	// nnnn is count, unless '1111', then int count follows
            obj_len = len(obj)
            b += self._dumpobjlen(0b11010000, obj_len)
            # keyref* objref*        
            for keyref in obj.keys():
                b += binascii.a2b_hex(("%%0%dx"%(2*self.byte_size_obj_ref))%keyref)
            for objref in obj.values():
                b += binascii.a2b_hex(("%%0%dx"%(2*self.byte_size_obj_ref))%objref)
        else:
            print(hex(len(b)))
            assert 0
        return b

    def _loadobjlen(self, s, ofs):
        len_or_fill = s[ofs] & 0xF
        if len_or_fill == 0b1111:
            hbit = s[ofs+1] >> 4
            lbit = s[ofs+1] & 0xF
            if hbit == 0b0001:
                return self.loads(s, ofs+1), ofs + 2 + 2**lbit
            else:
                print(hex(ofs))
                assert 0
        else:
            return len_or_fill, ofs + 1
        
    def loads(self, s, ofs): 
        #print(hex(ofs))   
        hbit = s[ofs] >> 4
        lbit = s[ofs] & 0xF
        if hbit == 0b0000:
            if lbit == 0b0000:
                #print("null")
                return None
            elif lbit == 0b1000:
                #print("false")
                return False
            elif lbit == 0b1001:
                #print("true")
                return True
        elif hbit == 0b0001:
            #print("int")
            s_ofs, e_ofs = ofs + 1, ofs + 2**lbit + 1
            return struct.unpack("!%s"%(uintfmt_byte_size[lbit]), s[s_ofs:e_ofs])[0]
        elif hbit == 0b0010:
            #print("real")
            s_ofs, e_ofs = ofs + 1, ofs + 2**lbit + 1
            if lbit == 0b0011:
                return struct.unpack("!%s"%(realfmt_byte_size[lbit]), s[s_ofs:e_ofs])[0]
            else:
                assert 0
        elif hbit == 0b0011:
            #print("datetime")
            s_ofs, e_ofs = ofs + 1, ofs + 2**lbit + 1
            if lbit == 0b0011:
                delta = struct.unpack("!d", s[s_ofs:e_ofs])[0]
                return DT_EPOCH + datetime.timedelta(seconds=delta)
            else:
                assert 0
        elif hbit == 0b0100:
            #print("data")
            b_cnt, s_ofs = self._loadobjlen(s, ofs)
            #print("len is", hex(b_cnt))
            e_ofs = s_ofs + b_cnt
            return plistlib.Data(s[s_ofs:e_ofs])
        elif hbit == 0b0101:
            #print("ascii string")    
            b_cnt, s_ofs = self._loadobjlen(s, ofs)
            e_ofs = s_ofs + b_cnt
            return s[s_ofs:e_ofs].decode('utf_8')
        elif hbit == 0b0110:
            #print("unicode string")
            b_cnt, s_ofs = self._loadobjlen(s, ofs)
            e_ofs = s_ofs + b_cnt
            return s[s_ofs:e_ofs].decode('utf_16be')
        elif hbit == 0b1000:
            #print("uid")            
            b_cnt, s_ofs = self._loadobjlen(s, ofs)
            e_ofs = s_ofs + b_cnt            
            return uuid.UUID(bytes=bytes(s[s_ofs:e_ofs]))
        elif hbit == 0b1010:
            #print("array")
            b_cnt, s_ofs = self._loadobjlen(s, ofs)
            e_ofs = s_ofs + self.byte_size_obj_ref*b_cnt          
            obj_idxs = []
            for idx in range(s_ofs,e_ofs,self.byte_size_obj_ref):
                obj_idxs.append(int(binascii.b2a_hex(s[idx:idx+self.byte_size_obj_ref]),16))
            new_obj = []
            for i in obj_idxs:
                o = self.loads(s, self.ofs_tbl[i])
                new_obj.append(o)
            return new_obj
        elif hbit == 0b1101:
            #print("dict")
            b_cnt, s_ofs = self._loadobjlen(s, ofs)
            e_ofs = s_ofs + self.byte_size_obj_ref*2*b_cnt  
            obj_idxs = []
            for idx in range(s_ofs,e_ofs,self.byte_size_obj_ref):
                obj_idxs.append(int(binascii.b2a_hex(s[idx:idx+self.byte_size_obj_ref]),16))
            new_obj = {}
            for i in range(0, b_cnt):
                k = self.loads(s, self.ofs_tbl[obj_idxs[i]])
                v = self.loads(s, self.ofs_tbl[obj_idxs[i+b_cnt]])
                new_obj[k] = v
            return new_obj
        else:
            #print("unknown")
            print(hex(ofs))
            assert 0

    def readPlistFromString(self, data):
        #print("readPlistFromString")
        #header
        magic = data[0:6]
        version = data[6:8]
        #print(magic, version)
        # trailer
        trailer = struct.unpack("!6xbb4xl12xl", data[-0x20:])
        self.byte_size_in_ofs = trailer[0]
        self.byte_size_obj_ref = trailer[1]
        self.number_of_objects = trailer[2]
        self.top_level_object_offset = trailer[3]
        #print(trailer)
        # ofs_tbl
        #011DAB #hex(int(binascii.b2a_hex(b'\x12\x34\x56'),16))
        self.ofs_tbl = []
        for idx in range(self.top_level_object_offset,len(data)-0x20,self.byte_size_in_ofs):
            self.ofs_tbl.append(int(binascii.b2a_hex(data[idx:idx+self.byte_size_in_ofs]),16))
        #print(self.ofs_tbl)
        # obj_tbl
        rootObject = self.loads(data, self.ofs_tbl[0])
        return rootObject

    def writePlistToString(self, rootObject):
        #print("writePlistToString")
        # header
        b= b"bplist00"
        # get byte_size_obj_ref
        self._calcobjref(rootObject)
        self.byte_size_obj_ref = 2 ** self._calcbytesize(len(self.objs))
        #print(self.byte_size_obj_ref)
        self.ofs_tbl = []
        # obj_tbl
        for obj in self.objs:
            self.ofs_tbl.append(len(b))
            b += self.dumps(obj)
        
        # ofs_tbl
        self.top_level_object_offset = len(b)
        self.byte_size_in_ofs = 2 ** self._calcbytesize(self.ofs_tbl[-1]) 
        for ofs in self.ofs_tbl:
            b += binascii.a2b_hex(("%%0%dx"%(2*self.byte_size_in_ofs))%ofs)
        # trailer
        b += struct.pack("!6xbb4xl12xl", 
            self.byte_size_in_ofs, 
            self.byte_size_obj_ref, 
            self.number_of_objects, 
            self.top_level_object_offset)
       
        return b

    def readPlist(self, pathOrFile):
        fp = open(pathOrFile, "rb")
        s = fp.read()
        pl = self.readPlistFromString(s)
        fp.close()
        return pl

    def writePlist(self, rootObject, pathOrFile):
        fp = open(pathOrFile, "wb")
        s = self.writePlistToString(rootObject)
        fp.write(s)
        fp.close()   

if __name__ == '__main__':
    b = bplist()
    pl = b.readPlist("1")
    import pprint
    pprint.pprint(pl)
    #b.writePlist(pl, "2")
    