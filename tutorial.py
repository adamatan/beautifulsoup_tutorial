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

root = xml.findChild("catalog")

# "catalog"
print root.name
print root.fetchText()

