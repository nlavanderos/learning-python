
#TODOS LOS ELEMENTOS DE UNA LISTA DESORDENADA LO DEJA COMO UNA ORDENADA
def get_elements_from_nested_list(l, new_l):
    if l is not None:
        e=l[0]
        if isinstance(e,list):
            get_elements_from_nested_list(e,new_l)
        else:
            new_l.append(e)
        if len(l)>1:
            return get_elements_from_nested_list(l[1:],new_l)
        else:
            return new_l


lista=[1,2,[2,3,3]]
nueLista=[]
get_elements_from_nested_list(lista,nueLista)
print(nueLista)
