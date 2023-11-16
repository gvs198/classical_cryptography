#Encryption of Affine Cipher
def encrypt(p,k1,k2):
    c,r="",range(len(p))
    for x in r:
        if p[x]==' ':
            continue
        c+=chr(((ord(p[x])-ord('a'))*k1+k2)%26+ord('A'))
    return c

#Decryption of Affine Cipher
def inv(k1):
    a=0
    for x in range(1,26,1):
        if (k1*x)%26==1:
            a=x
            break
    return a

def decrypt(c,k1,k2):
    d,r="",range(len(c))
    k1_inv=inv(k1)
    for x in r:
        d+=chr(((ord(c[x])-ord('A'))*k1_inv-k2*k1_inv+26)%26+ord('a'))
    return d

#Cryptoanalysis of Affine Cipher
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

def inv(k1):
    a=0
    for x in range(1,26,1):
        if (k1*x)%26==1:
            a=x
            break
    return a

def decrypt(c,k1_inv,k2):
    d,r="",range(len(c))
    for x in r:
        d+=chr(((ord(c[x])-ord('A'))*k1_inv-k2*k1_inv+26)%26+ord('a'))
    return d





l=input("Enter the key K1,K2 btw space:\n").split(' ')
p=input("Enter the Plaintext:\n")
cipher=encrypt(p,int(l[0]),int(l[1]))
print(cipher)

l=input("Enter the above key K1,K2 btw space:\n").split(' ')
c=input("Enter the above Ciphertext:\n")
d=decrypt(c,int(l[0]),int(l[1]))
print(d)

c=input("Enter the cipher:\n")
l,r=[],range(1,26,1)
for x in r:
    k1_inv=inv(x)
    if k1_inv==0:
        continue
    for k2 in range(26):
        d=decrypt(c,k1_inv,k2)
        l.append([x,k2,d,chi_square(d),])
l.sort(key=lambda inner:inner[3])
for x in l:
    print(x)