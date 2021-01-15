def pivot(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:

        # Move high left
        while low <= high and array[high] >= pivot:
            high -= 1

        # Move low right
        while low <= high and array[low] <= pivot:
            low += 1

        # Check that low less than high
        if low <= high:
            # If so swap values
            array[low], array[high] = array[high], array[low]
        else:
            # Otherwise break loop
            break

    #swapping pivot with high so that pivot is at its right # #position
    array[start], array[high] = array[high], array[start]

    # Return pivot index
    return high


def quick_sort(array, start=None, end=None):
    if start == None or end == None:
        start = 0
        end = len(array) - 1
    if start >= end:
        return

    # Pivot and get pivot index
    pivot_index = pivot(array, start, end)
    # Recurse on left of pivot
    quick_sort(array, start, pivot_index-1)
    # Recurse on right of pivot
    quick_sort(array, pivot_index+1, end)
