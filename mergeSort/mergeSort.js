function mergeSort(arr) {
    if(arr.length <= 1) return arr;

    const mid = Math.floor(arr.length / 2)
    const left = mergeSort(arr.slice(0, mid))
    const right = mergeSort(arr.slice(mid, arr.length))

    let [i, j, r] = [0, 0, 0]
    while (i < left.length && j < right.length) {
        if(left[i] < right[j]) {
            arr[r] = left[i];
            i += 1;
        } else {
            arr[r] = right[j];
            j += 1;
        }
        r += 1
    }

    while (i < left.length) {
       arr[r] = left[i]
       i += 1
       r += 1
    }
    while (j < right.length) {
       arr[r] = right[j]
       j += 1
       r += 1
    }

    return arr
}
