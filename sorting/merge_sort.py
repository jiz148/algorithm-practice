def merge(array, start, middle, end):

    # make sub arrays
    sub1 = array[start:middle + 1]
    sub2 = array[middle + 1:end + 1]

    # give infinity at each end
    sub1.append(float('inf'))
    sub2.append(float('inf'))

    i = 0
    j = 0

    for k in range(start, end + 1):
        if sub1[i] <= sub2[j]:
            array[k] = sub1[i]
            i += 1
        else:
            array[k] = sub2[j]
            j += 1

def merge_sort(array, start, end):

    if end > start:
        # divide
        middle = int((start + end) / 2)

        # conquer
        merge_sort(array, start, middle)
        merge_sort(array, middle + 1, end)

        # combine
        merge(array, start, middle, end)


if __name__ == '__main__':
    array = [9, 33, 3, 9, 2, 4, 2, 3, 1, 5, 4]
    merge_sort(array, 0, len(array) - 1)

    print(array)
