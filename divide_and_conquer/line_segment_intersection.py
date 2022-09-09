"""
Given two sets of points with p1, p2 ...  pn on line y = 0 and q1, q2 ... qn on the line
y = 1. The points are not necessarily ordered. For example, the points on y = 0 might
be ordered from left to right as p4; p2; p5; p1; p6; p3, with n = 6. Similarly, the points on
y = 1 are not necessarily ordered. Design an algorithm of O(n log n) to decide how many
pairs of the line segments piqi intersect.
"""


def line_segments_intersection(l1, l2):
    # sort l2, by l1, O(nlogn)
    _ = merge_sort(l1, l2, 0, len(l1))
    l3 = [0] * len(l2)

    return merge_sort(l2, l3, 0, len(l2))


def merge_sort(l1, l2, start, end):
    """
    merge sort l1 and l2(by l1 index) simultaneously
    return the number of inversions
    """
    # base case
    if start == end - 1:
        return 0
    # divide
    mid = int((start + end) / 2)
    left = merge_sort(l1, l2, start, mid)
    right = merge_sort(l1, l2, mid, end)
    # merge
    merge_n = merge(l1, l2, start, end, mid)
    return left + right + merge_n


def merge(l1, l2, start, end, mid):
    l1_left = l1[start: mid].copy()
    l1_right = l1[mid: end].copy()
    l1_left.append(float('Inf'))
    l1_right.append(float('Inf'))

    l2_left = l2[start: mid].copy()
    l2_right = l2[mid: end].copy()
    i, j, count = 0, 0, 0
    for k in range(start, end):
        if l1_left[i] <= l1_right[j]:
            l1[k] = l1_left[i]
            l2[k] = l2_left[i]
            i += 1
            count += j
        else:
            l1[k] = l1_right[j]
            l2[k] = l2_right[j]
            j += 1
    return count


def test(l1, l2):
    count = 0
    for i in range(len(l1)):
        for j in range(i + 1, len(l1)):
            if (l1[i] < l1[j] and l2[i] > l2[j]) or (l1[i] > l1[j] and l2[i] < l2[j]):
                count += 1
    return count


if __name__ == "__main__":
    l1 = [3, 2, 5, 6, 7, 4, 1]
    l2 = [3, 7, 1, 6, 5, 2, 4]
    print('actual: ', test(l1, l2))
    print('result: ', line_segments_intersection(l1, l2))
