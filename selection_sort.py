def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i+1, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[i], arr[minimum] = arr[minimum], arr[i]
