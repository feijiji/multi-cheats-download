#coding=utf-8
import linecache

file = open(r"1-10000_DONE.txt","r")
linecount=len(file.readlines())

i = 1
strlist = []
str = ''

#格式化列表
for i in range(1,linecount):
    str = linecache.getline(r"1-10000_DONE.txt",i)
    str = str.strip('\n') 
    str = int(str)
    str += 1
    str = "%s"%(str)
    strlist.append(str)
    i+=1

for i in range(1,linecount):
    filename = strlist[i-1]
    file = open(filename,"r")
    filecontent = linecache.getline(filename,12)
    filecontent = filecontent.strip('Location: ') 
    file = open("url_1_10000.txt","ab")
    file.write(filecontent)
file.close()

