graph = [[0,0,0,0,0],
		 [0,0,5,10,15],
         [0,5,0,14,15],
         [0,6,18,0,17],
         [0,8,13,14,0]]

source = 1
valueSet = set({4,3,2,1})
valueSet.remove(source)

def findingTSM(i,s,total):
    if s==set():
        return graph[i][source]
    else:
        mini = float('inf')
        for k in s:
            st = s.copy()
            st.remove(k)
            mini = min(mini,graph[i][k]+findingTSM(k,st,total))
        total += mini
        return total
            
	
print("Starting Vertex (",source,"): ",findingTSM(source,valueSet,0))
