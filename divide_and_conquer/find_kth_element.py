from random import randrange


def find_kth_element(array, k):
    """
    O(logn)
    @return: kth element of array
    """
    # pick an element randomly
    randi = randrange(len(array))
    rand = array[randi]

    # split O(n)
    left, right = [], []
    for item in array:
        if item <= rand:
            left.append(item)
        else:
            right.append(item)

    if len(left) == k:
        return rand
    if len(left) >= k:
        return find_kth_element(left, k)
    else:
        return find_kth_element(right, k - len(left))


if __name__ == '__main__':
    array = [2, 3, 1, 5, 6, 7, 4]
    print(find_kth_element(array, 4))