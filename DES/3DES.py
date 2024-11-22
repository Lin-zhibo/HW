import deskey
from DES import DES
from deskey import createRoundkey

def DES_3(message,keys1,keys2,keys3,mode):
    if mode == "encrypt":
        modes=["encrypt","decrypt", "encrypt"]
    elif mode == "decrypt" :
        modes=["decrypt", "encrypt", "decrypt"]
    else:
        print("error: invalid 3DES mode")
        return
    tmp0=DES(message,keys1,modes[0])
    tmp1=DES(tmp0,keys2,modes[1])
    ciphertxt = DES(tmp1,keys3,modes[2])
    
    return ciphertxt

def DES3(message,keys:list,key_amount,mode):
    if len(keys) != key_amount:
        print("error: the amount of keys is not enough")
        return
    
    match key_amount:
        case 2:
            ciphertext=DES_3(message,keys[0],keys[1],keys[0],mode)
            return ciphertext
        case 3:
            if mode == "decrypt":
                keys=keys[::-1]
            ciphertext=DES_3(message,keys[0],keys[1],keys[2],mode)
            return ciphertext
        case 1:
            print("warning: you only provide 1 key, did you want to run DES?[y/n]")
            answer=input()
            if answer == 'y' or answer == 'Y':
                ciphertext = DES(message,keys[0],mode)
            else:
                print("the programme end, please restart it")
                return
            
            return ciphertext
        case _:
            print("error: invalid amount of keys for 3DES")
            return

if __name__ == "__main__" :
    key0=""
    key1=""
    key2=""
    
    m=""
    
    key=[key0,key1,key2]
    keys=[]
    i=0
    for k in key:
        if k != "":
            keys.append(createRoundkey(k))
            i+=1
            
    C=DES3(m,keys,i,"encrypt")
    print(C)