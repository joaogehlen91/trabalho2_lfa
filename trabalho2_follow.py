"""
GLC = [
    ['<S>', 'a<B>c', 'bc', '<B><C>d', 'a'],
    ['<B>', 'b<D>', 'b<C>', '&'],
    ['<C>', 'a<C>', '<B>d', '<D>c', '&'],
    ['<D>', '<B><C>', 'cd', 'ac', '<C>e']
]

FIRST = {
	'<S>': ['a', 'c', 'b', 'e', 'd'],
	'<C>': ['a', 'c', 'b', 'e', 'd', '&'],
	'<D>': ['a', 'c', 'b', 'e', 'd', '&'],
	'<B>': ['b', '&']
}
"""

GLC = [
    ['<S>', '<S>yx', '<B>z', '<C><A>w', '<A><B>'],
    ['<A>', 'a<C><B>', '<B>yb', 'b<C>'],
    ['<B>', 'c<A>d', '<B>yd', 'a<B>', '&'],
    ['<C>', 'z<B>d', 'w<C>c', '<A><B>y','&']
]

FIRST = {
	'<S>': ['a', 'c', 'b', 'w', 'y', 'z'],
	'<C>': ['a', 'c', 'b', '&', 'w', 'y', 'z'],
	'<A>': ['a', 'y', 'c', 'b'],
	'<B>': ['a', 'y', 'c', '&']
}


estados_e_follows = {}

#prepara dicionario
for regra in GLC:
	for estado in regra[0:1]:
		estados_e_follows.update({estado: []})

estados_e_follows['<S>'] += ['$']


def first_nao_terminal(estado):
	return [x for x in FIRST[estado] if x != '&']



def follow_terminal(producao, estado):
	i = producao.find(estado)
	terminal = []
	try:
		terminal = list(producao[i+3])
	except:
		terminal = []
	
	if '<' in terminal:
		return first_nao_terminal(producao[i+3:(i+3)+3])
	else:
		return terminal

def follow_estado(producao, estado, nome):
	i = producao.find(estado)
	if i+3 == len(producao): #significa que o estado esta no final da producao
		return estados_e_follows[nome]
	return []


#primeiro passo do follow, inclui somente os follows terminais
for estado in estados_e_follows:
	linha = []
	for regra in GLC:
		for producao in regra[1:]:
			if estado in producao:
				terminal = follow_terminal(producao, estado)
				if terminal: 
					linha += terminal
	estados_e_follows[estado] += linha

for i in estados_e_follows:
	print(i), set(estados_e_follows[i])

#segundo passo do follow, pegar os follow do estado que dah nome a regra
for nome in estados_e_follows:
	linha = []
	for regra in GLC:
		for producao in regra[1:]:
			if estado in producao:
				follow = follow_estado(producao, estado, nome)
				if follow: 
					linha += follow
	estados_e_follows[estado] += linha


		
for i in estados_e_follows:
	print(i), set(estados_e_follows[i])

