#make the libZotero library available
from libZotero import zotero

#create Zotero library object called zlib
zlib=zotero.Library('group','155975','<null>','9GLmvmZ1K1qGAz9QWcdlyf6L')

#retrieve the first five top-level items.
items = zlib.fetchItemsTop({'limit': 5, 'content': 'json,bib,coins'})
