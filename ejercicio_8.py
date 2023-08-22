def main():
    def area_circulo(r):
        A=3.14*r**2
        print(f"El area del circulo es :{A}")
        return A

    r=float(input("Ingrese radio de el circulo: "))

    def volumen_cilindro(h):
        P=area_circulo(r)
        V=P*h
        print(f"El volumen del cilindro es:{V}")
    h=float(input("Ingrese haltura de el Cilindro: "))
    volumen_cilindro(h)
if __name__== "__main__":
    main()