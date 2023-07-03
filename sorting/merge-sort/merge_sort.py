def merge_sort(iterable):
    listLength = len(iterable)
    if listLength == 1:
        return iterable

    midPoint = listLength // 2

    leftList = merge_sort(iterable[:midPoint])
    rightList = merge_sort(iterable[midPoint:])

    return merge(leftList, rightList)

def merge(left, right):
    output = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            output.append(left[i])
            i = i + 1
        else:
            output.append(right[j])
            j = j + 1

    output.extend(left[i:])
    output.extend(right[j:])

    return output