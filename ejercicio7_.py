def main():
    n=int(input("favor ingresar numero a factoriar : "))
    aux=n
    nexclamacion=1

    for i in range(n):
        if n != 0:
            nexclamacion=nexclamacion*n
            n=n-1
        else:
            print(f"el factorial de {aux} es {nexclamacion}")

    print(f"el factorial de {aux} es {nexclamacion}")
if __name__== "__main__":
    main()