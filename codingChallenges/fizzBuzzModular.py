def fizzBuzz(n):
    
    for num in range(1, n+1):
        if num % 15 == 0:
            l.append("FizzBuzz")
        elif num % 3 == 0:
            l.append("Fizz")
        elif num % 5 == 0:
            l.append("Buzz")
        else:
            l.append(num)

if __name__ == '__main__':
    l=[]

    n=int(input())
    fizzBuzz(n)
    print(l)