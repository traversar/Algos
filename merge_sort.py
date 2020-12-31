def merge_sort(arr):
    size = len(arr)
    if size > 1:
        middle = size // 2
        left_arr = arr[:middle]
        right_arr = arr[middle:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        r = 0

        left_size = len(left_arr)
        right_size = len(right_arr)
        while i < left_size and j < right_size:
            if left_arr[i] < right_arr[j]:
              arr[r] = left_arr[i]
              i += 1
            else:
                arr[r] = right_arr[j]
                j += 1

            r += 1


        while i < left_size:
            arr[r] = left_arr[i]
            i += 1
            r += 1

        while j < right_size:
            arr[r]=right_arr[j]
            j += 1
            r += 1
