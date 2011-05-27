"""
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 0 0 0 0
"""

##################
"""
 2 0 6 0 8 0 3 0 0
 1 0 9 0 4 0 0 8 7
 7 0 0 0 0 0 0 0 0
 0 0 0 0 6 3 0 0 0
 6 0 4 0 0 2 1 0 8
 0 0 0 0 0 1 0 4 0
 0 7 0 0 0 8 0 0 0
 0 0 0 5 0 4 0 9 0
 0 0 0 2 0 7 0 6 0
"""
"""
 2 4 6 7 8 5 3 1 9
 1 5 9 3 4 6 2 8 7
 7 8 3 1 2 9 4 5 6
 8 1 7 4 6 3 9 2 5
 6 3 4 9 5 2 1 7 8
 9 2 5 8 7 1 6 4 3
 4 7 2 6 9 8 5 3 1
 3 6 8 5 1 4 7 9 2
 5 9 1 2 3 7 8 6 4
"""
##################
"""
 0 0 4 0 0 0 0 0 7
 3 0 6 0 0 0 0 0 0
 0 0 9 0 6 4 1 0 2
 9 5 0 0 8 0 0 7 4
 7 0 0 2 0 0 6 0 0
 2 0 0 0 1 0 9 5 0
 0 0 0 7 0 1 0 0 6
 0 0 0 0 0 0 0 0 0
 0 0 0 0 0 9 5 1 0
"""
"""

 1 2 4 9 5 3 8 6 7
 3 8 6 1 7 2 4 9 5
 5 7 9 8 6 4 1 3 2
 9 5 1 3 8 6 2 7 4
 7 4 3 2 9 5 6 8 1
 2 6 8 4 1 7 9 5 3
 8 9 5 7 4 1 3 2 6
 6 1 2 5 3 8 7 4 9
 4 3 7 6 2 9 5 1 8
"""

##################
m="""
 0 1 0 0 0 0 0 0 0
 9 0 6 0 0 0 0 0 0
 0 0 0 8 0 2 0 3 0
 0 3 9 0 0 0 0 4 0
 7 0 0 0 0 0 0 0 0
 4 8 5 0 0 1 0 6 0
 0 0 0 0 3 4 0 8 0
 0 0 3 0 1 5 0 9 4
 0 0 0 0 0 6 5 0 0
"""
"""
 3 1 8 5 7 9 4 2 6
 9 2 6 1 4 3 8 7 5
 5 4 7 8 6 2 1 3 9
 1 3 9 6 5 7 2 4 8
 7 6 2 4 9 8 3 5 1
 4 8 5 3 2 1 9 6 7
 6 5 1 9 3 4 7 8 2
 8 7 3 2 1 5 6 9 4
 2 9 4 7 8 6 5 1 3
"""

n = 9
d_set = set(xrange(1, 10))

a = [[None for i in xrange(n)] for j in xrange(n)]
t_set =[[None for i in xrange(n) ] for j in xrange(n)]
path = []

def init():
    i=0
    for s in m.split():
        x=i/9
        y= i%9
        #print x,y,s
        a[x][y] = int(s)
        i += 1

def do_copy(a):
    b = [[None for i in xrange(n)] for j in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            b[i][j] = a[i][j]
    return b
    
def test():
    cnt=0
    for i in xrange(n):
        s = ""
        for j in xrange(n):
            refresh_set(i,j)
            s += " " + str(a[i][j])
            if(a[i][j] !=0):
                cnt += 1
        print s
    print cnt
    return cnt
    
def init_set():
    for i in xrange(n):
        for j in xrange(n):
            if a[i][j] != 0:
                t_set[i][j] = set([a[i][j]])
            else:
                t_set[i][j] = d_set.copy()
        
def get_digits_r1(x,y):
    if len(t_set[x][y])==0:
        raise Exception("!!error [%d,%d]"%(x, y))
        
    if len(t_set[x][y])==1:
        #refresh_set(x,y)
        return
        
    #
    for i in xrange(n):
        if i != x:
            if len(t_set[i][y])==1:
                t_set[x][y] -= t_set[i][y]
                if len(t_set[x][y])==1:
                    refresh_set(x,y)
                    return
    
    for j in xrange(n):
        if j != y:
            if len(t_set[x][j])==1:
                t_set[x][y] -= t_set[x][j]
                if len(t_set[x][y])==1:
                    refresh_set(x,y)
                    return
        
    ##
    xl = (x/3)*3
    yt = (y/3)*3
    for i in xrange(xl, xl+3):
        for j in xrange(yt, yt+3):
            if i !=x or i!=y:
                if len(t_set[i][j])==1:
                    t_set[x][y] -= t_set[i][j]
                    if len(t_set[x][y])==1:
                        refresh_set(x,y)
                        return

def get_digits_r2(x,y):
    if len(t_set[x][y])==0:
        #pdb.set_trace()
        raise Exception("!!error [%d,%d]"%(x, y))
        
    if len(t_set[x][y])==1:
        #refresh_set(x,y)
        return
    ###
    t = t_set[x][y].copy()
    #print "..digit.3", x, y, repr(t_set[x][y])
    xl = (x/3)*3
    yt = (y/3)*3
    for i in xrange(xl, xl+3):
        for j in xrange(yt, yt+3):
            if i!=x or j!=y:
                #print "..digit.3.", x, y, i, j, repr(t), repr(t_set[i][j])
                t -= t_set[i][j]
                
    if len(t)==1:
        t_set[x][y] = t
        refresh_set(x,y)
        return
    
    print "..digit..", x, y, repr(t_set[x][y])
    
def refresh_set(x,y):
    if len(t_set[x][y])==1:
        t = t_set[x][y].copy()
        digit = t.pop() 
        #print "==found [%d,%d]:%d"%(x, y, digit)
        a[x][y]=digit
        # 
        for i in xrange(n):
            if i != x:
                t_set[i][y] -= t_set[x][y]
        for j in xrange(n):
            if j != y:
                t_set[x][j] -= t_set[x][y]
        ##
        xl = (x/3)*3
        yt = (y/3)*3
        for i in xrange(xl, xl+3):
            for j in xrange(yt, yt+3):
                if i!=x or j!=y:
                    t_set[i][j] -= t_set[x][y] 

def get_guess_pos():
    for i in xrange(n):
        for j in xrange(n):
            if len(t_set[i][j])>1:
                return i,j

def do_guess():
    global a;
    i,j = get_guess_pos()
    
    b=do_copy(a)
    
    for d in t_set[i][j]:
        print "..try..",i,j,repr(t_set[i][j]),d
        #solve
        try:
            path.append(b)
            a[i][j]=d
            return do_route();
        except Exception as e :
            print e.args
            a = do_copy(path.pop())
            
def do_route():
    init_set()
    print "=============begin============="
    cnt = 0; prev_cnt = 0;
    is_done = False
    while not is_done:
        cnt = test()
        if cnt == 81:
            print "=============end============="
            is_done = True
            break;
        print "..prev_cnt:", prev_cnt, "cnt", cnt
        if(prev_cnt == cnt):
            do_guess()
                            
        prev_cnt = cnt
        
        for i in xrange(n):
            for j in xrange(n):
                get_digits_r1(i,j)
    
        for i in xrange(n):
            for j in xrange(n):
                get_digits_r2(i,j)  
    
                    
if __name__ == '__main__':
    init()
    do_route()
    
