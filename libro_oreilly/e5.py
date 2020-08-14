"""
Ejercicio numero 5
"""
import math as mt
import random as rd
A = mt.pi
B = mt.sqrt(2)
#random point float 0.0 to 1
C = rd.random()
F = rd.uniform(2.6, 4)
D = rd.choice([1, 2, 3, 4])
G = rd.randrange(10)
print(A, B, C, D, F, G, len(str(A)), sep='\n')


#LEN MARCA EL NUMERO DE ELEMENTOS,ENTONCES EL 0 PASA A HACER 1....
# PARA ENCONTRAR EL ULTIMO ELEMENTO SERI S[LEN(S)-1] SIENDO S UN STRING

V = 'estonoesunacanciondeamor'
V = 'f'+V[1:]

L = list(V)
ST = ''
L[0] = ''.join('E')
for cc in L:
    ST += cc

print(ST)

LIK = bytearray(b'spam')
LIK.extend(b'eggs')
print(LIK)
DEC = LIK.decode()
print(DEC)

JU = 'Dededo'
print(JU.find('De'))
JU = JU.replace('de', 'Du').upper()

#if all are alphabetical is true
print(JU, JU.isalpha())

LIN = 'aaa,bbb,ccc,ddd\n'
LIN = LIN.rstrip().split(',')
print(LIN)


#Camel Case: Second and subsequent words are capitalized,
#to make word boundaries easier to see.
#(Presumably, it struck someone at some point that the capital letters strewn
#   throughout the variable name vaguely resemble camel humps.)
# Example: numberOfCollegeGraduates
# Pascal Case: Identical to Camel Case, except the first word is also capitalized.
# Example: NumberOfCollegeGraduates
# Snake Case: Words are separated by underscores.
# Example: number_of_college_graduates

# Snake Case should be used for functions and variable names.
# Pascal Case should be used for class names. (PEP 8 refers to this as the “CapWords” convention.)
