# README

Web mining for IMDB using Complex Network techniques.

# TODO

## Lucas

* Implement SVD DONE!
* Implement Single-liknage IHAC DONE!

## Vilson

* Create a database (SQLite?) DONE!
    * Movie title
    * Genre
    * Director
    * Actors (at least 4, 2 men, 2 women)
    * Plot
    * Keywords
    * Backlinks (> 50 < 200)

# Installing

We are using IMDb.py to download and access all IMDB information
with an OOP model. In this way, we have some dependencies.

## Dependencies

Currently we are covering a Ubuntu GNU/Linux 11.04 system. Install
the following packages:

    # MySQL
    sudo apt-get install mysql-client mysql-server

    # Python 2.6+
    sudo apt-get install python

    # IMDb.py
    wget -rc http://prdownloads.sourceforge.net/imdbpy/IMDbPY-4.9.tar.gz
    tar -xvzf IMDbPY-4.9.tar.gz
    cd IMDbPY-4.9/
    sudo python setup.py install

## Downloading the IMDB plain files

We used a local copy of the entire IMDB database (until June 22,
2012). Here are the steps to get your own. The plain files will be
downloaded in your ~/tmp/imdb directory. It is a time consuming
action, so go take a coffee.

    mkdir -f ~/tmp/imdb
    cd ~/tmp/imdb
    wget -rc ftp://ftp.fu-berlin.de/pub/misc/movies/database/

More about the attributes available on IMDB plain files database,
please refer to
ftp://ftp.fu-berlin.de/pub/misc/movies/database/tools/movie-database-faq .

# Authors

* Lucas Rodrigues
* Vilson Vieira

IFSC / University of São Paulo / 2012