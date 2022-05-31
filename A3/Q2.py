a=(2,1)
lst=list(a)

def lucasReg(n):
    if n < 3:
        if n==1:
            print(lst[0])
        if n==2:
            print(lst[0:2])
    elif n==3:
        lst.append(lst[0]+lst[1])
    else:
        i=0
        elt1=lst[0]
        elt2=lst[1]
        for i in range (2,n):
            elt3,elt1 = elt1+elt2,elt2
            elt2=elt3
            lst.append(elt3)
        return lst


def lucasGen(n):
    elt1, elt2 = 2, 1
    for i in range(n):
        yield elt1
        elt1, elt2 = elt2, elt1 + elt2


print(lucasReg(5))
print(list(lucasGen(5)))

