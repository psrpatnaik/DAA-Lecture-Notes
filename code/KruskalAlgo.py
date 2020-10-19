# the edge u--c--->v to be represented as [u,v,c]
# |V| O(|V|)
def cycle_detected(forest, edge):
    cycle = False
    for tree in forest:
        if edge[0] in tree and edge[1] in tree:
            cycle = True
            return cycle
    return cycle
# |V| ~ O(|V|)
#{{1,3,4},{5,6,7},{0,9}}
def merge_forest(forest):
    i = 0
    while(i < len (forest)-1):
        j = i + 1
        while (j < len(forest)):
            if (len(forest[i].intersection(forest[j])) > 0):
                merged_tree = forest[i].union(forest[j])
                treeA = forest[i]
                treeB = forest[j]
                forest.remove(treeA)
                forest.remove(treeB)
                forest.append(merged_tree)
                i = 0
                j = i + 1
                continue
            j+=1
        i+=1

# graph_edges = [
#         [0, 1, 4], [0, 7, 8], [1, 2, 8], [1, 7, 11],
#         [2, 3, 7], [2, 8, 2], [2, 5, 4], [3, 4, 9],
#         [3, 5, 14], [4, 5, 10], [5, 6, 2], [6, 8, 6],
#         [6, 7, 1], [7, 8, 7]
#     ]

graph_edges=[
             [1,2,5], [1,3,2], [2,4,3], [2,3,2],
             [2,5,7], [3,4,3], [3,7,9], [4,5,2],
             [4,7,6], [5,6,8], [6,9,4], [5,8,7],
             [5,7,5], [7,8,2], [6,8,3]
      ]

graph_vertices = set()
tree_edges = []
tree_vertices = set()
# in Kruskal there is formation of forest which eventually merges to a single tree
forest = []
# generate set of vertices for the graph
for edge in graph_edges:
    graph_vertices.add(edge[0])
    graph_vertices.add(edge[1])
#print(graph_vertices)
sorted_graph_edges = sorted(graph_edges, key = lambda x: x[2])
#print(sorted_graph_edges)

# include first edge
tree_edges.append(sorted_graph_edges[0])
# add the vertices of first edge to the tree
tree_vertices.add(sorted_graph_edges[0][0])
tree_vertices.add(sorted_graph_edges[0][1])
# forest.append(sorted_graph_edges[0]) # we wnat the forest to be list of sets
forest.append({sorted_graph_edges[0][0],sorted_graph_edges[0][1]})
# forest be list of sets
index = 1
# |E| times O(|E|)
while(graph_vertices != tree_vertices or len(forest)!=1):
    #print(index)
    choosen_edge = sorted_graph_edges[index]

    # crucial logic
    if ( not cycle_detected(forest, choosen_edge)):
        forest.append({choosen_edge[0], choosen_edge[1]})
        tree_edges.append(choosen_edge)
        tree_vertices.add(choosen_edge[0])
        tree_vertices.add(choosen_edge[1])
        # See if we can merge the trees in the forest
        merge_forest(forest)
    index += 1

print(tree_edges)

mincost = 0
for edge in tree_edges:
    mincost += edge[2]
print(mincost)

# O|E| times (O|V| + O|V|) =====> O(|E|.|V|)
# If the cycle detection and merging of trees in forest is done in log(n) ~ log |V|
# using a data structure called Union-Find
# O(|E|log|V|) same goes with Prim's Algorithm


