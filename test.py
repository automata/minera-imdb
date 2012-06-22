# -*- coding: utf-8 -*-

import imdb

ia = imdb.IMDb()

s_result = ia.search_movie('The Untouchables')

for item in s_result:
    print item['long imdb canonical title'], item.movieID

# Retrieves default information for the first result (a Movie object).
the_unt = s_result[0]
ia.update(the_unt)

# Print some information.
print the_unt['runtime']
print the_unt['rating']
director = the_unt['director'] # get a list of Person objects.

# Get the first item listed as a "goof".
ia.update(the_unt, 'goofs')
print the_unt['goofs'][0]

# The first "trivia" for the first director.
b_depalma = director[0]
ia.update(b_depalma)
print b_depalma['trivia'][0] 
