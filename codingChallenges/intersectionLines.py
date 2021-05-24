from shapely.geometry import LineString
from fractions import Fraction
import re
def MathChallenge(strArr):
    d=re.findall('\((.*?,.*?)\)',strArr)
    cleanStr = [eval(i) for i in d]

    primeraLinea = LineString(cleanStr[:2])
    segundaLinea = LineString(cleanStr[2:])
    valores=primeraLinea.intersection(segundaLinea)
    if(primeraLinea.intersects(segundaLinea)==False):
        return 'no intersection'

    else:
    
        if(str(valores.x).split('.')[1]!=str(0) or str(valores.y).split('.')[1]!=str(0) ):
            xy=(Fraction.from_float(valores.x),Fraction.from_float(valores.y))
            return xy
        
        else:
            xy = int(valores.x),int(valores.y)
            return xy
  # code goes here

#input
#["(9,-2)","(-2,9)","(3,4)","(10,11)"]
x="(9,-2),(-2,9),(3,4),(10,11)"
print(MathChallenge(x))




