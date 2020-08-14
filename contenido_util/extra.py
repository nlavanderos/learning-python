import os,sys
'''
https://stackoverflow.com/questions/63260423/python-compare-2-lists-of-dictionnaries
'''
list1 = [
         {'code': '1111', 'description': 'Test'},
         {'code': '2222', 'description': 'Hello World'},
         {'code': '3333', 'description': 'Stack'},
         {'code': '4444', 'description': 'Gozilla'},
        ]

list2 = [
         {'code': '3333', 'description': 'Stack'},
         {'code': '4444', 'description': 'Megatron'},
         {'code': '5555', 'description': 'Winnie the Pooh'}
        ]

#COMPARE 4444 IN BETWEN OF LIST OF DICTIONARIES
#THIS IS FOR ONE ITEM ,THE BEST IS FOR ALL IN A LOOP WITH SEARCH IN INPUT MODE
match = []
encontrado=[]
for objeto_1 in list1:
    for objeto_2 in list2:
         if objeto_1.get('code')==objeto_2.get('code'):
            match.append(objeto_2)
            print('CODE: {} POS:{} INLIST1'.format(objeto_1.get('code'),list2.index(objeto_2)))
         
             

print(match)

