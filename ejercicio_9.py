def main():
    palabras=str(input("favor ingresar palabras : "))
    palabras=palabras.split(' ')
    con=len(palabras)
    aux=0
    for i in range(con):
        con=len(palabras[i])
        if con > aux:
            aux=con
            pal=i
    print(f"la palabra mas larga es {palabras[i]} con un largo de {aux}")
if __name__== "__main__":
    main()
