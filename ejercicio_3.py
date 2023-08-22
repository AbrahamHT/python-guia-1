def main():
    n=int(input("favor ingresar un numero : "))
    for i in range(2,n):
        if n%i == 0 :
            print("el numero ingresado no es primo")
            break
        if n == 1:
            print("el numero ingresado no es primo")
            break
    else:
        print("el numero ingresado es primo")
if __name__== "__main__":
    main()