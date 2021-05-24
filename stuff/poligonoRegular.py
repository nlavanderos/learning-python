import math
def calculoSuperficiePoligonoRegular(lado,numeroLados):
    anguloCentral=360/numeroLados
    apotema=lado/(2*math.tan(math.radians(anguloCentral/2)))
    perimetro=lado*numeroLados
    return ((perimetro*apotema)/2)/10**4


print(calculoSuperficiePoligonoRegular(3.1,6))