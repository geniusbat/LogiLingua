from random import randint

def initiate(dir): #DIR debe tener r""
    with open(dir,"r") as file:
        lineas = file.read()
        lineas.strip()
        lineas.replace(" ", "")
        lineas = lineas.replace('\r', '').replace('\n', '')
        datos = lineas.split(",")
    return datos

def generateWord(list):
    aux = getSmallestLargestWord(list)
    palabra =""
    fin = 0
    #Si fin==1 entonces sale del bucle
    posLetraFin = len(aux[1])
    while(fin!=1):
        dicLetras = {}
        for elemento in list:
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
                    if (num>=5): #Continuamos
                        posLetraFin+=1
                        #Añadimos letra 
                        if (i in dicLetras):
                            dicLetras[i]=dicLetras[i]+elemento[i]
                        else:
                            dicLetras[i]=elemento[i]
                i=i+1   
        print(dicLetras)
        fin=1    
        #Creamos la palabra
        i=0
        while(i<len(dicLetras)):
            letras = dicLetras[i]
            number = randint(0,len(letras)-1)
            palabra = palabra + letras[number]
            i+=1
    return palabra

def getSmallestLargestWord(list):
    menor = list[0]
    mayor = list[0]
    for elemento in list:
        if (len(elemento)>len(mayor)):
            mayor = elemento
        elif (len(elemento)<len(menor)):
            menor = elemento
    return [mayor,menor]

if __name__=="__main__":
    print(generateWord(initiate(r"C:\\Users\\Geniusbat\\Documents\\Proyectos\\Programación\\LogiLingua\\test.txt")))