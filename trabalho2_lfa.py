GLC = [
    ['<S>', '<S>yx', '<B>z', '<C><A>w', '<A><B>'],
    ['<A>', 'a<C><B>', '<B>yb', 'b<C>'],
    ['<B>', 'c<A>d', '<B>yd', 'a<B>', '&'],
    ['<C>', 'z<B>d', 'w<C>c', '<A><B>y','&']
]


estados_e_firsts = {}
firsts = []


def segundo_passo(estado, estado_origem):
	sem_epslon = [x for x in estados_e_firsts[estado_origem] if x != '&']
	estados_e_firsts[estado] = estados_e_firsts[estado] + sem_epslon

'''
def terceiro_passo(estado, producao): #<S>, #<A><B>
	print producao[0:3], estados_e_firsts[producao[0:3]]


	n_terminal = False
	if producao[3] == '<':
		n_terminal = True
	
	#while n_terminal:
		#if producao

	#if producao[4] == '<':

	#if '&' in estados_e_firsts[]
'''

def first(producao, i=0, j=3):
	estado = producao[i:j]
	if '&' in estados_e_firsts[estado]:
		i += 3
		j += 3
		return '' + first(producao[i:])
	else:
		if # tem que testar se não é um terminal 
		return estado



''' preparando dicionario'''
for regra in GLC:
	for estado in regra[0:1]:
		estados_e_firsts.update({estado: ''})


''' primeiro passo do first '''
for regra in GLC:
	linha = []
	for producao in regra[1:]:
		if producao[0] != '<':
			linha.append(producao[0])
	estados_e_firsts.update({regra[0]: linha})


''' sgundo passo do first '''
for regra in GLC:
	for producao in regra[1:]:
		if producao[0] == '<':
			segundo_passo(regra[0], producao[0:3])

'''
for regra in GLC:
	for producao in regra[1:]:
		if producao[0] == '<':
			terceiro_passo(regra[0], producao)

'''

print first('<C><A>w')


for i in estados_e_firsts:
	print(i),(estados_e_firsts[i])

