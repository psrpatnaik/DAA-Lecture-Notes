#Graph representation
#[[c1,u1,v1],[c2, u2,v2]]
graph_edges= [[4,0,1],[8,0,7],[11,1,7],[8,1,2],[2,2,8],[4,2,5],[7,2,3],[9,3,4],[14,3,5],[10,4,5],[2,5,6],[1,6,7],[7,7,8],[6,6,8]]
# sorted list of edges in the Graph
graph_edges_sorted= sorted(graph_edges)
# set to hold the graph's and MST's vertices.
graph_vertices=set()
mst_vertices=set()
# to hold the edges which form the Minimum cost spanning tree.
mst_edges=[]
# Populate the graph_vertices from the graph edges
for edge in graph_edges:
    graph_vertices.add(edge[1])
    graph_vertices.add(edge[2])
#print(graph_vertices)
#print(mst_vertices)
#print(graph_vertices == mst_vertices)
# Prim's Algorithm
# initialization, select node 0
mst_vertices.add(0)
while(graph_vertices != mst_vertices):
    for edge in graph_edges_sorted:
        # check if selection of edge forms cycle
        if edge[1] in mst_vertices and edge[2] in mst_vertices:
            continue
        if edge[1] not in mst_vertices and edge[2] not in mst_vertices:
            continue
        mst_vertices.add(edge[1])
        mst_vertices.add(edge[2])
        mst_edges.append(edge)

print("MST edges")
print(mst_edges)
mst_cost=0
for edge in mst_edges:
    mst_cost = mst_cost + edge[0]
print("MST Cost")
print(mst_cost)














