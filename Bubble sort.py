my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def BubbleSort(List):
    for i in range(len(List)-1):
        for j in range(len(List)-1-i):
            if List[j]>List[j+1]:
                Temp=List[j]
                List[j]=List[j+1]
                List[j+1]=Temp

BubbleSort(my_array)
print(my_array)