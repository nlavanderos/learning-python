"""
nameSpaces.py: a module that lists the namespaces of other modules
"""
from __future__ import print_function # 2.X compatibility
seplen = 60
sepchr = '-'
def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)
    count = 0
    for attr in sorted(module.__dict__): 
        print('%02d) %s' % (count, attr), end = ' ')
        if attr.startswith('__'):
            print('<built-in name>')
        else:
            print(getattr(module, attr)) 
        count += 1
    if verbose:
        print(sepline)
        print(module.__name__, 'has %d names' % count)
        print(sepline)
        
if __name__ == '__main__':
    import nameSpaces
    listing(nameSpaces)