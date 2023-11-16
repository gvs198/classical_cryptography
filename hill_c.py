#Encryption of Hill Cipher by 2*2 matrix
def encrypt(p,key):
    c,p1,r="","",range(len(p))
    for x in r:
        if p[x]==' ':
            continue
        p1+=p[x]
    if len(p1)%2==1:
        p1+='z'
    print(p1,len(p1))
    i=0
    while i<len(p1)-1:
            c+=chr((((ord(p1[i])-ord('a'))*key[0][0]+(ord(p1[i+1])-ord('a'))*key[0][1])%26)+ord('A'))
            c+=chr((((ord(p1[i])-ord('a'))*key[1][0]+(ord(p1[i+1])-ord('a'))*key[1][1])%26)+ord('A'))
            i+=2
    return c


#Decryption of Hill Cipher if key are known
def inv(k1):
    a=0
    for x in range(1,26):
        #print(k1*x%26,x)
        if (k1*x)%26==1:
            a=x
            break
    return a

def decrypt(c,k):
    de,r="",range(len(c))
    det=k[0][0]*k[1][1]-k[0][1]*k[1][0]
    print(det)
    dt_inv=inv(det)
    print(dt_inv)
    if dt_inv==0:
        return ""
    a,b,ce,d=(dt_inv*k[1][1])%26,(dt_inv*(-k[1][0]))%26,(dt_inv*(-k[0][1]))%26,(dt_inv*k[0][0])%26
    k_inv=[[a,ce],[b,d]]
    print(k_inv)
    i=0
    while i<len(c)-1:
         de+=chr((((ord(c[i])-ord('A'))*k_inv[0][0]+(ord(c[i+1])-ord('A'))*k_inv[0][1])%26)+ord('a'))
         de+=chr((((ord(c[i])-ord('A'))*k_inv[1][0]+(ord(c[i+1])-ord('A'))*k_inv[1][1])%26)+ord('a'))
         i+=2
    return de
        

#cryptoanalysis
freq={
    "A":0.082,
    "B":0.015,
    "C":0.028,
    "D":0.043,
    "E":0.127,
    "F":0.022,
    "G":0.02,
    "H":0.061,
    "I":0.07,
    "J":0.0002,
    "K":0.0008,
    "L":0.04,
    "M":0.024,
    "N":0.067,
    "O":0.075,
    "P":0.019,
    "Q":0.0001,
    "R":0.06,
    "S":0.063,
    "T":0.091,
    "U":0.028,
    "V":0.01,
    "W":0.023,
    "X":0.0001,
    "Y":0.02,
    "Z":0.0001
}

def chi_square(d):
    s,r=0,range(len(d))
    for x in r:
        s+=(d.count(d[x])-freq[chr(ord(d[x])-32)]*len(d))**2/d.count(d[x])
    return s

def decrypto(c,k):
    de,r="",range(len(c))
    det=k[0][0]*k[1][1]-k[0][1]*k[1][0]
    #print(det)
    dt_inv=inv(det)
    #print(dt_inv)
    if dt_inv==0:
        return ""
    a,b,ce,d=(dt_inv*k[1][1])%26,(dt_inv*(-k[1][0]))%26,(dt_inv*(-k[0][1]))%26,(dt_inv*k[0][0])%26
    k_inv=[[a,ce],[b,d]]
    #print(k_inv)
    i=0
    while i<len(c)-1:
         de+=chr((((ord(c[i])-ord('A'))*k_inv[0][0]+(ord(c[i+1])-ord('A'))*k_inv[0][1])%26)+ord('a'))
         de+=chr((((ord(c[i])-ord('A'))*k_inv[1][0]+(ord(c[i+1])-ord('A'))*k_inv[1][1])%26)+ord('a'))
         i+=2
    return de

def crypto(cip):
    t="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    r=range(26)
    ls=[]
    for i in r:
        for j in r:
            for k in r:
                for l in r:
                    key=[[ord(t[i])-ord('A'),ord(t[j])-ord('A')],[ord(t[k])-ord('A'),ord(t[l])-ord('A')]]
                    dec=decrypto(cip,key)
                    #print(key)
                    if dec!="":
                      ls.append([dec,chi_square(dec)])
                      #print([dec,chi_square(dec)])
    ls.sort(key=lambda inner:inner[1])
    for x in range(len(ls)):
       if p==ls[x][0]:
          print(ls[x])

p="this is encryption of hill cipher"
#key=[[ord('B')-ord('A'),ord('A')-ord('A')],[ord('T')-ord('A'),ord('H')-ord('A')]]
key=[[1,5],[3,4]]
#print(key)
cipher=""
cipher=encrypt(p,key)
#print(cipher)
print("Encrypted Data: \n",cipher,len(cipher))
print()

d=decrypt(cipher,key)
print("Decryption of Hill CipherText from known key:")
print(d,len(d))
print()
crypto(cipher)