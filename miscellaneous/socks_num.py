#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sock_counter(ar):
    socks_dic = {}
    pairs = 0

    for i in ar:
        socks_dic[i] = socks_dic.get(i, 0) + 1

        if socks_dic[i] == 2:
            pairs += 1
            socks_dic[i] = 0

    return pairs


"""
__name__ is a special variable in Python. When a Python script is executed, 
__name__ is set to '__main__' if the script is the main program being run. 
If the script is being imported as a module into another script, 
__name__ is set to the name of the script/module.
"""
if __name__ == '__main__':
    # n = int(input().strip())
    n = 9

    # ar = list(map(int, input().rstrip().split()))
    ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

    result = sock_counter(ar)

    # Expected Output 3
    print(str(result) + '\n')
