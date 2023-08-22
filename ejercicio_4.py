def main():
    pri=input("favor ingresar primera palabra : ")
    con=len(pri)
    a=(slice(-3,con))
    pri1=pri[a]
    aa=(slice(-2,con))
    pri2=pri[aa]
    seg=input("favor ingresar segunda palabra : ")
    conn=len(seg)
    b=(slice(-3,conn))
    seg1=seg[b]
    bb=(slice(-2,conn))
    seg2=seg[bb]

    if pri1 == seg1:
        print("ambas palabras riman")
    elif pri2 == seg2:
        print("las palabras escojidas riman un poco")
    else:
        print("estas palabras no riman")
if __name__== "__main__":
    main()