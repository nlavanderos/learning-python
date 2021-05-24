import sys

sys.setrecursionlimit(10**6)
def MathChallenge(num,acumulador=0):

  # code goes here
  if num == 0:
        return acumulador
  return MathChallenge(num-1,acumulador+num)

# keep this function call here 
print(MathChallenge(1000))

