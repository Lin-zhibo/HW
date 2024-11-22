import deskey
import desf
from deskey import createRoundkey
from desf import f
from desf import XORS


def DESRoundOP(Li,Ri,Ki):
    if len(Ki) != 48:
        print("error: roundkey lenth error")
        return
    tmp=f(Ri,Ki)
    if len(tmp) != 32:
        print("error: result of f function needs to be 32 bits")
    round_result=XORS(tmp,Li)
    
    return Ri,round_result # return Li+1, Ri+1

def IP(message):
    IP_table=[
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]
    
    tmpM="".join(message[i-1] for i in IP_table)
    
    L=tmpM[0:32]
    R=tmpM[32:]
    
    return L,R

def IP1(L,R):
    IP1_table=[
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25]
    
    tmpM=L+R
    
    M="".join(tmpM[i-1] for i in IP1_table)
    return M

def DES( message, roundkeys, mode:str):
    if len(message) != 64 :
        print("error: message lenth needs to be 64 bits")
        return
    if mode == "decrypt":
        # print(roundkeys)
        # ka=roundkeys[3]
        roundkeys=roundkeys[::-1]
        # kb=roundkeys[-4]
        # print(roundkeys)
        # print(XORS(ka,kb))
    if mode == "encrypt" or mode == "decrypt":
        L,R=IP(message)
        if len(L) != 32 or len(R) != 32:
            print("error: part message needs to be 32 bits")
            return
        for i in range(16):
            print("round %d start, mode: %s" % ((i+1),mode))
            if len(L) != 32 or len(R) != 32:
                print("error: part message needs to be 32 bits")
                return
            newL,newR=DESRoundOP(L,R,roundkeys[i])
            
            if len(newL) != 32 or len(newR) != 32:
                print("error: new part message needs to be 32 bits")
                return
            
            L=newL
            R=newR
            
            print("round %d end" % ((i+1)))
        C=IP1(R,L)
    
        return C
    else:
        print("error: -1")
        print("wrong mode!")
        return

if __name__ == "__main__":
    m="0110010001101001011011100110111101110011011000010111010101110010" #dinosaur (bytes: 8chars * 8bits)    0x 64696E6F73617572
    key="1100100111010010110111011101111011100111110000111110101111100100" #dinosaur (ascii: 8chars * 7bits)  0x C9D2DDDEE7C3EBE4
    c=DES(m,createRoundkey(key),"encrypt")
    checkM=DES(c,createRoundkey(key),"decrypt")
    # print(m)
    # print(c)
    print("ciphertext:",end='')
    print(hex(int(c,2))) # 0x cf0509c4da15c955
    # print(checkM)
    # print(XORS(m,checkM)) # == 000000000(zeros) 
