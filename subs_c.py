import random

def encrypt(p,k):
    c,r="",range(len(p))
    for x in r:
       c+=k[ord(p[x])-ord('a')]
    return c

def decrypt(c,k):
    d,r="",range(len(c))
    for x in r:
        d+=chr(k.index(c[x])+ord('a'))
    return d


#p=input("Enter the Plaintext: ")
p="thisiscryptoanalysisofsubstitutioncipher"
alpha_list=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random.shuffle(alpha_list)
key="".join(str(x) for x in alpha_list)
random.shuffle(alpha_list)
key1="".join(str(x) for x in alpha_list)
cipher=encrypt(p,key)
#print(cipher)


c=input("Enter the Ciphertext:\n")
d=decrypt(c,key)
print(d)
#print(key,key1)

#Cryptoanalysis using known Plaintext and known Ciphertext
p="EFNLOJYIZDKPMGAUBRQXWSHTCV"
cip="VCRFKOLJXUAHGTNBPQWYMEZSID"
ciphertext="cryptoanalysisofsubstitutioncipher"
key_inv,key={},{}
for x in range(len(p)):
    key[cip[x]]=p[x]
for x in range(len(p)):
    key[p[x]]=cip[x]
print(key)
ciphertext1,decipher="",""
for x in ciphertext:
    if x!=" ":
        ciphertext1+=x
#print(ciphertext1)
for x in ciphertext1:
    decipher+=chr(ord(key[x])-ord('a')+ord('A'))
print(decipher)
#new_key= dict([(value, key) for key, value in key.items()])
for x in ciphertext1:
    decipher+=chr(ord(key[x])-ord('A')+ord('a'))
print(decipher)
