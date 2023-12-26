# graph = [
#     [3,0,0,0,0,2,0,3,0,0,0,0,0],
#     [0,3,0,2,0,0,0,0,1,0,0,0,2],
#     [0,0,0,0,2,0,0,0,0,3,0,2,0],
#     [0,0,2,0,0,0,1,0,0,0,3,0,0]
# ]

# courses = {
#     0:'IT2001',
#     1:'IT2002',
#     2:'IT2003',
#     3:'IT2004',
#     4:'IT2005',
#     5:'IT2006',
#     6:'IT4001',
#     7:'IT4002',
#     8:'IT4003',
#     9:'IT4004',
#     10:'IT4101',
#     11:'IT4102',
#     12:'IT4103',
# }

graph = [[2,0,1,0,0],
          [0,1,2,0,1],
          [0,0,1,1,1]]

courses = {
    0:'IT2001',
    1:'IT2002',
    2:'IT2003',
    3:'IT2004',
    4:'IT2005'}

tt = []

for row in graph:
    count=0
    # Distinct Count of Teachers:
    for i in row:
        count+=i
    # Traversing through course:
    di = {}
    for i in range(len(row)):
        if row[i]!=0:
            di[i]=row[i]
    # Putting in time-table:
    tempt = []
    for i in di:
        for j in range(di[i]):
            tempt.append(courses[i])
    tt.append(tempt)


for i in tt:
    print(i)
