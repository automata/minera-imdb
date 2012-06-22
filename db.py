# -*- coding: utf-8 -*-

from imdb import IMDb

ia = IMDb('sql', uri='mysql://root:lm2526@localhost/imdb')
search_sk = ia.search_person(u'Stanley Kubrick')
for person in search_sk:
    print person['name'], person.personID

sk = search_sk[0]
ia.update(sk)
print 'Last directed movie:', sk['director'][0]
