#METODOS DE SOBRECARGA MAS USADOS

# __init__ Constructor Object creation: X = Class(args)
# __del__ Destructor Object reclamation of X
# __add__ Operator + X + Y, X += Y if no __iadd__
# __or__ Operator | (bitwise OR) X | Y, X |= Y if no __ior__
# __repr__, __str__ Printing, conversions print(X), repr(X), str(X)
# __call__ Function calls X(*args, **kargs)
# __getattr__ Attribute fetch X.undefined
# __setattr__ Attribute assignment X.any = value
# __delattr__ Attribute deletion del X.any
# __getattribute__ Attribute fetch X.any
# __getitem__ Indexing, slicing, iteration X[key], X[i:j], for loops and other iterations if no
# __iter__
# __setitem__ Index and slice assignment X[key] = value, X[i:j] = iterable
# __delitem__ Index and slice deletion del X[key], del X[i:j]
# __len__ Length len(X), truth tests if no __bool__
# __bool__ Boolean tests bool(X), truth tests (named __nonzero__ in 2.X)
# __lt__, __gt__, Comparisons X < Y, X > Y, X <= Y, X >= Y, X == Y, X != Y(or else __cmp__ in 2.X only)
# __le__, __ge__,
# __eq__, __ne__ 
# __radd__ Right-side operators Other + X, NON INSTANCE + INSTANCE
# __iadd__ In-place augmented operators X += Y (or else __add__)
# __iter__, __next__ Iteration contexts I=iter(X), next(I); for loops, in if no __contains__, all comprehensions, map(F,X), others (__next__ is named next in 2.X)
# __contains__ Membership test item in X (any iterable)
# __index__ Integer value hex(X), bin(X), oct(X), O[X], O[X:] (replaces 2.X __oct__, __hex__)
# __enter__, __exit__  Context manager (Chapter 34) with obj as var:
# __get__, __set__, # Descriptor attributes (Chapter 38) X.attr, X.attr = value, del X.attr
# __delete__
# __new__ Creation (Chapter 40) Object creation, before __init__

class Number:
    def __init__(self, start): 
        self.data = start
    def __sub__ (self, other): 
        return Number(self.data + other)


class Indexer:
    def __getitem__(self, index):
        if isinstance(index, int): # Test usage mode
            print('indexing', index)
        else:
            print('slicing', index.start, index.stop, index.step)


class Index:
    def __index__(self):
        return 1


class StepperIndex:

    def __init__(self,data):
        self.data=data

    #permite alterar lo que le solicitamos en el get del elemento, X[0+1]>>>X[1]
    def __getitem__(self, i):
        return self.data[i+1]


class Accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            #Nueva forma 3.x
            object.__setattr__(self, attr, value + 10)
            #self.__dict__[attr] = value + 10 # Not self.name=val or setattr
            #Imprime el diccionario creado 
            print(self.__dict__)
        else:
            raise AttributeError(attr + ' not allowed')


#Para customizar el error
class PrivateExc(Exception): pass # More on exceptions in Part VII
class Privacy:
    def __setattr__(self, attrname, value): # On self.attrname = value
        if attrname in self.privates:
            #Usualmente se usa AttributeError
            raise PrivateExc(attrname+' es un atributo privado', self) # Make, raise user-define except
        else:
            self.__dict__[attrname] = value # Avoid loops by using dict key


#Atributo privado age, en Test1
class Test1(Privacy):
    privates = ['age']


#Atributo privado name-pay, en Test2
class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

class addboth():
    
    def __init__(self,data):
        self.data=data

    def __add__(self, other):
        self.data += other
    def __str__(self):
        return '[Value: %s]' % self.data # User-friendly string
    def __repr__(self):
        return 'addboth(%s)' % self.data


if __name__ == '__main__' :

    #FUNCTION NUMBER
    varNumber=Number(5)
    #El simbolo -, representa el metodo sobrecarga __sub__
    #varNumber.__sub__(2)
    varNumber2=varNumber-2
    print(varNumber2.data)

    #FUNCTION INDEXER
    varIndexer = Indexer()
    varIndexer[0:50:2]


    #FUNCTION INDEX
    varIndex=Index()
    print([1,2,3][varIndex])
    print(hex(varIndex))

    #FUNCTION STEPPERINDEX
    X = StepperIndex("Spam") # X is a StepperIndex object 
    print(X[0])

    #FUNCTION Accesscontrol
    varAccess=Accesscontrol()
    varAccess.age=10
    print(varAccess.age)

    #FUNCTION Test1,Test2
    varTesteo=Test1()
    varTesteo2=Test2()
    varTesteo.name='Mio'
    #varTesteo2.name='Killua'
    print(varTesteo.name)

    #FUNCTION addboth
    varAddBoth=addboth(4)
    varAddBoth+1
    print(repr(varAddBoth))
    print(varAddBoth)