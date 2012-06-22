from __future__ import division
import math

ent_1={'irish':1,'patrick':1,'luz':1,'canada':1,'caixa':1,'NORMA':5}
ent_2={'celular':1,'caixa':1,'pub':1,'duff':1,'luigi':1,'NORMA':5}
ent_3={'lata':1,'torrent':1,'carteira':1,'caixa':0,'mouse':1,'NORMA':4}
#geracao da lista com as igualdaes entre os elementos (ja normalizado)

ALL_SVD=[ent_1,ent_2,ent_3] #lista com todos os dicionarios (como inserir no programa dependera da juncao)
SLH=[] #lista com das igualdades 
count=0 #contador de posicao
for target in ALL_SVD: #laco no alvo
	for neigh in ALL_SVD:#laco no vizinho 
		equal=0 #contador de matchs
		for word_target in [elem for elem in target.keys() if elem!='NORMA']:  #laco em todas as palavras do alvo (exeto NORMA)
			if (neigh.keys()).count(word_target): equal +=target[word_target]*neigh[word_target]#caso ocorra um mach
		SLH.append([count,equal/(math.sqrt(target['NORMA'])*math.sqrt(neigh['NORMA']))])
		count+=1
SLH=sorted(SLH,key=lambda value: value[1],reverse=True) #ordenacao dos elementos em ordem decrescente (reverse=True)
threshold=0.1 #valor de controle de clusterizacao (distancia maxima considerada no algoritimo )
SLH=[elem for elem in SLH if (threshold-elem[1])<0] #definicao de zero
SLH=[elem for elem in SLH if int(elem[0]/len(ALL_SVD))!=int(elem[0]%len(ALL_SVD))] #remocao de elementos identicos (tar=1 nei=1)
#geracao da lista direta e da lista inversa 
Inv_cluster=range(len(ALL_SVD)) #lista inversa do conjunto de cluster
cluster=[] #lista com o conjunto de clusters
for elem in Inv_cluster: #geracao da lista inicial
	cluster.append([elem])
print(cluster)
print(Inv_cluster)
print('\n')
#clusterizacao
for elem in SLH: 
	target=int(elem[0]/len(ALL_SVD))
	neigh=int(elem[0]%len(ALL_SVD))
	if(Inv_cluster[target]!=Inv_cluster[neigh]): #caso em que exista clusters diferentes
		cluster[Inv_cluster[target]].append(neigh) #adicionamos o vizinhos 
		cluster[Inv_cluster[neigh]].remove(neigh) #removemos do cluster antigo
		Inv_cluster[neigh]=Inv_cluster[target] #acertamos as tags
cluster=[elem for elem in cluster if len(elem)>0]
print(cluster)
print(Inv_cluster)
