import json
from datetime import datetime
from datetime import timedelta

#APERTURA Y CARGA DE ARCHIVO JSON
with open('prueba.json') as f:
  data = json.load(f)


potenciasID=[]
fechaIni=[]
fechaFin=[]

def seteo(a,b,c):
  
    for x in data:
        a.append(x["id_potencia"])
        b.append(x["fecha_inicio"])
        c.append(x["fecha_termino"])

# def lecturaDatos():
#     for id,ini,fin in  zip(potenciasID,fechaIni,fechaFin):
#         print('Inicio: {} Termino: {}  ID:{} '.format(ini,fin,id))



dt_apertura=[]

dt_cierre=[]

def recorte(fecha_apertura,fecha_cierre):
    x=0
    largo=len(fecha_apertura)
    while(x<largo):
        
        dt_apertura.append(datetime.strptime(fecha_apertura[x], "%m/%d/%y %H:%M"))
        dt_cierre.append(datetime.strptime(fecha_cierre[x], "%m/%d/%y %H:%M"))
        x+=1



sumaID=[]
def comparacion(dt_apertura,dt_cierre,potencia):
    i=0
    largo=len(potencia)
    while i<largo:
        each=[]
        restoFechas=0
        restoSegundos=0
        rangoDiario=0
        

        if dt_apertura[i].date()==dt_cierre[i].date():
            each.append(potencia[i])
            each.append(dt_apertura[i].date())
            restoFechas=dt_cierre[i]-dt_apertura[i]
            restoMinutos=restoFechas.total_seconds()/60
            each.append(restoMinutos)
            sumaID.append(each)    
          
        else:
            rangoDiario=dt_cierre[i] - dt_apertura[i]
            for d in range(rangoDiario.days+1):
                #Para recorte de fecha apertura
                each2=[]
                fecha_minutos=0
                if d==0:
                    each2.append(potencia[i])
                    each2.append(dt_apertura[i].date())
                    
                    fecha_minutos=(timedelta(days=1)-timedelta(hours=dt_apertura[i].hour,minutes=dt_apertura[i].minute)).total_seconds()/60
                    each2.append(fecha_minutos)
                    sumaID.append(each2)  
                
                if d!=0 and d!=len(range(rangoDiario.days)) :
                    each2.append(potencia[i])
                    fecha_origen = dt_apertura[i].date() + timedelta(days=d)
                    each2.append(fecha_origen[d].date())
                    each2.append(1440)
                    sumaID.append(each2)  
                     
                #Para recorte de fecha cierre
                if d==len(range(rangoDiario.days)):
                    each2.append(potencia[i])
                    each2.append(dt_cierre[i].date())
                    
                    fecha_minutos=timedelta(hours=dt_cierre[i].hour,minutes=dt_cierre[i].minute).total_seconds()/60
                    each2.append(fecha_minutos)
                    sumaID.append(each2)  

        i+=1


revisados=[]
def ids_revisados(sumaID):
    
    for contenido in sumaID:
        
        if contenido[0]  not in revisados:
            
            revisados.append(contenido[0])



resultados=[]

def suma_diaria_central(sumaID,revisados):
    cache=[]
    i=0
    fechas_distintas=[]
    fechas_distintas_espejo=[]
    each=[]
    minutos=0
    while i<len(revisados):

        #AGREGA A CACHE TODOS LOS ELEMENTOS CON EL PRIMER ID,EL CACHE VA A IR CAMBIANDO A MEDIDA QE LA VARIABLE I AVANCE
        for cantidad,elemento in enumerate(sumaID):
            
            if revisados[i]==elemento[0]:
                cache.append(elemento)
            
                
             
        #COMPARACION DE ELEMENTOS EN CACHE PARA AGREGARLOS A RESULTADOS,RECORRIENDO UN ID A LA VEZ.
        for puntero in range(len(cache)):
    
                if cache[puntero][1] not in fechas_distintas  :

                    fechas_distintas.append(cache[puntero][1]) 
                    fechas_distintas_espejo.append(cache[puntero][1])
                    
        

        for item in fechas_distintas:
            
            if item in fechas_distintas_espejo:
                for x,recorrido in enumerate(cache):
                    
                    if item == recorrido[1]:
                        minutos+=recorrido[2]
                        
                        
                        
                    
                    
                    if x==len(cache)-1:
                        each.append(cache[0][0])
                        each.append(item)
                        each.append(minutos)
                        resultados.append(each)
                        each=[]
                        minutos=0
                        fechas_distintas_espejo.remove(item) 
                        

                        #ELIMINACION DE ELEMENTOS EN CACHE,OPTIMIZACION PARA QUE EXPONENCIALMENTE EL TIEMPO DEL ALGORITMO MEJORE. 
                        for item in cache:
                            if item in sumaID:
                                sumaID.remove(item)
  
                
                    

        
        cache=[]
        i+=1
        
   



arrayItemsValidos=[]
arrayItemsInvalidos=[]
#1440 son las 24horas del dia en minutos osea 24*60
def verificacionDiaria(resultados):
    
    for resultado in resultados:

        if resultado[2]>1440:
            arrayItemsInvalidos.append(resultado)
        
        else:
            arrayItemsValidos.append(resultado)





seteo(potenciasID,fechaIni,fechaFin)

#Esta funcion permite visualizar la data en el JSON
#lecturaDatos()

#1.CON DATOS DE PRUEBA
#recorte(fecha_inicial,fecha_final)

#2.CON DATOS DE JSON

recorte(fechaIni,fechaFin)


comparacion(dt_apertura,dt_cierre,potenciasID)


ids_revisados(sumaID)

suma_diaria_central(sumaID,revisados)

verificacionDiaria(resultados)


print('\n')
print('Validos: ',arrayItemsValidos)
print('\n')
print('Invalidos: ',arrayItemsInvalidos)

print('\n')
print('CONTENIDO DE SUMAID: ',sumaID)
print('\n')


 


