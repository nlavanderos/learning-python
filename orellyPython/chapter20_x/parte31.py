#CHAPTER 27 :Class Coding Basics,797

#Python follow PEMDAS for arithmetics,in maths follow BODMAS RULE.
#PEMDAS
#P>PARENTESIS,E>MULTIPLICACION DE EXPONENTE,M>MULTIPLICACION,D>DIVISION,A>ADICION,S>SUSTRACCION
#BODMAS
##B>BRACKETS([],PARENTESIS),O>ORDERS(RAIZ,EXPONENTES),D>DIVISION,M>MULTIPLICACION,A>ADICION,S>SUSTRACCION


class Mage():
    """
    Clase enfocada al combate de mounstros (PVE), cuenta con diversos hechizos.
    """

    def __init__ (self):
        if self.level<15:
            print(f'{self.name} No puedes obtener esta profesion,tienes nivel {self.level}, el requerido es 15')

        else:
            self.skills+=['fireball','stormShadows']
            self.profession='Mage'

    def learnSkill(self,libro):
        """
        Permite aprender una habilidad
        """
        otherSkills=['iceWall','lightningBolt','earthBlow']
        posibles=['yes','si','s']
        eleccion=input(f'Deseas aprender la habilidad : {libro}\nSi/No: ').lower()
        if self.profession=='Mage' and libro in otherSkills and eleccion in posibles:
            self.skills.append(libro)
            print('Habilidad Aprendida')

        else:
            print(f'{self.name} no puedes aprender la habilidad,tienes diferente clase {self.profession}, no es un libro valido o no desea aprender')
        
class Assasin():
    """
    Clase enfocada al combate 1vs1 (PVP), cuenta con alta velocidad de ataque.
    """

    def __init__ (self):
        if self.level<15:
            print(f'{self.name} No puedes obtener esta profesion,tienes nivel {self.level}, el requerido es 15')

        else:
            self.skills+=['riposte','hide']
            self.profession='Assasin'

    def learnSkill(self,libro):
        """
        Permite aprender una habilidad
        """
        otherSkills=['strike','Dash']
        posibles=['yes','si','s']
        eleccion=input(f'Deseas aprender la habilidad : {libro}\nSi/No: ').lower()
        if self.profession=='Assasin' and libro in otherSkills and eleccion in posibles:
            self.skills.append(libro)
            print('Habilidad Aprendida')

        else:
            print(f'{self.name} no puedes aprender la habilidad,tienes diferente clase {self.profession}, no es un libro valido o no desea aprender')


class Cambio(Mage,Assasin):
    """
    Permite el cambio de clases de los personajes, cuantas veces desee.
    """

    def changeClass (self):
        classes=['Mage','Assasin']
        eleccion=input(f'Clases Disponibles : {classes}\nSelecciona una clase: ').capitalize()
        if eleccion in classes:
            eval(eleccion).__init__(self)
        else:
            posibles=['yes','si','s']
            print(f'La clase {eleccion} no existe')
            op=input('Volver al menu de clases? si/no : ')
            if op in posibles:
                self.changeClass()

            
            


class Character(Cambio): 
    """
    Permite la creacion de personaje:
        Forma de uso >>>varObjeto=Character('Zeus')
    Handler de clases:
        >>>varObjeto.changeClass()
    """

    def __init__ (self,name):
        self.name=name
        self.skills=['run','sleep']
        self.level=1
        self.money=0
        self.profession='Runner'
    
    def display (self): 
        """
        Muestra un mensaje con informacion del personaje
        """
        print(f'\nProfesion Actual de {self.name}: {self.profession}, habilidades: {self.skills}, nivel:{self.level}')
    
    def level_up(self):
        self.level+=1

    def prueba(self,m):
        print(f'Hola, acabas de iniciar sesion en servidor {m}{self}')




#Para poder importar el modulo cuando lo necesite, sin necesidad de ejecturar las pruebas que realize abajo de esta linea
#Se requiere el uso de
if __name__ == '__main__':

    #Testing

   


    #Creacion de personaje/instancia de clase a objeto 
    x=Character('Setxh')

    #Con getattr obtengo un metodo especificado de la instancia del objeto x
    #Donde en variable hola posteriomente, podre definir un mensaje.
    hola=getattr(x,'prueba')
    hola('Zeus')

    #Muestra  las nombres de referencia a la superclase, de determinada clase.En forma de tupla
    print(Cambio.__bases__)

    #Nombre de la clase otorgada al objeto del objeto
    print(x.__class__)


    #Muestra un mensaje con principales caracteristicas del personaje
    x.display()
    #Cada llamada al metodo level up permite al personaje subir un nivel, en este caso 15 niveles para satisfacer el cambio de clase
    #siendo este level aunque el requerido es 15
    [x.level_up() for l in range(15)]
    x.display()
    #Cambio de clase
    x.changeClass()
    x.display()
    #Atravez de este metodo podemos asignar una habilidad a un personaje
    x.learnSkill('iceWall')
    x.display()


    #class rec: pass
    #clases basadas en records, sirven para hacer codigo secuencial.Sin la necesidad de definir los self en cada clase.
    #por otro lado rec.name='LK' tambien funcionaria, pero cada vez seria reemplazado
    # var1=rec()
    # var2=rec()
    # var1.name='bob'
    # var2.name='yui'
    # print(var1,var2)