
def retirarepeticaoeordena(conj1):
    conj = []
    for i in conj1:
        if type(i) == list:
            for j in i:
                conj.append(j)
        else:
            conj.append(i)
    return list(set(conj))

# def retirarepeticoes(conj1):
#     conj = []
#     for i in conj1:
#         if i not in conj:
#            conj.append(i)
#     conj.sort()
#     return conj

def geraintersecao(conj1, conj2):
    return [x for x in conj1 if x in conj2]

def geradiferenca(conj1, conj2):
    return [x for x in conj1 if x not in conj2]

def unir(conj1, conj2):
    conj = []
    for i in conj1:
        if type(i) == list:
            for j in i:
                conj.append(j)
        else:
            conj.append(i)
    for i in conj2:
        if type(i) == list:
            for j in i:
                conj.append(j)
        else:
            conj.append(i)
    conj = retirarepeticoes(conj)
    return conj


c1 = [441,1,1,1,1,6,2,3,4,0]
c2 = [104,1,2,1,1,40,10,0]

# ordena(c1)
c1sr = retirarepeticaoeordena(c1)
c2sr = retirarepeticaoeordena(c2)

intersecao = geraintersecao(c1sr,c2sr)
diferenca_1p2 = geradiferenca(c1,c2)
diferenca_2p1 = geradiferenca(c2,c1)
uniao = unir(c1,c2)
print("A interseção dos conjuntos é: ",intersecao,"\n")
print("A diferença de A para B: ",diferenca_1p2,"\n")
print("A diferença de B para A: ",diferenca_2p1,"\n")
print("União de A com B: ",uniao,"\n")
print("A normalizado: ",c1sr,"\n")
print("B normalizado: ",c2sr,"\n")
