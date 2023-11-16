def encrypt(p,k):
    l,p1,c=[],"",""
    for x in k:
        l.append([x,ord(x)])
    for x in range(len(p)):
        if p[x]==' ':
            continue
        p1+=p[x]
    for x in range(len(p1)):
        l[x%len(k)].extend([p1[x]])


    l.sort(key=lambda inner:inner[1])


    max=0
    for x in range(len(l)):
        if len(l[x])>max:
            max=len(l[x])
    for x in range(len(l)):
        if len(l[x])!=max:
            l[x].extend(['!'])
    for x in l:
        #print(x,len(x),x[0],x[1])
        for y in range(2,len(x)):
            c+=x[y]
    return c

def decrypt(c,key):
    x=len(c)//len(key)
    l,ls=[],[]
    l=list(c)
    for z in range(len(key)):
        d=""
        for y in range(x):
            d+=l[z*x+y]
        ls.append(list(d))
    #print(ls)
    l=list(key)
    l.sort(key=lambda inner:inner[0])
    #print(l)
    for x in range(len(l)):
        ls[x].insert(0,l[x])
    #print(ls)
    l=[]
    for x in range(len(key)):
        for y in range(len(key)):
            if key[x]==ls[y][0]:
                l.append(ls[y])

    de=""
    for x in range(1,len(l[0])):
        for y in range(len(key)):
            de+=l[y][x]
            
    return de



#cryptoanalysis




#p=input("Enter the Plaintext: ")
#key=input("Enter the key: ")
p="this is encryption of transposition cipher"
key="half"
c=encrypt(p,key)
print(c)

d=decrypt(c,key)
print(d)