def main():
    
    import random 
    a=int(random.randrange(1,100))

    b=int(input("favor ingresar numero de 1 a 100 : "))
    while b != a:
        if b < a:
            print("el numero ingresado es menor al numero deseado \n ")
        else:
            print("el numero ingresado es mayor al numero deseado \n ")
        b=int(input("favor ingresar numero de 1 a 100 : "))
        
    print(f"el numero ingresado es igual al numero alazar {b}")
if __name__== "__main__":
    main()

