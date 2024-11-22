def setkey(stri):
    key=stri[2:]
    for i in range(64-len(key)):
        key="0"+key
    return key

def change1(key):
    ci=[57,49,41,33,25,17,9,
        1,58,50,42,34,26,18,
        10,2,59,51,43,35,27,
        19,11,3,60,52,44,36]
    di=[63,55,47,39,31,23,15,
        7,62,54,46,38,30,22,
        14,6,61,53,45,37,29,
        21,13,5,28,20,12,4]
    c="".join(key[i-1] for i in ci)
    d="".join(key[i-1] for i in di)
    
    return c,d

def change2(c,d):
    tmp=c+d
    tmpi=[14, 17, 11, 24,  1,  5,
        3,  28, 15,  6, 21, 10,
        23, 19, 12,  4, 26,  8,
        16,  7, 27, 20, 13,  2,
        41, 52, 31, 37, 47, 55,
        30, 40, 51, 45, 33, 48,
        44, 49, 39, 56, 34, 53,
        46, 42, 50, 36, 29, 32]
    roundkey="".join(tmp[i-1] for i in tmpi)
    return roundkey
    

def movlft(ar):
    tmp=ar[1:]+ar[0]
    return tmp

def MV(ar, round:int):
    table=[1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    for i in range(table[round]):
        tmp=movlft(ar)
        ar=tmp
    return ar
        
    

def createRoundkey(key):
    if len(key) != 64:
        print("error: key needs to be 64 bits")
        print("key=")
        print(key)
        print("lenth=")
        print(len(key))
        return
    C, D = change1(key)
    keys=[]
    for i in range(16):
        C=MV(C,i)
        D=MV(D,i)
        roundkey=change2(C,D)
        if len(roundkey) != 48:
            print("error: roundkey needs to be 48 bits")
            return
        keys.append(roundkey)
    return keys




#64bit key
if __name__ == "__main__":
    input_key="1100100111010010110111011101111011100111110000111110101111100100"
    
    key=setkey(input_key)
    roundkeys=createRoundkey(key)
    
    print(roundkeys)
    print(len(roundkeys))

