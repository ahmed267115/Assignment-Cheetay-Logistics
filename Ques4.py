def candyStoreMin(arr, n, k):
     
    cost = 0
    i = 0
    while(n):
        cost += arr[i]
        n = n-k
        i += 1
    return cost
 
def candyStoreMax(arr, n, k):
 
    cost = 0
    index = 0
    i = n-1
    while(i >= index):
 
        cost += arr[i]

        index += k
        i -= 1
 
    return cost

arr = [3, 2, 1, 4]
n = len(arr)
k = 2 
arr.sort()

print(candyStoreMin(arr, n, k), " ",
      candyStoreMax(arr, n, k))


