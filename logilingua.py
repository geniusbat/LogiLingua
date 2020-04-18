from random import randint

def initiate(dir): #Da una lista de los datos del directorio
    with open(dir,"r") as file:
        lineas = file.read()
        lineas = "".join(lineas.split())
        datos = lineas.split(",")
    return datos

def generateWord(lista):
    aux = getSmallestLargestWord(lista)
    palabra =""
    #Si fin==1 entonces sale del bucle
    posLetraFin = len(aux[1])
    dicLetras = {}
    #Cogemos cada palabra y metemos sus vocales en un diccionario (dicLetras)
    for elemento in lista:
        i=0
        while (i<len(elemento)):
            #Caso general
            if (i<posLetraFin):
                #Añadimos letra 
                if (i in dicLetras):
                    dicLetras[i]=dicLetras[i]+elemento[i]
                else:
                    dicLetras[i]=elemento[i]
            #Caso vayamos x la siguiente letra a la menor letra
            else:
                num = randint(0,10)
                if (num>=4): #Continuamos
                    posLetraFin+=1
                    #Añadimos letra 
                    if (i in dicLetras):
                        dicLetras[i]=dicLetras[i]+elemento[i]
                    else:
                        dicLetras[i]=elemento[i]
                else:
                    break #Pasamos de la palabra
            i=i+1   

    #print(dicLetras)
    #Creamos la palabra
    i=0
    while(i<len(dicLetras)):
        letras = dicLetras[i]
        number = randint(0,len(letras)-1)
        palabra = palabra + letras[number]
        i+=1
    return palabra

def getSmallestLargestWord(lista):
    menor = lista[0]
    mayor = lista[0]
    for elemento in lista:
        if (len(elemento)>len(mayor)):
            mayor = elemento
        elif (len(elemento)<len(menor)):
            menor = elemento
    return [mayor,menor]

#Funcion que devuelve V si la letra dada es vocal o C si es consonante
def getLetterType(char):
    if ((char=="a")or(char=="e")or(char=="i")or(char=="o")or(char=="u")):
        return "v"
    else: 
        return "c"

def getWordBin(palabra):
    ret = ""
    for i in palabra:
        ret=ret+getLetterType(i)
    return ret

def getListBin(lista):
    aux = getSmallestLargestWord(lista)
    palabra =""
    posLetraFin = len(aux[1])
    dicLetras = {}
    #Cogemos cada palabra y metemos sus vocales en un diccionario (dicLetras)
    for elemento in lista:
        i=0
        while (i<len(elemento)):
            #Caso general
            if (i<posLetraFin):
                #Añadimos letra 
                if (i in dicLetras):
                    dicLetras[i]=dicLetras[i]+getWordBin(elemento[i])
                else:
                    dicLetras[i]=getWordBin(elemento[i])
            #Caso vayamos x la siguiente letra a la menor letra
            else:
                num = randint(0,10)
                if (num>=5): #Continuamos
                    posLetraFin+=1
                    #Añadimos letra 
                    if (i in dicLetras):
                        dicLetras[i]=dicLetras[i]+getWordBin(elemento[i])
                    else:
                        dicLetras[i]=getWordBin(elemento[i])
                else:
                    break #Pasamos de la palabra
            i=i+1   
    #Creamos la palabra
    i=0
    while(i<len(dicLetras)):
        letras = dicLetras[i]
        number = randint(0,len(letras)-1)
        palabra = palabra + letras[number]
        i+=1
    return palabra

#Crea una palabra y la devuelve si cumple con la estructura bin de las palabras
def generateWordOnBin(lista,iterations):
    wordBin = getListBin(lista)
    continua = True
    i=0
    while(continua):
        palabra = generateWord(lista)
        if (getWordBin(palabra)==wordBin):
            continua=False
        #Chequea si usuario desea continuar iteraciones
        i+=1
        if ((i==iterations)and(continua==True)):
            print("Desired word is:"+wordBin)
            print("Actual word is: "+palabra)
            into = input("Press 1 to continue, 0 to finish: ")
            if (into=="1"):
                i=0
            else:
                continua=False
    return palabra
        


if __name__=="__main__":
    #print(generateWord(initiate(r"C:\\Users\\Geniusbat\\Documents\\Proyectos\\Programación\\LogiLingua\\test.txt")))

    print(generateWordOnBin(initiate(r"C:\\Users\\Geniusbat\\Documents\\Proyectos\\Programación\\LogiLingua\\test.txt"),10))