"""
------------------------PROBLEM DESCRIPTION-------------------------------
A shopkeeper has bags of wheat that each have different weights and different
profits.
eg.

Object No       : 1    2   3   4   5   6   7
Profit          : 5    8   7   1   12  3   4
Weights         : 2    7   1   6   4   2   5
Profit/Weight   : -    -   -   -   -   -   -
Max_weight = 60

Constraints:
max_weight > 0
profit[i]  > 0
weight[i]  > 0

Calculate the maximum profit that the shop shopkeeper can make given
maximum weight that can be carried.
--------------------------------------------------------------------------
"""
def calc_profit(profit: list, weight: list, max_weight: int) -> int:
    if len(profit) != len(weight):
        raise ValueError("The length of profit and weight must be same.")
    if max_weight <= 0:
        raise ValueError("max_weight must be greater than zero.")
    if any(p<0 for p in profit):
        raise ValueError("Profit can not be negative.")
    if any(w<0 for w in weight):
        raise ValueError("Weight can not be negative.")

    # creating profit/weight list
    profit_by_weight = [p / w for p, w in zip(profit, weight)]

    # creating a copy of profit_by_weight and sorting
    sorted_profit_by_weight = sorted(profit_by_weight)

    length = len(sorted_profit_by_weight)
    limit = 0
    gain = 0
    i = 0

    while limit <= max_weight and i < length:
        biggest_profit_by_weight = sorted_profit_by_weight[length - 1 - i]
        index = profit_by_weight.index(biggest_profit_by_weight)
        profit_by_weight[index] = -1

        if weight[index] <= max_weight - limit:
            limit += weight[index]
            gain += 1*profit[index]
        else:
            gain += (max_weight - limit)/weight[index] * profit[index]
            break
        i += 1
    return gain

if __name__ == '__main__':
    print(
        "Input profits, weights, and then max_weight (all positive ints) separated by "
        "spaces."
    )

    profit_ = [int(x) for x in input("Input profits separated by spaces: ").split()]
    weight_ = [int(x) for x in input("Input weights separated by spaces: ").split()]
    max_weight_ = int(input("Max weight allowed: "))

    total_gain = calc_profit(profit_, weight_, max_weight_)
    print('Total profit is: ', total_gain)

'''
------------------------OUTPUT BOX----------------------------------------
Input profits, weights, and then max_weight (all positive ints) separated by spaces.
Input profits separated by spaces: 10 9 8
Input weights separated by spaces: 3 4 5
Max weight allowed: 25
Total profit is:  27
-------------------------------------------------------------------------
'''