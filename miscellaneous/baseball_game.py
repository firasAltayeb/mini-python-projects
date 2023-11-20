#
# You are given a list of strings operations, where operations[i] is the
# ith operation you must apply to the record and is one of the following:
#
# Record a new score of x.
# '+' # Record a new score that is the sum of the previous two scores.
# 'D' # Record a new score that is the double of the previous score.
# 'C' # Invalidate the previous score, removing it from the record.

def is_digit(s):
    return s.lstrip('-').isdigit()


def cal_points(operations):
    scores = []

    for ops in operations:
        if is_digit(ops):
            scores.append(int(ops))
        elif len(scores) > 0 and ops == "C":
            scores.pop()
        elif ops == "D":
            temp = scores[-1] * 2
            scores.append(temp)
        elif ops == "+":
            temp = scores[-1] + scores[-2]
            scores.append(temp)
        print(scores)

    return sum(scores)


if __name__ == '__main__':
    s = ["5", "-2", "4", "C", "D", "9", "+", "+"]

    result = cal_points(s)

    # Expected Output YES
    print(result)
