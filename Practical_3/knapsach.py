import time
import matplotlib.pyplot as plt

limit = 850

weight = [7, 0, 30, 22, 80, 94, 11, 81, 70, 64, 59, 18, 0, 36, 3, 8, 15, 42, 9, 0, 42, 47, 52, 32, 26, 48, 55,
6, 29, 84, 2, 4, 18, 56, 7, 29, 93, 44, 71, 3, 86, 66, 31, 65, 0, 79, 20, 65, 52, 13]

profit = [ 360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 670, 892, 600, 38, 48, 147, 78, 256, 63, 17, 120,
164, 432, 35, 92, 110, 22, 42, 50, 323, 514, 28, 87, 73, 78, 15, 26, 78, 210, 36, 85, 189, 274,
43, 33, 10, 19, 389, 276, 312 ]

# limit = 15
# weight = [2,3,5,7,1,4,1]
# profit = [10,5,15,7,6,18,3]

class Knapsack:
    def __init__(self):
        self.w = weight
        self.p = profit
        self.l = limit
        self.arr = []
        self.maxProfit = 0
        for i in range(len(weight)):
            li = []
            li.append(weight[i])
            li.append(profit[i])
            if(weight[i]!=0):
                li.append(profit[i]/weight[i])
            else:
                li.append(profit[i]/1)
            li.append(i)

            self.arr.append(li)
    
    def printList(self):
        print(self.arr,len(self.arr))


    def ByWeight(self):
        self.maxProfit = 0
        sorted_data = sorted(self.arr, key=lambda x: x[0])

        wei = 0
        for i in range(len(weight)):
            if wei<self.l:
                ldash = sorted_data[i]
                # print(ldash)
                if (wei)<=self.l and (wei+ldash[0]<=self.l):
                    self.maxProfit+=ldash[1]
                    wei+=ldash[0]
                    print("Index:",ldash[3],"   Weight:",ldash[0],"   Profit:",ldash[1])
                else :
                    frac = (self.l-wei)/ldash[0]
                    # print("fraction",frac)
                    self.maxProfit += (ldash[1]*frac)
                    wei+=frac*ldash[0]
                    print("Index:",ldash[3],"   Weight:",frac*ldash[0],"   Profit:",ldash[1]*frac)

            else:
                break
        print("\n\nMaximum Profit:",self.maxProfit)          


    def ByProfit(self):
        self.maxProfit = 0
        sorted_data = sorted(self.arr, key=lambda x: x[1], reverse=True)

        wei = 0
        for i in range(len(weight)):
            if wei<self.l:
                ldash = sorted_data[i]
                # print(ldash)
                if (wei)<=self.l and (wei+ldash[0]<=self.l):
                    self.maxProfit+=ldash[1]
                    wei+=ldash[0]
                    print("Index:",ldash[3],"   Weight:",ldash[0],"   Profit:",ldash[1])
                else :
                    frac = (self.l-wei)/ldash[0]
                    # print("fraction",frac)
                    self.maxProfit += (ldash[1]*frac)
                    wei+=frac*ldash[0]
                    print("Index:",ldash[3],"   Weight:",frac*ldash[0],"   Profit:",ldash[1]*frac)

            else:
                break
        print("\n\nMaximum Profit:",self.maxProfit)   
        
    def ByRatio(self):
        self.maxProfit = 0
        sorted_data = sorted(self.arr, key=lambda x: x[2],reverse=True)

        wei = 0
        for i in range(len(weight)):
            if wei<self.l:
                ldash = sorted_data[i]
                # print(ldash)
                if (wei)<=self.l and (wei+ldash[0]<=self.l):
                    self.maxProfit+=ldash[1]
                    wei+=ldash[0]
                    print("Index:",ldash[3],"   Weight:",ldash[0],"   Profit:",ldash[1])
                else :
                    frac = (self.l-wei)/ldash[0]
                    # print("fraction",frac)
                    self.maxProfit += (ldash[1]*frac)
                    wei+=frac*ldash[0]
                    print("Index:",ldash[3],"   Weight:",frac*ldash[0],"   Profit:",ldash[1]*frac)

            else:
                break
        print("\n\nMaximum Profit:",self.maxProfit)
    

    def getResult(self):
        x = []
        start=time.perf_counter()
        k.ByWeight()
        end= time.perf_counter()   
        timetaken=end-start
        x.append(timetaken)
        print("\n\n\n")

        start=time.perf_counter()
        k.ByProfit()
        end= time.perf_counter()   
        timetaken=end-start
        x.append(timetaken)


        print("\n\n\n")
        start=time.perf_counter()
        k.ByRatio()
        end= time.perf_counter()   
        timetaken=end-start
        x.append(timetaken)
        name = ["by Weight","by Profit","by Ratio"]
       

        # Create a horizontal bar chart
        plt.barh(name,x)

        # Adding labels and title
        plt.xlabel('Values')
        plt.ylabel('Items')
        plt.title('Horizontal Bar Chart for a Single List')

        # Display the graph
        plt.show()
                

    
k = Knapsack()
k.getResult()


