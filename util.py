def mesesUnicos(lista):
    for y in range(len(lista)):
        x = 0
        c = x + 1
        while c < (len(lista)):
            if lista[x].data_venda.month == lista[c].data_venda.month and lista[x].data_venda.year == lista[c].data_venda.year:
                lista.remove(lista[x])
            c += 1
        x += 1
    return lista

def gerarDict(listaKeys, listaValues):
    dic = {}
    for x in listaKeys:
        dic[x.data_venda.month, x.data_venda.year] = []
    for y in listaValues:
        if (y.data_venda.month, y.data_venda.year) in dic:
            dic[y.data_venda.month, y.data_venda.year].append(y)
    return dic

def toTuple(string):
    for x in string:
        if x == '(' or x == ')':
            string = string.replace(x, '')
    aux = tuple(map(int, string.split(', ')))
    return aux