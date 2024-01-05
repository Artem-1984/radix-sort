def radix_sort(arr):
    max_digits = max([len(str(x)) for x in arr])
    base = 10
    bins = [[] for x in range(base)]
    for i in range(0, max_digits):
        for x in arr:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        arr = [x for queue in bins for x in queue]
        bins = [[] for x in range(base)]
    return arr
arr1=[17,11,55,32,122,12,34,65,3,44,44]
print(radix_sort(arr1))
