graph = [[0,0,0,0,0],
		 [0,0,10,15,20],
         [0,5,0,9,10],
         [0,6,13,0,12],
         [0,8,8,9,0]]

def findingTSM(i,s,total):
    if s==set():
        return graph[i][1]
    else:
        mini = float('inf')
        for k in s:
            st = s.copy()
            st.remove(k)
            mini = min(mini,graph[i][k]+findingTSM(k,st,total))
        total += mini
        return total
            
	
print("Starting Vertex (1):",findingTSM(1,set({2,3,4}),0))