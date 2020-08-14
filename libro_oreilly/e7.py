import re
# ESTE COMANDO dir(nombreFuncion) NOS PERMITE SABER QUE METODOS PUEDE USAR ESA FUNCION.

#HELP(nombreFuncion.REPLACE) OR HELP(nombreCadena.REPLACE) NOS DIRA INFO 
#IN CONSOLE PRINTS OUT THE \0 AS x00 that means \xNN HEXADECIMAL ESCAPE NOTATION
S = 'A\0B\0C'  
print(S) 
print(ord('\n'))
#byte with the binary value 10 in ascii
msg='\'path\''
print(msg)

print('spam'.encode('utf8'))      
# Encoded to 4 bytes in UTF-8 in files
print('spam'.encode('utf16'))
     # But encoded to 10 bytes in UTF-16

match=re.match('Hello[ \t]*(.*)world','Hello pythdfdsfd dfdsfsdon world')
print(match.group(1))
#1 sera a lo que esta entremedio del hello world
#0 sera toda la frase en este caso 
match2=re.match('[/:](.*)[/:](.*)[/:](.*)', '/usr/home:lumberjack')
print(match2.group(1))
#EN ESTE CASO HAYA UN / O : Y TMB HAYA CUALQUIER STRING DESPUES LO GUARDA EN UN GRUPO PARA EL MATCH

n120='Naruto capitulo 11 sub esp'
naruto=re.match('(^[N-n]aruto[ \t]*)(.*[ \t]*[0-9][ \t]*)(sub esp|us)',n120)

try:
  print(naruto.group(0))
except:
  print("El nombre de la serie no corresponde a naruto")


# REG EX DOCUMENTATION
# []	A set of characters	"[a-m]"
# \	Signals a special sequence (can also be used to escape special characters)	"\d"	
# .	Any character (except newline character)	"he..o"	
# ^	Starts with	"^hello"	
# $	Ends with	"world$"	
# *	Zero or more occurrences	"aix*"	
# +	One or more occurrences	"aix+"	
# {}	Exactly the specified number of occurrences	"al{2}"	
# |	Either or	"falls|stays"	
# ()	Capture and group

# special secuences
# \A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
# \b	Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"
# r"ain\b"	
# \B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"
# r"ain\B"	
# \d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
# \D	Returns a match where the string DOES NOT contain digits	"\D"	
# \s	Returns a match where the string contains a white space character	"\s"	
# \S	Returns a match where the string DOES NOT contain a white space character	"\S"	
# \w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
# \W	Returns a match where the string DOES NOT contain any word characters	"\W"	
# \Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"

# sets
# [arn]	Returns a match where one of the specified characters (a, r, or n) are present	
# [a-n]	Returns a match for any lower case character, alphabetically between a and n	
# [^arn]	Returns a match for any character EXCEPT a, r, and n	
# [0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
# [0-9]	Returns a match for any digit between 0 and 9	
# [0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
# [a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
# [+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string

# findall() The findall() function returns a list containing all matches.
# search() The search() function searches the string for a match, and returns a Match object if there is a match.
# sub()  The sub() function replaces the matches with the text of your choice:
# split() The split() function returns a list where the string has been split at each match:

# match propeties
# .span() returns a tuple containing the start-, and end positions of the match.
# .string returns the string passed into the function
# .group() returns the part of the string where there was a match
