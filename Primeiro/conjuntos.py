
def retirarepeticaoeordena(conj1):
    conj = []
    for i in conj1:
        if i not in conj:
           conj.append(i)
    conj.sort()
    return conj

def geraintersecao(conj1, conj2):
    return [x for x in conj1 if x in conj2]

def geradiferenca(conj1, conj2):
    return [x for x in conj1 if x not in conj2]

def unir(conj1, conj2):
    uniao = []
    for i in conj1:
        if type(i) == list:
            for j in i:
                uniao.append(j)
        else:
            uniao.append(i)
    for i in conj2:
        if type(i) == list:
            for j in i:
                uniao.append(j)
        else:
            uniao.append(i)
    uniao = retirarepeticaoeordena(uniao)
    return uniao


c1 = [441,1,1,1,1,6,2,3,4,0]
c2 = [31,1,2,40,1,10,39,104]

c1 = retirarepeticaoeordena(c1)
c2 = retirarepeticaoeordena(c2)

intersecao = geraintersecao(c1,c2)
diferenca_1p2 = geradiferenca(c1,c2)
diferenca_2p1 = geradiferenca(c2,c1)
uniao = unir(c1,c2)
print(f"Conjunto A sem repetições e ordenado: {c1}")
print(f"Conjunto B  sem repetições e ordenado: {c2}")
print(f"A interseção dos conjuntos é: {intersecao}")
print(f"A diferença de A para B: {diferenca_1p2}")
print(f"A diferença de B para A: {diferenca_2p1}")
print(f"União de A com B: {uniao}")

