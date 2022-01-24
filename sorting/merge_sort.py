def merge(array, start, middle, end):
    """
    Merge two sorted lists,
    counts and returns the inversions within two lists as well
    """
    count = 0

    # make sub arrays
    sub1 = array[start:middle + 1].copy()
    sub2 = array[middle + 1:end + 1].copy()

    # give infinity at each end
    sub1.append(float('inf'))
    sub2.append(float('inf'))

    i = 0
    j = 0

    for k in range(start, end + 1):
        if sub1[i] <= sub2[j]:
            array[k] = sub1[i]
            i += 1
            count += j
        else:
            array[k] = sub2[j]
            j += 1

    return count


def merge_sort(array, start, end):
    """
    Sorts the array and returns the number of inversions
    """

    if end > start:
        # divide
        middle = int((start + end) / 2)

        # conquer
        a = merge_sort(array, start, middle)
        b = merge_sort(array, middle + 1, end)

        # combine
        count = merge(array, start, middle, end)

        return a + b + count
    else:
        return 0


def test_number_of_inversions(array):
    """
    @return: the number of inversions in an array
    """
    array = array.copy()
    count = 0
    while len(array) > 0:
        item = array.pop(0)
        for another_item in array:
            if another_item < item:
                count += 1

    return count


if __name__ == '__main__':
    array = [9, 33, 3, 9, 2, 4, 2, 3, 1, 5, 4]
    actual_count = test_number_of_inversions(array)
    count = merge_sort(array, 0, len(array) - 1)
    print("actual count:", actual_count)
    print("result count:", count)
    print(array)
