# sort according to finish time:
li = [[1, 4, 'A1', 10]
        ,[3,5 ,'A2', 15]
        ,[0, 6, 'A3', 14]
        ,[5, 7, 'A4', 12]
        ,[3, 9 ,'A5', 20]
        ,[5, 9 ,'A6', 30]
        ,[6, 10, 'A7', 32]
        ,[8, 11, 'A8', 28]
        ,[8, 12 ,'A9', 30]
        ,[2, 14 ,'A10', 40]
        ,[12, 16 ,'A11', 45]]

def BubbleSort(l,idx):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j][idx] > l[j+1][idx]:
                temp = l[j][idx]
                l[j][idx] = l[j+1][idx]
                l[j+1][idx] = temp
    return l 

def ActivitySelection(selected):
    # Sorting on basis of end-time:
    # sorted_data = sorted(li, key=lambda x: x[1])
    sorted_data = BubbleSort(li,1)
    # calculating profit:
    totalProfit = 0
    # Running up first process:
    selected.append(sorted_data[0])
    totalProfit+=sorted_data[0][3]
    prevActivity = sorted_data[0]
    # Remaining processes:
    for i in range(1,len(li)):
        activity = sorted_data[i]
        if activity[0]>=prevActivity[1]:
            selected.append(activity)
            prevActivity = activity
            totalProfit+=activity[3]
    return totalProfit


selected = []

total = ActivitySelection(selected)
print('Start-Time',"\t",'End-Time','\t','Activity','\t','Profit')
for i in selected:
    print(i[0],"\t\t",i[1],'\t\t',i[2],'\t\t',i[3])
print('\n','Maximum profit earned: ',total)


# Graph:
import matplotlib.pyplot as plt
import numpy as np

fig2, ax2 = plt.subplots()
ax2.set_yticks(np.arange(len(selected)))
ax2.set_yticklabels([x[2] for x in selected])
for i in range(len(selected)):
    start_Time = selected[i][0]
    end_Time = selected[i][1]
    ax2.barh(i, end_Time-start_Time, left=start_Time, height=0.5, align='center')
ax2.set_xlabel('Timeline')
ax2.set_ylabel('Activities')
ax2.set_title('Gantt Chart')
ax2.grid(True)

plt.show()






