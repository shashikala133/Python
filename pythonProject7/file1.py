#read first n lines of a file
def file_read_from_head(fname,nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f,nlines):
            print(line)
file_read_from_head('new.py',3)

#display current directory
import os
print(os.getcwd())

#read a file line by line store it into an array
def file_read(fname):
    content_array=[]
    with open(fname) as f:
        for line in f:
            content_array.append(line)
        print(content_array)
file_read('new.py')


#count frequency of file with given extension
import os
for i in os.listdir():
    if(i.endswith(".py")):
        print(i)

#count the no.of lines in the text file
f=open("new.py",'r')
i=0
while(f.readline()!=''):
    i+=1
print("no.of lines in file is",i)
f.close()
