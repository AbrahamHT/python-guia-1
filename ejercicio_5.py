def main():
  a=str(input("Favor ingresar palabra :"))
  letra=input("Favor ingresar 1 letra :")
  cont=0
  for i in a: 
      if letra == i:
        cont=cont+1 
  print(f"Las veces que se encuentra la letra{letra} en la palabra {a} es de {cont}")
if __name__== "__main__":
    main()
        