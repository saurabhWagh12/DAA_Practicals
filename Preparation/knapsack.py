li = [[10, 2], [5, 3], [15, 5], [7, 7], [6, 1], [18, 4], [3, 1]]
capacity = 15

li = sorted(li, key=lambda x: (x[0] / x[1]), reverse=True)
print(li)

weight = 0
profit = 0
ans = []

for i in range(len(li)):
    if capacity > weight:
        if weight + li[i][1] <= capacity:
            profit += li[i][0]
            weight += li[i][1]
            ans.append(li[i])
        else:
            diff = capacity - weight
            profit += li[i][0] * (diff / li[i][1])
            ans.append([diff,li[i][0] * (diff / li[i][1])])
            weight+=diff


print(profit)
print(ans)
