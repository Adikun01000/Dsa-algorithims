my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def insertionsort(List):
    for i in range(1,len(List)):
        key=i
        Value=List[i]
        for j in range(i-1,-1,-1):
            if List[j]>Value:
                List[j+1]=List[j]
                key=j
            else:
                break
        List[key]=Value
insertionsort(my_array)
print(my_array)