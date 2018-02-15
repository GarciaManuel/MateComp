from numpy import *

def isSuffix(a , b):
    
    lenA = len(a)
    lenB = len(b)
    if (lenA==0 or lenB==0):
        return True
    if(lenA>=lenB):
        return a.endswith(b)
    if(lenB>lenA):
        return b.endswith(a)
    return True

def equal(a,b):
    
    if(a==b):
        return True
    return False

def transition(p,list,matrix):
    m = len(p)
    al = len(list)
    
    for q in range(0,m+1):
        for a in range(0,al):
            k= min(m+1,q+2)
            k=k-1
            while (not(equal(list[a],p[k-1])) or (not(isSuffix(p[0:k],p[0:q]+list[a])))):
                k=k-1
                if (k<1 or k>m+1):
                    break
            matrix[q][a]=k
    return 0

def matcher(string,matrix,m,alphabet):
    acum=0
    n=len(string)
    q=0
    for i in range(0,n):
        q=matrix[q,alphabet.index(string[i])]
        if q==m:
            acum=acum+1
    print(acum)



import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)


al = lines[0]
p = lines[1]
string = lines[2]
m=len(p)
alphabet=[]

for i in al:
    alphabet.append(i)
sort(alphabet)

limit = m+1
matrix = range(limit*limit)
matrix = reshape(matrix,(limit,limit))


transition(p,alphabet,matrix)
matcher(string,matrix,m,alphabet)


