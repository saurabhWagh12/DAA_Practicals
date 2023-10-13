graph = [
		 [0,10,15,20],
         [5,0,9,10],
         [6,13,0,12],
         [8,8,9,0]]

travelset = []

def findPath(source,vertex,graph,travelset):
    if not travelset:
        return graph[vertex][source]
    else:
        if len(travelset) == 1:
            element = 0
            for x in travelset:
                element = x
            travelset.remove(element)
            c = findPath(source,element,graph,travelset)
           
            return graph[vertex][element] + c
        else:
            lenval = []
            for x in travelset:
                travelsetcpy = travelset.copy()
                travelsetcpy.remove(x)
                c= findPath(source,x,graph,travelsetcpy)
                lenval.append((x,graph[vertex][x]+c))
            lenval.sort(key= lambda x:x[1])
            return lenval[0][1]  
cost= findPath(0,3,graph,travelset)
print("cost = ",cost)