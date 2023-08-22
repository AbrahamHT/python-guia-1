def main():
    N=0
    while N < 1 or N > 6:
        N=int(input("¿Que conversión desea realizar?\n1) centímetros -> pulgadas\n2) metros -> kilometros\n3) onzas -> gramos\n4) milla -> kilometro\n5) celcius -> fahrenheit\n6) Salir\nRESPUESTA:"))

        if N == 1:
            variable=int(input("Favor ingresar centimetros : "))
            R=variable/2.54
            print(f"La conversion de {variable}CM a pulgada es de {R}in")
        elif N==2:
            variable=int(input("Favor ingresar metros :"))
            R=variable/1000
            print(f"La conversion de {variable}M a kilometros es de {R}km")
        elif N==3:
            variable=int(input("Favor ingresar onzas :"))
            R=variable*28.35
            print(f"La conversion de {variable}oz a gramos es de {R}gr")
        elif N==4:
            variable=int(input("Favor ingresar millas :"))
            R=variable*1.609
            print(f"La conversion de {variable}mi a kilometros es de {R}km")
        elif N==5:
            variable=int(input("Favor ingresar celcius :"))
            R=(variable * 9/5) + 32 
            print(f"La conversion de {variable}°C a fahrenheit es de {R}°F")
        elif N==6:
            print("--Has cerrado el conversor--")
            break
if __name__== "__main__":
    main()