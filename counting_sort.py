def countingSort(arr):
    size=len(arr)
    max_val=max(arr)+1
    output=[0]*size
    count=[0]*max_val
    for m in range(0,size):
        count[arr[m]]+=1
    for m in range(1,max_val):
        count[m]+=count[m-1]
    m=size-1
    while m>=0:
        output[count[arr[m]]-1]=arr[m]
        count[arr[m]]-=1
        m-=1
    for m in range(0,size):
        arr[m]=output[m]
data=[2,3,2,5,7,6,1,8]
print("original array:",data)
countingSort(data)
print("Sorted Array:")
print(data)