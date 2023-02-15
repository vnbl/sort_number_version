'''
Function to sort list of version number items

items in list must consist of one to three numbers separated by dots

'''

import re

def solution(lista):

    dict_lista = []

    for i in lista:

        elemento = re.findall("[\d+]+", i)
        elemento = [eval(i) for i in elemento]

        try:
            assert(len(elemento) <= 3)
        except:
            raise AttributeError('invalid version number in list')

        #print(len(elemento))
        #print(elemento)

        if len(elemento)==1:
            elemento.append(-1)
        if len(elemento)==2:
            elemento.append(-1)
            
        dict_lista.append(elemento)
    
    for i in range(2,-1,-1):
        sorted_dict = sorted(dict_lista, key = lambda x : x[i])

    for i in range(0,len(sorted_dict)):
        for j in range(0,3):
            try:
                sorted_dict[i].remove(-1)
            except:
                continue

        if len(sorted_dict[i]) == 3:
            sorted_dict[i] = str(sorted_dict[i][0]) + '.' + str(sorted_dict[i][1]) + '.' + str(sorted_dict[i][2])
        elif len(sorted_dict[i]) == 2:
            sorted_dict[i] = str(sorted_dict[i][0]) + '.' + str(sorted_dict[i][1])
        elif len(sorted_dict[i]) == 1:
            sorted_dict[i] = str(sorted_dict[i][0])

    return(sorted_dict)


new_list = solution(['10.8.7', '2.1', '1', '1.0.3', '3.8.1', '1.1.1', '1.100.1'])

print(new_list)




