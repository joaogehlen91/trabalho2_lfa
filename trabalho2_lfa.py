GLC = [
    ['<S>', '<S>yx', '<B>z', '<C><A>w', '<A><B>'],
    ['<A>', 'a<C><B>', '<B>yb', 'b<C>'],
    ['<B>', 'c<A>d', '<B>yd', 'a<B>', '&'],
    ['<C>', 'z<B>d', 'w<C>c', '<A><B>y','&']
]

#GLC = [
#    ['<S>', 'a<B>c', 'bc', '<B><C>d', 'a'],
#    ['<B>', 'b<D>', 'b<C>', '&'],
#    ['<C>', 'a<C>', '<B>d', '<D>c', '&'],
#    ['<D>', '<B><C>', 'cd', 'ac', '<C>e']
#]


estados_e_firsts = {}

#prepara dicionario
for regra in GLC:
	for estado in regra[0:1]:
		estados_e_firsts.update({estado: ''})


def firsts_indiretos(producao, i=0, j=3):
	producao_original = producao
	estado = producao[i:j]
	
	if estado:
		if estado[i] == '<':
			i += 3
			j += 3
			return estados_e_firsts[estado] + firsts_indiretos(producao_original[i:])
	
	return []


def first(producao, i=0, j=3):
	estado = producao[i:j]
	if estado == '':
		return []
	if estado[0] != '<':
		return list(estado[0])

	if '&' in estados_e_firsts[estado]:
		i += 3
		j += 3
		return [] + first(producao[i:])
	else:
		return estados_e_firsts[estado]


def segundo_passo(estado, producao_origem):
	sem_epslon = [x for x in firsts_indiretos(producao_origem) if x != '&']
	estados_e_firsts[estado] = estados_e_firsts[estado] + sem_epslon


def terceiro_passo(estado, producao):
	retorno = first(producao)
	if not retorno:
		retorno = ['&']
	estados_e_firsts[estado] = estados_e_firsts[estado] + retorno



def execute():
	#segundo passo do first, inclui os firsts indiretos, menos o epslon
	for regra in GLC:
		for producao in regra[1:]:
			if producao[0] == '<':
				#segundo_passo(regra[0], producao[0:3])
				segundo_passo(regra[0], producao)

	#terceiro passo do first
	for regra in GLC:
		for producao in regra[1:]:
			if producao[0] == '<':
				terceiro_passo(regra[0], producao)
    

def calcula_tamanho():
	acum = 0
	for i in estados_e_firsts:
		acum += len(set(estados_e_firsts[i]))
	return acum


#primeiro passo do first, inclui somente os firsts terminais
for regra in GLC:
	linha = []
	for producao in regra[1:]:
		if producao[0] != '<':
			linha.append(producao[0])
	estados_e_firsts.update({regra[0]: linha})


# falta ajustar o tamanho, executar ate nao mudar mais o tamanho
tamanho_ant = 0
execute()
tamanho = calcula_tamanho()

while tamanho_ant != tamanho:
	tamanho_ant = tamanho
	execute()
	tamanho = calcula_tamanho()
	

print("First: ")
for i in estados_e_firsts:
	print(i), set(estados_e_firsts[i])
print("")
