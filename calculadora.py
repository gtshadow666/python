#Creamos la calases de la culaculadora para poder generr el bjetos
class calculadora:
    def __init__ (self):#Le decimos con que va a trabajar
        pass
    def suma(self,a,b):#se encargar de hacer la suama
        return a + b
    def resta(self,a,b):#se cncarga de hacer la resta
        return a-b
    def division(self,a,b):#se encraga de la diviosn
        return a/b
    def multriplicar(self,a,b):#se encarga de la multriplicacion
        return a*b
    def elevar(self,a,b):# De elevar los numero el primero elevado al segundo asi que acpetra cualquier exponenetene que sea un numero real ya que usamos flopat y los irracionales estan dentro
        return a**b

while True:# bucle para que la calculadora nunca pare
    selecion= input("Puedes hacer suma, resta, multriplicacion , divison o potencia escoje una:")
    while True:# bucle para conseguir los numeros y no para hsat que el suraio nos de el primer nuemoro bien
        try:
            num1=float(input("Primer numero:"))
            break
        except ValueError:
            print("Ingrese un numero")
    while True:# lo meismo que el bucle de arriba pero para el numero dos
        try:
            num2=float(input("Segundo numero:"))
            break
        except ValueError:
            print("Ingrese un numero")
    calcular=calculadora()#creamos la instancia del objeto para luego poder llamralo sin ningun problema
    if selecion.lower() == "suma":
        print(calcular.suma(num1,num2))#usamos el atributo del objeto
    elif selecion.lower() == "resta":
        print(calcular.resta(num1,num2))#usamos el atributo resta del objeto
    elif selecion.lower() == "multriplicacion":
        print(calcular.multriplicar(num1,num2))
    elif selecion.lower() == "divison":
        print(calcular.division(num1,num2))
    elif selecion.lower() == "potencia":
        print(calcular.elevar(num1,num2))
    else:
        print("Algo salio mal vuelve a intentarlo, gracias")