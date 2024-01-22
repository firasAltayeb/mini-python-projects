#
# Complete the 'minimumSwaps' function below.
#
# Returns minimum number of swaps to sort the array
#

def minimum_swaps(arr):
    ref_arr = sorted(arr)
    print(f'ref_arr is {ref_arr}')
    index_dict = {v: i for i, v in enumerate(arr)}
    swaps = 0
    print(f'initial arr: {arr}')
    print(f'initial index_dict: {index_dict}')
    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_idx = index_dict[correct_value]
            arr[to_swap_idx], arr[i] = arr[i], arr[to_swap_idx]
            print(f'arr: {arr}')
            index_dict[v] = to_swap_idx
            index_dict[correct_value] = i
            print(f'index_dict: {index_dict}')
            swaps += 1

    return swaps


if __name__ == '__main__':
    # arr = list(map(int, input().rstrip().split()))
    arr = [4, 3, 1, 2]

    result = minimum_swaps(arr)

    print(result)
