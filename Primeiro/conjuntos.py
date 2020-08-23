
def retirarepeticoes(conj1):
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
    conj1.append(conj2)


c1 = [1,1,1,1,1,6,2,3,4]
c2 = [1,2,1,1]

c1sr = retirarepeticoes(c1)
c2sr = retirarepeticoes(c2)

intersecao = geraintersecao(c1sr,c2sr)
diferenca_1p2 = geradiferenca(c1,c2)
diferenca_2p1 = geradiferenca(c2,c1)

print("A interseção dos conjuntos é: ",intersecao,"\n")
print("A diferença de A para B: ",diferenca_1p2,"\n")
print("A diferença de B para A: ",diferenca_2p1,"\n")

