def encrypt(p,key):
    p1=""
    for x in range(len(p)):
        if p[x]==' ':
            continue
        p1+=p[x]
    c,r="",range(len(p1))
    for x in r:
        c+=chr((ord(p1[x])-ord('a')+ord(key[x%len(key)]))%26+ord('A'))
    return c

def decrypt(c,key):
    d,r="",range(len(c))
    for x in r:
        d+=chr((ord(c[x])-ord('A')-ord(key[x%len(key)]))%26+ord('a'))
    return d

#p=input("Enter the Plaintext: ")
#key=input("Enter the key: ")
p="this is vigenere cipher"
key="UAHGTNBP"
c=encrypt(p,key)
print(c)

d=decrypt(c,key)
print(d)

p="thisisvigenerecipher"
cip="AUCLOSJKNRHXXEQKWUYK"
print(len(p),len(cip))
key=""
for x in range(len(p)):
    key+=chr(((ord(cip[x])-ord('A'))-(ord(p[x])-ord('a')))+ord('A'))
print(key)
c,key_f=key[0],""
key_f+=c
i=1
while key[i]!=c:
    key_f+=key[i]

print(key_f)


# for x in ciphertext1:
#     decipher+=chr(ord(key[x])-ord('a')+ord('A'))
# print(decipher)
#new_key= dict([(value, key) for key, value in key.items()])
# rt
