arr = [8,5,64,56,7,7,8,78,6,5,4]
temp = 0

for i in range(0, len(arr)):
    for j in range (0, len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


print(arr)
