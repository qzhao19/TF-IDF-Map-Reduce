#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip('\n')
    (key, word_count) = line.split('\t', 1)
    (word, doc_name) = key.split(',', 1)
    cur_value = word + "," + word_count
    print ('%s\t%s' % (doc_name, cur_value))
























