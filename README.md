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

    # Python 2.6+ and some libs
    sudo apt-get install python python-mysqldb

    # IMDb.py
    wget -rc http://prdownloads.sourceforge.net/imdbpy/IMDbPY-4.9.tar.gz
    tar -xvzf IMDbPY-4.9.tar.gz
    cd IMDbPY-4.9/
    sudo python setup.py install

## Downloading the IMDB plain files

We used a local copy of the entire IMDB database (until June 22,
2012). Here are the steps to get your own. The plain files will be
downloaded in your ~/tmp/imdb directory. It is a time consuming
action (around 1.1gb of data), so go take a coffee.

    mkdir -f ~/tmp/imdb
    cd ~/tmp/imdb
    wget -rc ftp://ftp.fu-berlin.de/pub/misc/movies/database/
    mv ftp.fu-berlin.de/pub/misc/movies/database/*.gz ./
    rm -rf ftp.fu-berlin.de

So now we have 1.1gb of .list.gz files.

## Setting up a local SQL database

First of all create a database:

    mysqladmin -u root -p create imdb

Having all the .list.gz files at ~/tmp/imdb, run this script, inside of
IMDb.py directory:

    cd IMDbPY-4.9/bin/
    python imdbpy2sql.py -d ~/tmp/imdb/ -u mysql://root:lm2526@localhost/imdb

This will take a *lot* of time (we spent about 5 hours).

# Using

# Some interesting information

We downloaded 8,2G in 3h 32m 27s (676 KB/s).

And we indexed the entire IMDb plain files data base in 303 min:

    # TIME TOTAL TIME TO INSERT/WRITE DATA : 258min, 17sec (wall) 111min, 21sec (user) 25min, 54sec (system)
    building database indexes (this may take a while)
    # TIME createIndexes() : 21min, 37sec (wall) 0min, 0sec (user) 0min, 0sec (system)
    adding foreign keys (this may take a while)
    # TIME createForeignKeys() : 23min, 7sec (wall) 0min, 0sec (user) 0min, 0sec (system)
    RESTORING imdbIDs values for movies... DONE! (restored 0 entries out of 0)
    # TIME restore movies : 0min, 1sec (wall) 0min, 0sec (user) 0min, 0sec (system)
    RESTORING imdbIDs values for people... DONE! (restored 0 entries out of 0)
    # TIME restore people : 0min, 0sec (wall) 0min, 0sec (user) 0min, 0sec (system)
    RESTORING imdbIDs values for characters... DONE! (restored 0 entries out of 0)
    # TIME restore characters : 0min, 3sec (wall) 0min, 0sec (user) 0min, 0sec (system)
    RESTORING imdbIDs values for companies... DONE! (restored 0 entries out of 0)
    # TIME restore companies : 0min, 1sec (wall) 0min, 0sec (user) 0min, 0sec (system)
    # TIME FINAL : 303min, 6sec (wall) 111min, 21sec (user) 25min, 54sec (system)

Total time: 212 min + 303 min = 515 min = 8.5 h to download and index

More about the attributes available on IMDB plain files database,
please refer to
ftp://ftp.fu-berlin.de/pub/misc/movies/database/tools/movie-database-faq .

# Authors

* Lucas Rodrigues
* Vilson Vieira

IFSC / University of São Paulo / 2012