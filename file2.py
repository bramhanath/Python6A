def greater(a,b,c):
    x=a if (a<b and a<c) else b
    if ( c<a and c<b):
        x=c
    print x
    return x
    

greater(5,46,24.8)

