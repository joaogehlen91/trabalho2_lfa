import json

GLC = []
line = []


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

def execute_first():
	""" Segundo passo do first, inclui os firsts indiretos, menos o epslon """
	for regra in GLC:
		for producao in regra[1:]:
			if producao[0] == '<':
				segundo_passo(regra[0], producao)


	""" Terceiro passo do first """
	for regra in GLC:
		for producao in regra[1:]:
			if producao[0] == '<':
				terceiro_passo(regra[0], producao)

def execute_follow():
	for regra in GLC:
		nome_regra = regra[0]
		for producao in regra[1:]:
			if producao[-1] == '>': # se a producao termina com um nao terminal
				copia_follow(nome_regra, producao)

def calcula_tamanho(conjunto):
	acum = 0
	for i in conjunto:
		acum += len(set(conjunto[i]))
	return acum

def follow_terminal(producao, estado):
	i = producao.find(estado)
	terminal = []
	try:
		terminal = list(producao[i+3])
	except:
		terminal = []
	
	if '<' in terminal:
		return [x for x in FIRST[producao[i+3:i+6]] if x != '&']
	else:
		return terminal

def copia_follow(nome_regra, producao):
	estado = producao[-3:] # os tres ultimos
	if estado and estado[-1] == '>':
		estados_e_follows[estado] += estados_e_follows[nome_regra]
		if '&' in FIRST[estado]:
			producao = producao[:-3]  # do inicio, menos os 3 ultimos
			copia_follow(nome_regra, producao)

def escreve_saida(FF, file_saida, name_set):
	file_saida.write('    | ')
	file_saida.write(name_set)
	file_saida.write('\n')
	for i in FF:
		file_saida.write(i)
		file_saida.write(' |')
		for j in FF[i]:
			file_saida.write(' ')
			file_saida.write(j)
			file_saida.write(', ')
		file_saida.write('\n')
	file_saida.write('\n')


GLC_Json = json.load(open('GLC.json'))
file_saida = open('saida.out', 'w')


""" Transforma a entrada em uma lista """
for i in GLC_Json:
	line = []
	line.append(str(i))
	for j in GLC_Json[i]:
		line.append(str(j))
	GLC.append(line)


"""prepara dicionarios"""
estados_e_firsts = {}
for regra in GLC:
	for estado in regra[0:1]:
		estados_e_firsts.update({estado: ''})

estados_e_follows = {}
for regra in GLC:
	for estado in regra[0:1]:
		estados_e_follows.update({estado: []})
estados_e_follows['<S>'] += ['$']


""" primeiro passo do first, inclui somente os firsts terminais """
for regra in GLC:
	linha = []
	for producao in regra[1:]:
		if producao[0] != '<':
			linha.append(producao[0])
	estados_e_firsts.update({regra[0]: linha})


""" Repete o segundo e terceiro passo do first ateh que nao tenha mais mudancas """
tamanho_ant = 0
execute_first()
tamanho = calcula_tamanho(estados_e_firsts)

while tamanho_ant != tamanho:
	tamanho_ant = tamanho
	execute_first()
	tamanho = calcula_tamanho(estados_e_firsts)


""" Organiza conjunto """
for i in estados_e_firsts:
	estados_e_firsts[i] = list(set(estados_e_firsts[i]))

""" Mostra o conjunto first pronto """
escreve_saida(estados_e_firsts, file_saida, 'F I R S T')
print("Conjunto First: ")
for i in estados_e_firsts:
	print(i, estados_e_firsts[i])
print

FIRST = estados_e_firsts

""" Primeiro passo do follow, inclui somente os follows terminais """
for estado in estados_e_follows:
	linha = []
	for regra in GLC:
		for producao in regra[1:]:
			if estado in producao:
				terminal = follow_terminal(producao, estado)
				if terminal: 
					linha += terminal
	estados_e_follows[estado] += linha

tamanho_ant = 0
execute_follow()
tamanho = calcula_tamanho(estados_e_follows)

""" Segundo passo do follow, executa ateh nao tiver mudanca mais """
while tamanho_ant != tamanho:
	tamanho_ant = tamanho
	execute_follow()
	tamanho = calcula_tamanho(estados_e_follows)


""" Organiza conjunto """	
for i in estados_e_follows:
	estados_e_follows[i] = list(set(estados_e_follows[i]))


print("\nConjunto Follow: ")
for i in estados_e_follows:
	print (i, estados_e_follows[i])

escreve_saida(estados_e_follows, file_saida, 'F O L L O W')