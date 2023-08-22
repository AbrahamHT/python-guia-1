def main():
    salir=str("salir")
    palabra=0
    while palabra != salir:
        palabra=str(input("favor ingresar una palabra : "))
        a=palabra[::-1]
        if palabra == salir:
            print("--saliendo--")
        else:
            print(a)
if __name__== "__main__":
    main()
