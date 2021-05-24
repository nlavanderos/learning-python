#https://github.com/Mafijec/Fizz-Buzz-Python-Fastest
def fizzBuzz(n):
    l=[]
    for i in range(1,n+1):
        l.append([str(i),"Buzz","Fizz","FizzBuzz"][2*(i%3==0) + (i%5==0)])
    return print(l)

n=15
fizzBuzz(n)

