#!/usr/bin/env python

import sys
import string
count=0
words=[]
temp=[]
for line in sys.stdin:
       line = line.strip()
       count = line.count(',')
       if (count >27):
             words=line.split(",")
       else:
             temp_list= line.split(",")
             for each in temp:
               words.append(each)
       if (len(words)>27) and words[0] != "DATE":
             words = words[-5:]
             for word in words:
                   if len(word)>0:
print "%s\t%s"%(word, 1)
