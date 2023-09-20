
# Name : Saurabh Wagh
# Section : A
# Practical 1 : (DAA)

import pandas as pd
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Divide the list into two halves
        right_half = arr[mid:]

        merge_sort(left_half)  # Recursively sort the left half
        merge_sort(right_half)  # Recursively sort the right half

        # Merge the sorted left and right halves
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def bruteForce(column):
    maximum = float("-inf")
    minimum = float("inf")
    for i in column:
        if maximum<i:
            maximum = i
    for i in column:
        if minimum>i:
            minimum = i
    ldash = []
    ldash.append(maximum)
    ldash.append(minimum)
    return ldash
    
timex = []
timey = []


# Reading CSV file 1:
file_path = "./data500.csv"

df = pd.read_csv(file_path)
column = df['numbers']

# Brute force Approach
print("For first File: \n")
start=time.perf_counter()
l = bruteForce(column)
end= time.perf_counter()   
timetaken=end-start
timex.append(timetaken)

print("Maximum: ",l[0])
print("Minimum: ",l[1])

li = []
for i in column:
    li.append(int(i))

# Divide and conquer:
start=time.perf_counter()
merge_sort(li)
end= time.perf_counter()   
timetaken=end-start
timey.append(timetaken)
print("Maximum after sorting: ",li[len(li)-1])
print("Minimum after sorting: ",li[0],"\n\n")



# Reading CSV file 2:
file_path = "./test1.csv"

df = pd.read_csv(file_path)
column = df['val']

# Brute force Approach
print("For Second File: \n")
start=time.perf_counter()
l = bruteForce(column)
end= time.perf_counter()   
timetaken=end-start
timex.append(timetaken)

print("Maximum: ",l[0])
print("Minimum: ",l[1])

li = []
for i in column:
    li.append(i)

# Divide and conquer:
start=time.perf_counter()
merge_sort(li)
end= time.perf_counter()   
timetaken=end-start
timey.append(timetaken)
print("Maximum after sorting: ",li[len(li)-1])
print("Minimum after sorting: ",li[0],"\n\n")


# Reading CSV file 3:
file_path = "./test4.csv"

df = pd.read_csv(file_path)
column = df['val']
column.fillna(0, inplace=True)

# Brute force Approach
print("For Third File: \n")
start=time.perf_counter()
l = bruteForce(column)
end= time.perf_counter()   
timetaken=end-start
timex.append(timetaken)

print("Maximum: ",l[0])
print("Minimum: ",l[1])

li = []
for i in column:    
    li.append(i)

# Divide and conquer:
start=time.perf_counter()
merge_sort(li)
end= time.perf_counter()   
timetaken=end-start
timey.append(timetaken)
print(max(li),min(li),len(column),len(li),li[len(li)-1])
print("Maximum after sorting: ",li[len(li)-1])
print("Minimum after sorting: ",li[0],"\n\n")


# Reading CSV file 4:
file_path = "./test3.csv"

df = pd.read_csv(file_path)
column = df['val']

# Brute force Approach
print("For Fourth File: \n")
start=time.perf_counter()
l = bruteForce(column)
end= time.perf_counter()   
timetaken=end-start
timex.append(timetaken)

print("Maximum: ",l[0])
print("Minimum: ",l[1])

li = []
for i in column:
    li.append(i)

# Divide and conquer:
start=time.perf_counter()
merge_sort(li)
end= time.perf_counter()   
timetaken=end-start
timey.append(timetaken)
print(max(li),min(li),len(column),len(li),li[len(li)-1])
print("Maximum after sorting: ",li[len(li)-1])
print("Minimum after sorting: ",li[0],"\n\n")

# Reading CSV file 5:
file_path = "./test2.csv"

df = pd.read_csv(file_path)
column = df['fare_amount']

# Brute force Approach
print("For Fifth File: \n")
start=time.perf_counter()
l = bruteForce(column)
end= time.perf_counter()   
timetaken=end-start
timex.append(timetaken)

print("Maximum: ",l[0])
print("Minimum: ",l[1])

li = []
for i in column:
    li.append(i)

# Divide and conquer:
start=time.perf_counter()
merge_sort(li)
end= time.perf_counter()   
timetaken=end-start
timey.append(timetaken)
print(max(li),min(li),len(column),len(li),li[len(li)-1])
print("Maximum after sorting: ",li[len(li)-1])
print("Minimum after sorting: ",li[0],"\n\n")

print(timex,timey)


# Data Plotting for analysis
import matplotlib.pyplot as plt

# Data
data = [
    timex,
    timey
]

# Create the plot
plt.figure(figsize=(10, 6))

plt.plot(data[0], label='Brute Force', marker='o', linestyle='-')

plt.plot(data[1], label='Divide and conquer', marker='x', linestyle='-')

plt.title('Data Analysis Plot')
plt.xlabel('Brute-Force Approach')
plt.ylabel('Divide-and-conquer Approach')
plt.legend() 
plt.grid(True)  

plt.show()  

# Conclusion : Divide and Conquer algorithm is taking much time than Brut force approach and can be analyzed from the graph plotted.