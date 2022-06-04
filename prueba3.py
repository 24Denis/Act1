# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 08:13:02 2022

@author: Usuario
"""
print ("CALCULADORA DE COORDENADAS")

print("seleccione el tipo de conversion que desea realizar: ")
print("1. DD a DMS")
print("2. DMS a DD")
opcion = int(input(">> "))
hemlat=str(input("ingrese el hemisferio de la latitud (N/S)"))
print(">> ")
hemlon=str(input("ingrese el hemisferio de la longitud (E/W)"))
print(">> ")

if opcion==1:
    print("ingrese el tipo de numero")
    print("1. Entero")
    print("2. Decimal")
    num=int(input(">> "))
        
    if num==1:
        def DMSlon (a, b, c, d):
            entero = float(input("Ingrese el valor de la coordenada de la longitud: "))
            resultado = (entero*60)
            return resultado
                
        def DMSlat (a, b, c, d):
            entero2= float(input("Ingrese el valor de la coordenada de la latitud: "))
            resultado = (entero2*60)
            return resultado
   
        print ((DMSlon (resultado, "0", "0", hemlon)), (DMSlat (resultado, "0", "0", hemlat)))
    
    elif num==2:
        decDMS2= float(input("Ingrese el valor de los numeros decimales para la longitud: "))
        gradoDMS2= float(input("Ingrese el valor del numero entero para la longitud: "))
        def DMS2lon (a, b, c):
            minutodec=decDMS2*60
            minente=int(minutodec)
            minfin=(minutodec-minente)
            segun=minfin*60
            grado=gradoDMS2
            resultado =  grado, minente, segun
            return resultado
        
        def DMS2lat (a, b, c):
            decDMS2= float(input("Ingrese el valor de los numeros decimales para la longitud: "))
            gradoDMS2= float(input("Ingrese el valor del numero entero para la longitud: "))
            minutodec=decDMS2*60
            minente=int(minutodec)
            minfin=(minutodec-minente)
            segun=minfin*60
            grado=gradoDMS2
            resultado = grado, minente, segun
            return resultado
        print (DMS2lat (decDMS2, gradoDMS2, hemlat), (DMS2lon (decDMS2, gradoDMS2, hemlon)))
        
    else:
            print("opcion incorrecta", exit)
    
elif opcion ==2:
    seg= float(input("Ingrese el valor de los segundos de la longitud: "))
    minu= float(input("Ingrese el valor de los minutos de la longitud: "))
    grad= float(input("Ingrese el valor de los grados de la longitud: "))
    
    def DD (a, b, c):
        resulta=(((seg/60)/60)+(minu/60)+grad)
        return resulta
    def DDlat (a, b, c):
        seg2= float(input("Ingrese el valor de los segundos de la longitud: "))
        minu2= float(input("Ingrese el valor de los minutos de la longitud: "))
        grad2= float(input("Ingrese el valor de los grados de la longitud: "))
        resultad=(((seg2/60)/60)+(minu2/60)+grad2)
        return resultad
    print ("Aqui tienes el resultado: ", str (DD(seg, minu, grad)+"°"), str(DDlat(seg2, minu2, grad2)+"°"))

else:
    print ("Su opcion es incorrecta")
    
