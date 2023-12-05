# li = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
li = [-2,-5,6,-2,-3,1,5,-6]
# li = [-2,1,-3,4,-1,2,1,-5,4]
import sys
def maxSum(li,l,r):
    if l==r:
        return li[0]
    else:
        mid = (l+r)// 2
        rightSum = maxSum(li,mid+1,r)
        leftSum = maxSum(li,l,mid)
        cum = crossSum(li,l,mid,r)
        return max(rightSum,leftSum,cum)
def crossSum(li,l,mid,r):
    rightSum = -sys.maxsize
    sums = 0
    for x in range(mid,l,-1):
        sums = sums + li[x]
        if sums > rightSum:
            rightSum = sums
    
    leftSum = -sys.maxsize
    sums = 0
    for x in range(mid,r+1):
        sums = sums + li[x]
        if sums > leftSum:
            leftSum = sums
    return max(rightSum,leftSum,(rightSum + leftSum - li[mid]))    

print(maxSum(li,0,len(li)-1))    
