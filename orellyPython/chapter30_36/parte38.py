class tracer:
    def __init__(self, func): 
        self.calls = 0
        self.func = func
    def __call__(self, *args): 
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args)

@tracer #se ejecuta el decorador tracer con la funcion spam pasada como argumento
def spam(a, b, c): #cuando retorna self.func(*args), hace referencia a esta linea el cual retorna spam(1,2,3) en primer instancia
    return a + b + c #finalmente la suma el cual es un valor 6

print(spam(1, 2, 3)) # Really calls the tracer wrapper object
print(spam('a', 'b', 'c')) # Invokes __call__ in class


#META CLASS, valido para todas clases.Donde por default los attr y gattr estaran definidos en meta.
class Meta(type):
    def __new__(cls, name, bases, dct):
        x = super().__new__(cls, name, bases, dct)
        x.attr = 100
        x.gattr = 1010
        return x


class Foo(metaclass=Meta):
    pass

print(Foo.attr,Foo.gattr)
#eventualmente se podra redifinir
Foo.gattr=9
print(Foo.gattr)