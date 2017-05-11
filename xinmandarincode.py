# -*- coding: utf-8 -*-

import nltk
import codecs
import re
from nltk.corpus import PlaintextCorpusReader
nltk.data.path = nltk.data.path + ["/home/yiw023"]
##nltk.data.path = nltk.data.path + ["/home/yiw023/roger"]

path = nltk.data.find(r"/xin_nosgml_segmented_tagged.txt")
raw = codecs.open(path, encoding='utf-8')

outfile = codecs.open("xin_data.txt","w","utf-8")


regex = re.compile('[^ ]+#CD\W([^ ]+#M)\W([^ ]+#NN)')

counts = {}

general_classifier = u'\u4e2a#M'

for line in raw:
        a = regex.search(line)
        if a:
                classifier = a.group(1)
                noun = a.group(2)

                if not noun in counts:
                        counts[noun] = {}
                counts[noun][classifier] = counts[noun].get(classifier, 0) + 1

for noun in counts.keys():
        if general_classifier in counts[noun]:
                print >> outfile, noun,
                ##outfile.write(noun) ## an alternative
                for classifier in counts[noun]:
                        print >> outfile, classifier,
                        print >> outfile, counts[noun][classifier],
                print >> outfile
