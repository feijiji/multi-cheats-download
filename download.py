__author__ = 'Administrator'

import linecache
import urllib2

file = open(r"url_10000_20000.txt","r")
linecount=len(file.readlines())
i = 1
strlist = []
str = ''

for i in range(1,linecount+1):
    str = linecache.getline(r"url_10000_20000.txt",i)
    str = str.strip('\n') 
    strlist.append(str)
    i+=1

for i in range(1,linecount+1):
    url = strlist[i-1]
    print url
    try:
        re = urllib2.Request(url)
        data = urllib2.urlopen(url).read()
        savepath = url[37:-1]
        with open(savepath, 'wb') as f:
            f.write(data)
    except Exception:
    	continue