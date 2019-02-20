def greater(a,b,c):
    x=a if (a<b and a<c) else b
    if ( c<a and c<b):
        x=c
        return x
    def main():
        a=77
        b=234
        c=222
        d=greatest(a,b,c)
        print(d)
        main()

