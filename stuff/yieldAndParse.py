import argparse
def mame(x):
    for i in range(x): yield i**2



def countdown2(N): # Generator function, recursive
    if N == 0:
        yield 'stop'
    else:
        yield N
    for x in countdown2(N-1): yield x # 3.3+: yield from countdown2(N-1)


# parser = argparse.ArgumentParser(description='Process some integers.')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                   help='an integer for the accumulator')
o=5
x=countdown2(5)
G=iter(x)

# print(parser.parse_args([str(o)]))
for algo in range(1,6):
    print(next(G))