#!/usr/bin/python

# BeautifulSoup is required - install it using easy_install or pip
from BeautifulSoup import BeautifulSoup


################################## Parse file ##################################
xml_string  = open('books.xml').read()
xml         = BeautifulSoup(xml_string)

############################# Document properties ##############################

# <class 'BeautifulSoup.BeautifulSoup'>
print type(xml)

# [document]
print xml.name

########################### Root node (the catalog) ############################
# Equivalent statements
root = xml.findChild("catalog")
root = xml.catalog

# "catalog"
print root.name

######################## Book titles (all 'title' tags) ########################
titles = root.findAll(name="title")
# [u'title', u'title', u'title', u'title', u'title']
print [tag.name for tag in titles]
# [u"XML Developer's Guide", u'Midnight Rain', u'Maeve Ascendant', u"Oberon's Legacy", u'The Sundered Grail']
print [tag.text for tag in titles]

books = root.findAll(name="book")

# [[(u'id', u'bk101')], [(u'id', u'bk102')], [(u'id', u'bk103')], [(u'id', u'bk104')], [(u'id', u'bk105')]]
print [tag.attrs for tag in books]
