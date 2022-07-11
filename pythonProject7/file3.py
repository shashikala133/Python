#count number of words in the given file
from collections import Counter
def word_count(fname):
    with open (fname) as f:
        return Counter(f.read().split())
print("number of words in the file:",word_count('new.py'))



#count number of lines in a given file
f=open('new.py','r')
i=0
while(f.readline()!=''):
    i+=1
print("no.of lines in the file is:",i)
f.close()