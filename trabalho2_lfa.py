GLC = [
    ['<S>', '<S>yx', '<B>z', '<C><A>w', '<A><B>'],
    ['<A>', 'a<C><B>', '<B>yb', 'b<C>'],
    ['<B>', 'c<A>d', '<B>yd', 'a<B>', '&'],
    ['<C>', 'z<B>d', 'w<C>c', '<A><B>y','&']
]


estados_e_firsts = {}
firsts = []

def atualiza_firsts(estado, estado_origem):
	for i in estados_e_firsts[estado_origem]:
		


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

for regra in GLC:
	linha = []
	for producao in regra[1:]:
		if producao[0] == '<':
			# atualizar a lista de item do estado
			atualiza_firsts(regra[0] ,producao[0:3])
			print ""
			#linha.append(estados_e_firsts[producao[0:3]])

	#estados_e_firsts.update({regra[0]: linha})

print estados_e_firsts	