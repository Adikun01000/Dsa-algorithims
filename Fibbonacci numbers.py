#Using recurrsion fibonnacci numbers
print(0)
print(1)
count=2
def reucursionFib(pre1,pre2):
    global count
    if count<=19:
        newfib=int(pre1+pre2)
        print(newfib)
        pre1=pre2
        pre2=newfib
        count+=1
        reucursionFib(pre1,pre2)
    else:
        return




def F(n:int):
    if n<=1:
        return n
    else:
        return( F(n-1)+F(n-2))
    
print(F(19))