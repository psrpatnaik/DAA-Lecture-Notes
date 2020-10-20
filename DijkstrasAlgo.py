# graph = {
#     0: [[1, 4], [7, 8]],
#     1: [[0, 4], [7, 11], [2, 8]],
#     2: [[1, 8], [8, 2], [5, 4], [3, 7]],
#     3: [[2, 7], [5, 14], [4, 9]],
#     4: [[3, 9], [5, 10]],
#     5: [[6, 2], [2, 4], [3, 14], [4, 10]],
#     6: [[5, 2], [8, 6], [7, 1]],
#     7: [[6, 1], [8, 7], [0, 8]],
#     8: [[2, 2], [6, 6], [7, 7]]
#  }

graph= {
    0: [[1,2],[2,5],[3,2]],
    1: [[0,2],[2,3],[4,1]],
    2: [[1,3],[0,5],[3,3],[5,1],[7,1],[4,1]],
    3: [[0,2],[2,3],[6,2]],
    4: [[1,1],[2,1],[8,7]],
    5: [[2,1],[6,2],[7,3]],
    6: [[5,2],[3,2]],
    7: [[8,1],[5,3],[2,1]],
    8: [[4,7],[7,1]]
}

def next_unvisited_node(distance):
    unvisited_distances=[[vertex, distance] for vertex, distance in enumerate(distance)
                         if not node_visited[vertex]]
    unvisited_nodes = sorted(unvisited_distances, key=lambda item: item[1])
    return unvisited_nodes[0][0]

distance = [99999] * len(graph)
previous = [-1] * len(graph)
node_visited = [False] * len(graph)
unvisited = list()
for i in range(len(graph)):
    unvisited.append(i)
start_node = 0
distance[start_node] = 0
while(len(unvisited)!=0):
    # logic
    current_node = next_unvisited_node(distance)
    for neighbor in graph[current_node]:
        if (distance[neighbor[0]] > distance[current_node]+ neighbor[1]):
            distance[neighbor[0]] = distance[current_node]+ neighbor[1]
            previous[neighbor[0]] = current_node
    node_visited[current_node] = True
    unvisited.remove(current_node)

print("{:10} {:10} {:10}".format("Nodes", "Distance", "Previous Node"))
for i,j in enumerate(distance):
    print("{:10} {:10} {:10}".format(i, j, previous[i]))
