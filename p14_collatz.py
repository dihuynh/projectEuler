#!/usr/bin/env python

#!/usr/bin/env python

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2013
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

# a global dictionary for a lazy cache
global cache
global cache_lazy
cache = dict()
cache_lazy = dict()
cache_lazy = {1:1}
 

def collatz_read (r) :
    """
    r is a  reader
    returns an generator that iterates over a sequence of lists of ints of length 2
    """
    for s in r :
        l = s.split()
        b = int(l[0])
        e = int(l[1])
        assert b > 0
        assert e > 0
        yield [b, e]

# ------------
# collatz_eval
# ------------
def collatz_eval ((i, j)) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    generate_cache()
    
    v = 1
    if (j< i):
        i,j=j,i

    if ( i < j/2) :
        i = j/2
 
    #indexes of i and j in cache
    ii = i / 10000
    ij = j / 10000
    
    #print "J-I = ", (j-i)
    #print "ii and ij ", ii, " " , ij

    if (ii == ij and i <= cache[ii][0] <= j):
        return cache[ii][1]
    
    #if it's small enough and is between ranges
    # do the computation
    if (j-i <= 10000):
        return collatz_eval_simple((i,j))

    index = ii

    #go through each range to find the max length
    while (index < ij):
        #print "index is ", index
        #print "cache[index][0] " , cache[index][0]
        if ( i <= cache[index][0] and cache[index][1] > v):
            v = cache[index][1] #current max length
        elif ( i >= cache[index][0]) :
            temp2 = collatz_eval_simple((i,(ii+1)*10000))
            if (temp2 > v):
                v = temp2

        if (cache[index][1] > v):
            v = cache[index][1]
        index+=1
        #corner case, if it reaches ij
        if (ij == index and j < cache[index][0]):
            temp2 = collatz_eval_simple(((ij*10000),j))
            if (temp2> v):
                v = temp2
        else:
            if(cache[index][1]> v):
                v = cache[index][1]
            
    assert v > 0
    return v


# -------------------
# collatz_eval_simple
# ------------------

def collatz_eval_simple ((i, j)) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    Uses
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    v = 1
    if (j< i):
        i,j=j,i

    if ( i < j/2) :
        i = j/2
    for k in range(i, j+1):
        temp = collatz_getLength(k)
        if (temp > v):
            v = temp

    assert v > 0
    return v

# -----------------
# collatz_getLength
# -----------------

def collatz_getLength(k) :
    """
    helper method to find the cycle length of the parameter
    """
    c = 1

    assert k>0

    if (k in cache_lazy):
        return cache_lazy[k]
    else: # not in the cache
        if (k%2) == 0:
            c = 1+ collatz_getLength(k/2)
        else :
            c= 2+ collatz_getLength((3*k+1)/2)

        cache_lazy[k]=c
        
    assert c>0
    return c

def generate_cache(): 
    cache[0]=(6171,262)
    cache[1]=(17647,279)
    cache[2]=(26623,308)
    cache[3]=(35655,324)
    cache[4]=(45127,314)
    cache[5]=(52527,340)
    cache[6]=(60975,335)
    cache[7]=(77031,351)
    cache[8]=(87087,333)
    cache[9]=(91463,333)
    cache[10]=(106239,354)
    cache[11]=(115547,349)
    cache[12]=(129991,344)
    cache[13]=(135111,344)
    cache[14]=(142587,375)
    cache[15]=(156159,383)
    cache[16]=(160411,370)
    cache[17]=(173321,347)
    cache[18]=(180463,365)
    cache[19]=(195465,360)
    cache[20]=(206847,373)
    cache[21]=(216367,386)
    cache[22]=(225023,368)
    cache[23]=(230631,443)
    cache[24]=(240617,368)
    cache[25]=(254911,363)
    cache[26]=(263103,407)
    cache[27]=(270271,407)
    cache[28]=(288489,389)
    cache[29]=(298843,371)
    cache[30]=(300030,371)
    cache[31]=(312318,384)
    cache[32]=(324551,384)
    cache[33]=(336199,366)
    cache[34]=(345947,441)
    cache[35]=(351359,379)
    cache[36]=(360361,410)
    cache[37]=(376603,423)
    cache[38]=(389191,436)
    cache[39]=(394655,405)
    cache[40]=(405407,405)
    cache[41]=(410011,449)
    cache[42]=(423679,418)
    cache[43]=(438699,400)
    cache[44]=(448265,369)
    cache[45]=(450651,387)
    cache[46]=(461262,444)
    cache[47]=(474121,382)
    cache[48]=(480481,413)
    cache[49]=(492571,426)
    cache[50]=(502137,426)
    cache[51]=(511935,470)
    cache[52]=(525543,408)
    cache[53]=(532715,377)
    cache[54]=(546681,452)
    cache[55]=(554143,421)
    cache[56]=(564905,421)
    cache[57]=(576978,390)
    cache[58]=(583787,434)
    cache[59]=(591983,403)
    cache[60]=(601327,403)
    cache[61]=(615017,447)
    cache[62]=(626331,509)
    cache[63]=(635519,416)
    cache[64]=(640641,416)
    cache[65]=(656761,429)
    cache[66]=(665215,442)
    cache[67]=(675969,385)
    cache[68]=(686985,398)
    cache[69]=(691894,442)
    cache[70]=(704623,504)
    cache[71]=(712683,411)
    cache[72]=(720722,411)
    cache[73]=(735679,424)
    cache[74]=(740306,393)
    cache[75]=(753206,424)
    cache[76]=(767903,468)
    cache[77]=(775035,437)
    cache[78]=(788315,406)
    cache[79]=(796095,468)
    cache[80]=(801769,406)
    cache[81]=(818943,450)
    cache[82]=(820022,450)
    cache[83]=(837799,525)
    cache[84]=(847358,419)
    cache[85]=(854191,419)
    cache[86]=(865401,388)
    cache[87]=(871915,432)
    cache[88]=(886953,445)
    cache[89]=(894623,370)
    cache[90]=(906175,445)
    cache[91]=(910107,476)
    cache[92]=(927003,476)
    cache[93]=(939497,507)
    cache[94]=(940257,383)
    cache[95]=(950943,414)
    cache[96]=(960962,414)
    cache[97]=(970599,458)
    cache[98]=(980905,427)
    cache[99]=(997823,440)
# -------------
# collatz_print
# -------------

def collatz_print (w, (i, j), v) :
    """
    prints the values of i, j, and v
    w is a writer
    v is the max cycle length
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    for t in collatz_read(r) :
        v = collatz_eval(t)
        collatz_print(w, t, v)

