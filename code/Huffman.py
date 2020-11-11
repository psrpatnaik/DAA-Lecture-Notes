import heapq
# input
class Node:
    def __init__(self,character, frequency, node_type, left_ptr, right_ptr):
        self.character = character
        self.frequency = frequency
        self.node_type = node_type
        self.left_ptr = left_ptr
        self.right_ptr = right_ptr

    def __lt__(self, other):
        return self.frequency < other.frequency

node_list= []
# sample input 1
# node_list.append(Node("a",10,"leaf", None, None))
# node_list.append(Node("b",4,"leaf", None, None))
# node_list.append(Node("i",1,"leaf", None, None))
# node_list.append(Node("y",12,"leaf", None, None))
# node_list.append(Node("z",2,"leaf", None, None))
# node_list.append(Node("c",6,"leaf", None, None))

# sample input 2
node_list.append(Node("a",45,"leaf",None,None))
node_list.append(Node("b",13,"leaf",None,None))
node_list.append(Node("c",12,"leaf",None,None))
node_list.append(Node("d",16,"leaf",None,None))
node_list.append(Node("e",9,"leaf",None,None))
node_list.append(Node("f",5,"leaf",None,None))

# heapify the node list
heapq.heapify(node_list) #O(n log n)

while(len(node_list) > 1):   # n
    min_node_1= heapq.heappop(node_list)
    min_node_2 = heapq.heappop(node_list)
    internal_node = Node(min_node_1.character+min_node_2.character,
                         min_node_1.frequency + min_node_2.frequency,
                         "internal",
                         min_node_1,
                         min_node_2
                         )
    heapq.heappush(node_list,internal_node)  # log n
#O(n log n)
# output
huffman_codes={}

# inorder traversal of the computed tree
def compute_huffman_codes(node, code_string):
    if (node.node_type != "leaf"):
        compute_huffman_codes(node.left_ptr, code_string + "0")
        compute_huffman_codes(node.right_ptr, code_string + "1")
    else:
        huffman_codes[node.character] = code_string

compute_huffman_codes(node_list[0],"")
print(huffman_codes)

# O(n log n)