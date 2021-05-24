def minmax(function, *args):
    res = args[0]
    for arg in args[1:]:
        if function(res, arg):
            res = arg
            
    return res
def lessthan(x, y): return x > y # See also: lambda, eval
def grtrthan(x, y): return x < y
print(minmax(lessthan, 4, 2, 1, 5, 6, 3)) # Self-test code
print(minmax(grtrthan, 4, 2, 1, 5, 6, 3))