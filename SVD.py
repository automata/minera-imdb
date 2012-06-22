from __future__ import division
import re
import urllib
import urllib2
import string
from bs4 import BeautifulSoup

SVD=[] #lista com as palavras SVD
keyword=['assassination','holmes'] #definicao da palavra chave a ser procurada
#Gerando a partir do plot do filme
file_plot=open("plot_1.txt","r") #leitura do arquivo de plot
text=''.join(open("plot_1.txt","r").readlines()) #obtencao do texto intiero
file_plot.close()
sentences=re.split(r' *[\.\?!]["\)\]]* *', text) #separacao por sentencas (AINDA DEVE SER FEITO O VERIFICADOR DE ABREVIACOES)
sentences=[elem.lower() for elem in sentences if len(elem)>0] #transformamos em minusculas e removemos sentencas de tamanho nulo 
max_score=[0,0] #lista com o valor das maiores pontuacoes
selected_sentences=['',''] #lista com as sentencas de maior pontuacao
for snt in sentences:
	score=0 
	for word in keyword: score+=snt.count(word) #contagem de ocorrencias (para cada palavra)
	score=(score*score)/(len(keyword))
	if score>max_score[0]:
		max_score[0]=score
		selected_sentences[0]=snt
	else:
		if score>max_score[1]:
			max_score[1]=score
			selected_sentences[1]=snt
for punc in string.punctuation:	selected_sentences=[elem.replace(punc,'') for elem in selected_sentences]  #remocao de pontuacao
SVD.extend(selected_sentences[0].split())
SVD.extend(selected_sentences[1].split())
#Gerando a partir dos backlinks
file_backlink=open("backlinks.txt","r") #leitura do arquivo de plot
for url in file_backlink.readlines(): #laco nas urls dos backlinks
	file_url=urllib.urlopen(url) #abertura do arquivo de url
	soup=BeautifulSoup(file_url) #transformamos o arquivo html em uma arvore (Biblioteca Beaultiful Soup)
	file_url.close() #fechamento do arquivo de url
	text_raw=soup.find_all('p') #pegamos todo texto de um site
	text='' #"anulamos" a string de texto
	for tag in text_raw: #laco na lista criada pela procura
		if tag.string: text+=tag.string#condicao para existir uma string
	sentences=re.split(r' *[\.\?!]["\)\]]* *', text) #separacao por sentencas (AINDA DEVE SER FEITO O VERIFICADOR DE ABREVIACOES)
	sentences=[elem.lower() for elem in sentences if len(elem)>0] #transformamos em minusculas e removemos sentencas de tamanho nulo 
	max_score=[0,0] #lista com o valor das maiores pontuacoes
	selected_sentences=['',''] #lista com as sentencas de maior pontuacao
	for snt in sentences:
		score=0 
		for word in keyword: score+=snt.count(word) #contagem de ocorrencias (para cada palavra)
		score=(score*score)/(len(keyword))
		if score>max_score[0]:
			max_score[0]=score
			selected_sentences[0]=snt
		else:
			if score>max_score[1]:
				max_score[1]=score
				selected_sentences[1]=snt
	for punc in string.punctuation:	selected_sentences=[elem.replace(punc,'') for elem in selected_sentences]  #remocao de pontuacao
	SVD.extend(selected_sentences[0].split())
	SVD.extend(selected_sentences[1].split())
file_backlink.close()
#transformando a lista em um dicionario mais amigavel
SVD_dic={'NORMA':len(SVD)} #a unica entrada em maiusculo do dicionario eo numero total de palavras
for word in SVD: 
	SVD_dic[word]=SVD.count(word)
	filter (lambda a: a != word, SVD) #remocao das palavras iguais da lista
print(SVD_dic)