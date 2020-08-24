
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

def seestacontido(conj1, conj2):
    # Se contem conj1 no conj2
    conferencia = geraintersecao(conj1, conj2)
    if len(conferencia) == len(conj1):
        return True
    else:
        return False

def contemelemento(e,conj1):
    for i in range(0, len(conj1)):
        if conj1[i] == e:
            return True
    return False


c1 = [0,4,2]
c2 = [1,0,4,2]

e = 1

# Elimina repetiçao e ordena
c1 = retirarepeticaoeordena(c1)
c2 = retirarepeticaoeordena(c2)

# Identifica interseção
intersecao = geraintersecao(c1,c2)

# Indentifica conjunto diferença
diferenca_1p2 = geradiferenca(c1,c2)
diferenca_2p1 = geradiferenca(c2,c1)

# Reliza união dos conjuntos
uniao = unir(c1,c2)

# Verifica se um contém o outro
contem_c1emc2 = seestacontido(c1,c2)
contem_c2emc1 = seestacontido(c2,c1)


print(f"Conjunto A sem repetições e ordenado: {c1}")
print(f"Conjunto B  sem repetições e ordenado: {c2}")
print(f"A interseção dos conjuntos é: {intersecao}")
print(f"A diferença de A para B: {diferenca_1p2}")
print(f"A diferença de B para A: {diferenca_2p1}")
print(f"União de A com B: {uniao}")

# Retorna sobre os conjuntos serem iguais ou um conter o outro
if contem_c2emc1 == True and contem_c1emc2 == True:
    print("Os conjuntos A e B são iguais")
else:
    if contem_c2emc1 == True:
        print(f"Conjunto B está contido no conjunto A")
    elif contem_c1emc2 == True:
        print(f"Conjunto A está contido no conjunto B")
    else:
        print(f"Os conjuntos não contêm um ao outro")

# Se há o elemento nos conjuntos
c1ce = contemelemento(e,c1)
c2ce = contemelemento(e,c2)

# Retorna sobre os conjuntos conterem o elemento e
if c1ce == True and c2ce == True:
    print(f"Ambos conjuntos conjuntos têm o elemento {e}")
else:
    if c1ce == True:
        print(f"{e} está presente no conjunto A")
    elif c2ce == True:
        print(f"{e} está presente no conjunto B")
    else:
        print(f"{e} não está presente em nenhum dos conjuntos")
