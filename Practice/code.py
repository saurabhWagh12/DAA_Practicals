def kadanes_algorithm(arr):
    max_so_far = float("-inf")
    max_ending_here = 0
    start = 0
    end = 0
    s = 0
    
    for i in range(len(arr)):
        max_ending_here += arr[i]
        
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            start = s
            end = i
        
        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1

    return max_so_far, start, end


# li = [5,-3,9,12,-8,7,11,-9,1,-2,4,6]
li = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
print(kadanes_algorithm(li))