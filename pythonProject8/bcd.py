'''pos=-1
def search(list,n):

    #for i in list:
       # globals()['pos']=i
        #if i==n:
           # return True
    #else:
       # return False


    i=0
    while i<len(list):
        globals()['pos']=i
        if list[i]==n:
            return True
        i+=1
    else:
        return False



list=[4,7,9,33,29,1]
n=1
if search(list,n):
    print("found",n,"at position",pos+1)
else:
    print("not found")'''

#binary search

pos=-1
def search(num,n):
    l=0
    u=len(num)-1
    while l<=u:
        mid=(l+u)//2
        globals()['pos']=mid
        if num[mid]==n:
            return True
        else:
            if num[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False
num=[2,4,6,8,9,10,5365,756,98,26622,57656]
n=26622
if search(num,n):
    print("found at",pos+1)
else:
    print("not found")
