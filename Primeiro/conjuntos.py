
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

def recebeconj(nome):
    conj = []
    while True:
        conj.append(int(input(f'Digite um elemnto do conjunto {nome}: (Apenas inteiros) ')))
        continua = input(f'Digitar novo elemento? [S/N] ')
        if continua in 'Nn':
            break
        # conj.append(elemento)
    print(f'Seu conjunto digitado foi: {conj}\n')
    return conj

def prodcart(conj1, conj2):
    cart = []
    for i in range(len(conj1)):
        for j in range(len(conj2)):
            cart.append(f'<{conj1[i]}, {conj2[j]}>')
        j = 0
    return cart


c1 = recebeconj('A')
c2 = recebeconj('B')

# Variáveis fixas para teste
# c1 = [0,5]
# c2 = [1,2]


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

print(f"Seus conjuntos são:\n  A = {c1}\n  B = {c2}\n")

print(f"Subtrações:\n  A - B = {diferenca_1p2}\n  B - A = {diferenca_2p1} \n")
print(f"Interseção dos conjuntos = {intersecao} \n")
print(f"União dos conjuntos = {uniao} \n")

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

# Produto cartesiano
cartesiano_ab = prodcart(c1,c2)
cartesiano_ba = prodcart(c2,c1)
print(f"\nProduto cartesiano \n  A x B =  {cartesiano_ab} \n  B x A =  {cartesiano_ba}")

# Se há o elemento nos conjuntos
e = (int(input(f'\nInsira número inteiro para buscar nos conjuntos: ')))
c1ce = contemelemento(e,c1)
c2ce = contemelemento(e,c2)


# Retorna sobre os conjuntos conterem o elemento e
if c1ce == True and c2ce == True:
    print(f"\nAmbos conjuntos conjuntos têm o elemento {e}")
else:
    if c1ce == True:
        print(f"{e} está presente no conjunto A")
    elif c2ce == True:
        print(f"{e} está presente no conjunto B")
    else:
        print(f"{e} não está presente em nenhum dos conjuntos")