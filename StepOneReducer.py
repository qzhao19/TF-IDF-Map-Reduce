#!/usr/bin/python

#reduce output: <<word, doc_name>,n>

import sys
import time
start = time.time()
cur_word=None
cur_doc_name=None
cur_word_count=0

#input come from standard in
for line in sys.stdin:
    #parse the input to get the key and value
    (key,val)=line.split('\t',1)
    #parse the key to get the word and document name
    (word,doc_name)=key.split(',',1)
    
    if cur_word!=word or cur_doc_name!=doc_name:
        if cur_word and cur_doc_name:
            cur_key=cur_word+','+cur_doc_name
            print('%s\t%s' %(cur_key,cur_word_count))
            cur_word_count=0
        cur_word=word
        cur_doc_name=doc_name
        try:
            cur_word_count+=int(val)
        except:
            continue
cur_key=cur_word+','+cur_doc_name
print('%s\t%s' %(cur_key, cur_word_count))   
end = time.time()
hours, rem = divmod(end-start, 3600)
minutes, seconds = divmod(rem, 60)
print("Step one reducer execution time=", "{:0>2}:{:0>2}:{:05.2f}".format(int(hours),int(minutes),seconds))








