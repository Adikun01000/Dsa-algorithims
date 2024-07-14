my_array = [64, 34, 25, 12, 22, 11, 90, 5]

def partition(List,low,high):
    pivot=List[high]
    key=low-1
    for j in range(low,high):
        if List[j]<=pivot:
            key+=1
            List[key],List[j]=List[j],List[key]
    List[key+1],List[high]=List[high],List[key+1]
    return key+1

def quicksort(List,low=0,high=None):
    if high is None:
        high=len(List)-1
    if low<high:
        pivot_index=partition(List,low,high)
        quicksort(List,low,pivot_index-1)
        quicksort(List,pivot_index+1,high)

quicksort(my_array)
print(my_array)