'''
 USE OF WALRUS OPERATOR
 '''

a = [1, 2, 3, 4]
if (n := len(a)) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

print('{1} tenemos que {0}'.format('hablar', 'hola'))

NUM_FLOAT = 12497822.2657221
print('{:{coma}{punto}2f}'.format(NUM_FLOAT, punto='.', coma=',')
      .replace(',', 'B').replace('.', ',').replace('B', '.'))

print(u'\N{see-no-evil monkey}', '\N{GHOST}')
print(u'\u2713', '\u2714', '\u2716', '\u2717', '\u0001', sep='  ')
print(NUM_FLOAT, 'saltodelinea', sep='\n')
print('\U0001F606', '\U0001F498')#LAST AS GHOST

#https://unicode.org/emoji/charts/full-emoji-list.html#1f47b
