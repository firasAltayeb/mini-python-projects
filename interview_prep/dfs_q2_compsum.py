# Given an array of distinct integers candidates and a target integer target, return a list
# of all unique combinations of candidates where the chosen numbers sum to target. You may
# return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times. Two combinations
# are unique if the frequency of at least one of the chosen numbers is different.

def combination_sum(candidates, target):
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur[:])
            return
        if i >= len(candidates) or total > target:
            return

        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res
