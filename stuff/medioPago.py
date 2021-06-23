# Daniela necesita decidir cómo comprar un refrigerador que cuesta 550.000 de contado 
# o 640.000 a crédito. Ella tiene 490.000 pesos en efectivo.

class Persona():

    def __init__(self,nombre,efectivo=0,credito=0):

        self.nombre=nombre
        self.efectivo=efectivo
        self.credito=credito
    
    def transaccion(self):

        if(self.efectivo==550000):
            return True
        elif(self.credito==640000):
            return True
        else:
            return False

#Class item(),eventualmente para tener un listado de items por id



x=Persona('Daniela',490000)

print(x.nombre,x.efectivo)
print(x.transaccion())