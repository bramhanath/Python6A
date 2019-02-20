def comExp(a,b,c):

    if(a>b and a>c):
        return a
    if(b>a and b>c):
        return b
    
    return c
print(comExp(32,24,12))
