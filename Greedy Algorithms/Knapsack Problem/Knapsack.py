def knapsack_solver(profits, weights, max_weight):
    max_bag = max_weight
    result_list = [0]*len(profits)
    prof_per_weight = list() # store profits by weight
    for i in range(len(profits)):
        val = (profits[i] / weights[i])
        prof_per_weight.insert(i,(i, val))
    prof_per_weight.sort(key= lambda i: i[1], reverse=True) # store initail indexes and sort ib the decreasing order of profits
    #
    while max_bag!=0 and len(prof_per_weight)>0:
        x = prof_per_weight.pop(0) # pop the maximum element
        if max_bag-weights[x[0]]>=0: # check if it can fit completely in the bag
            max_bag -= weights[x[0]] # update bag capacity
            result_list[x[0]] = 1 # update the usage of that object
        else:
            result_list[x[0]] = max_bag/weights[x[0]] # fraction of usable weight
            max_bag -= max_bag
    max_profit = 0
    for i in range(len(profits)):
        max_profit += profits[i]*result_list[i]
    return max_profit
# Time Complexity: O(n log n) [Sorting] + O(n) [list traversals]
# Total Time Complexity: O(n log n)

profits = [10, 5, 15, 7, 6, 18, 3]
weights = [2, 3, 5, 7, 1, 4, 1]
bag_capacity = 15
print(knapsack_solver(profits, weights, bag_capacity))