def linear_search(arr, target):
    n=len(arr)
    for i in range(n):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input('enter elements:').split()))
target=int(input('enter target:'))
result=linear_search(arr,target)
if result != -1:
    print(f'found at {result}')
else:
    print('not found')