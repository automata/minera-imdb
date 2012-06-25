# -*- coding: utf-8 -*-

from imdb import IMDb

im = IMDb('sql', uri='mysql://root:lm2526@localhost/imdb')
#im = IMDb()   # para consultar usando web diretamente

# faz busca por pessoa, se resultado vazio, busca por keyword
# mude a string abaixo para especificar a busca
search_str = 'alfred hitchcock'
results = im.search_person(search_str)
names = [x['name'].lower() for x in results]
if search_str not in names:
    results = im.get_keyword(search_str)
    if results == []:
        other_keywords = im.search_keyword(search_str)
        results = im.get_keyword(other_keywords[0])

if results == []:
    print 'Coloque outra palavra chave'
else:
    # achou uma lista de pessoas, pega só pessoas com mesmo nome
    right_people = [x for x in results if x['name'].lower() == search_str]
    results = []
    for p in right_people:
        im.update(p)
        if 'director' in p.keys():
            results.extend(p['director'])
        if 'producer' in p.keys():
            results.extend(p['producer'])
        if 'producer' in p.keys():
            results.extend(p['producer'])
        if 'biographical movies' in p.keys():
            results.extend(p['biographical movies'])
        if 'writer' in p.keys():
            results.extend(p['writer'])
        if 'actor' in p.keys():
            results.extend(p['actor'])
        if 'editor' in p.keys():
            results.extend(p['editor'])

# temos os filmes todos, agora vamos pegar o plot
[im.update(m) for m in results if type(m) != type(u'str')]

# acessando os plots:
for m in results:
    if type(m) != type(u'str'):
        if m.has_key('plot') > 0:
            print m['title'], m['plot']
