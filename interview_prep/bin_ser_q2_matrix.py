def search_matrix(matrix, target):
    row, col = len(matrix), len(matrix[0])
    first, last = 0, row - 1

    while first <= last:
        row = (first + last) // 2
        if target > matrix[row][-1]:
            first = row + 1
        elif target < matrix[row][0]:
            last = row - 1
        else:
            break

    if not (first <= last):
        return False

    s, e = 0, col - 1

    while s <= e:
        mid = (s + e) // 2
        if target > matrix[row][mid]:
            s = mid + 1
        elif target < matrix[row][mid]:
            e = mid - 1
        else:
            return True

    return False
