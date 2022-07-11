#copy the content of one file to another
import os
f1=open('new.py','r')
r=f1.read()
f1.close()
if(os.path.exists('new2.py')):
    print('file already exists')
else:
    f2=open('new2.py','w')
    f2.write(r)
    f2.close()
    print('content of new2.py')
    for i in open('new2.py').read().split("\n"):
        print(i)