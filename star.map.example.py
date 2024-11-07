#!/usr/bin/python3

data = [
    11,
    "22",
    33
]
def double (algo):
    return algo*2

def doblados(contenedor):
    answ = []
    for item in contenedor:
        answ.append (item*2)
    return answ



if __name__ == "__main__":
    
    # not starred map()
    miMapa = map (double,data)
    print(miMapa) #map object 
    for  item in miMapa: 
        print (item)
        
    #miMapa2 =
    
    