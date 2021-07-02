#Permite saber los parametros de una llamada
class Callee:
    def __call__(self, *pargs, **kargs): # Intercept instance calls
        print('Called:', pargs, kargs)
varCalle=Callee()
varCalle(1,5,9,s=12,m=122)


class Comparacion:
    data = 'queso'
    def __gt__(self, other): # 3.X and 2.X version
        return len(self.data) > len(other)
    def __lt__(self, other):
        return len(self.data) < len(other)

varComparacion=Comparacion()
print(varComparacion < 'hamburgesa')

class Truth:
    def __bool__(self): return True

varTruth=Truth()
if varTruth: print('yes!')


class Life:
    def __init__(self, name='unknown'):
        print('Hello ' + name)
        self.name = name
    def live(self):
        print(self.name)
    def __del__(self):
        print('Goodbye ' + self.name)


lilo = Life('lilo')
lilo.live()
lilo = 'stich'


#Python y OOP tres grandes conceptos.
# Inheritance
# Encapsulation
# Polymorphism

#Mangling, FOR Pseudoprivate Attributes
#VALID FOR VAR,METHOD,ATRIB INSIDE A CLASS>> __X CONVERTS INTO automatically -> _ClassName__X


#UNBOUND AND BOUND METHOD Objects

#UNBOUND
# object1 = Spam()
# t = Spam.doit   #CLASS.METHOD
# t(object1, 'howdy') #CLASS.METHOD(INSTANCE,ARGUMENT/S)

#BOUND
# object1 = Spam()
# x = object1.doit
# x('hello world') #CLASS.METHOD(ARGUMENT/S) 


class Product:
    def __init__(self, val): # Bound methods
        self.val = val

    #Mangling
    def __method(self, arg):
        return self.val * arg
    def method2(self, arg):
        return self.val - arg
    def method3(self, arg):
        return self.val + arg

pobject = Product(2)
m=[[],[],[]]
actions = [pobject._Product__method,pobject.method2,pobject.method3]
[m[x].append(i(j)) for x,i in enumerate(actions) for j in range(10) ]
print(m)


#factory function, sirve para llamar todo tipo de clases con dif argumentos
def factory(aClass, *pargs, **kargs): # Varargs tuple, dict
    return aClass(*pargs, **kargs) # Call aClass (or apply in 2.X only)

pobject2=factory(Product,2)
print(pobject2.val)