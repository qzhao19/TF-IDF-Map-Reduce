#!/usr/bin/python

#TF map computation
#mapper output: <<word,doc_name>,1>
import sys
from string import punctuation
stop_words=['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but',
            'by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he',
            'her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might',
            'most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says',
            'she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas',
            'us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']

for line in sys.stdin:
    #remove pounctuation and leading and trailing whitespace
    line=line.translate(None, punctuation).strip('\t')
    #split the line into content
    contents=line.split(' ')
    #get document name
    doc_name=contents[0]
    contents.remove(doc_name)
    for content in contents:
        content=content.rstrip()
        if content not in stop_words:
            key=content+','+doc_name
            print('%s\t%s' %(key,1))
    
































