#!/usr/bin/python

# BeautifulSoup is required - install it using easy_install or pip
from BeautifulSoup import BeautifulSoup


################################## Parse file ##################################
xml_string  = open('books.xml').read()
xml         = BeautifulSoup(xml_string)

############################# Document properties ##############################
print type(xml)         # <class 'BeautifulSoup.BeautifulSoup'>
print xml.name          # [document]

########################### Root node (the catalog) ############################
# Equivalent statements
root = xml.findChild("catalog")
root = xml.catalog
print root.name         # "catalog"

#################################### Books #####################################
books = root.findAll(name="book")
print [tag.name  for tag in books]  # [u'book', u'book', u'book', u'book', u'book']
print [tag.text  for tag in books]  # All the text between "<book>" and "</book>", we probably don't want this
                                    # [u"Gambardella, MatthewXML Developer's GuideComputer44.952000-10-01An in-depth look at creating applications \n      with XML.", u'Ralls, KimMidnight RainFantasy5.952000-12-16A former architect battles corporate zombies, \n      an evil sorceress, and her own childhood to become queen \n      of the world.', u'Corets, EvaMaeve AscendantFantasy5.952000-11-17After the collapse of a nanotechnology \n      society in England, the young survivors lay the \n      foundation for a new society.', u"Corets, EvaOberon's LegacyFantasy5.952001-03-10In post-apocalypse England, the mysterious \n      agent known only as Oberon helps to create a new life \n      for the inhabitants of London. Sequel to Maeve \n      Ascendant.", u"Corets, EvaThe Sundered GrailFantasy5.952001-09-10The two daughters of Maeve, half-sisters, \n      battle one another for control of England. Sequel to \n      Oberon's Legacy."]
print [tag.attrs for tag in books]  # [[(u'id', u'bk101')], [(u'id', u'bk102')], [(u'id', u'bk103')], [(u'id', u'bk104')], [(u'id', u'bk105')]]

######################## Book titles (all 'title' tags) ########################
titles = root.findAll(name="title")
print [tag.name for tag in titles]  # [u'title', u'title', u'title', u'title', u'title']
print [tag.text for tag in titles]  # [u"XML Developer's Guide", u'Midnight Rain', u'Maeve Ascendant', u"Oberon's Legacy", u'The Sundered Grail']

