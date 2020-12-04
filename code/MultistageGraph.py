# index (u) [[v1,c1],[v2,c2]]
# Adjacency list representation of multistage graph
multistage_graph= [[[1,2],[2,2],[3,5]],
                   [[4,4],[5,11]],
                   [[4,9],[5,5],[6,16]],
                   [[6,2]],
                   [[7,18]],
                   [[7,13]],
                   [[7,2]],
                   [[]]
                   ]
n = len(multistage_graph)
distance = [-1] * n
# initialize sink node
distance [n-1] = 0
for i in range (n-2, -1, -1):
    # For examaple, distance (2, 2) =  min {4  + 18, 5 + 13 , 16 + 2}
    distance [i] = min ([ x[1] + distance [x[0]] for x in multistage_graph[i]])
print(distance)
#O(V^2) == > O( |V| + |E|)


