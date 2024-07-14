unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]

def CountingSort(List):
    MaxValue=max(List)#returns the value thats high or returns the value that is iterrable
    count=[0]*(MaxValue+1)

    while len(List)>0:
        num=List.pop(0)
        count[num]+=1

    for i in range(len(count)):
        while count[i]>0:
            List.append(i)
            count[i]-=1
    return List

print(CountingSort(unsortedArr))