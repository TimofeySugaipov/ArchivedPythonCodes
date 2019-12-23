# Candidate number: 14459
# Using Python 3

from collections import deque
from Graph import Graph

# Depth-first search (recursive, as presented in the lecture)
def DFS(G):
        for u in G.V:
                u.color = 'white'
                u.pi = None
        global time
        time = 0
        for u in G.V:
                if u.color == 'white':
                        DFSVisit(G,u)
def DFSVisit(G,u):
        global time
        time += 1
        u.d = time
        u.color = 'gray'
        for v in G.Adj[u.id]:
                if v.color == 'white':
                        v.pi = u
                        DFSVisit(G,v)
        u.color = 'black'
        time += 1
        u.f = time
                        
                

# Display result of DFS
def display(G):
	for v in G.V:
		s = str(v.id) + ": " + str(v.d) + " " + str(v.f)
		print(s)	
		
if __name__ == '__main__':
        
	# Road network example from the lecture
	G = Graph()
	# Create vertices
	for i in range(0,27):
		G.add_node()
	# Create horizontal edges
	G.add_edge_using_ids(0,1)
	G.add_edge_using_ids(1,2)
	G.add_edge_using_ids(2,3)
	G.add_edge_using_ids(3,4)
	G.add_edge_using_ids(4,5)
	G.add_edge_using_ids(6,7)
	G.add_edge_using_ids(7,8)
	G.add_edge_using_ids(9,10)
	G.add_edge_using_ids(10,11)
	G.add_edge_using_ids(11,12)
	G.add_edge_using_ids(13,14)
	G.add_edge_using_ids(14,15)
	G.add_edge_using_ids(16,17)
	G.add_edge_using_ids(18,19)
	G.add_edge_using_ids(19,20)
	G.add_edge_using_ids(21,22)
	G.add_edge_using_ids(22,23)
	G.add_edge_using_ids(24,25)
	# Create vertical edges
	G.add_edge_using_ids(2,6)
	G.add_edge_using_ids(3,7)
	G.add_edge_using_ids(4,8)
	G.add_edge_using_ids(6,9)
	G.add_edge_using_ids(7,10)
	G.add_edge_using_ids(8,11)
	G.add_edge_using_ids(9,13)
	G.add_edge_using_ids(10,14)
	G.add_edge_using_ids(11,15)
	G.add_edge_using_ids(12,16)
	G.add_edge_using_ids(14,18)
	G.add_edge_using_ids(15,19)
	G.add_edge_using_ids(16,20)
	G.add_edge_using_ids(18,21)
	G.add_edge_using_ids(19,22)
	G.add_edge_using_ids(20,23)
	G.add_edge_using_ids(21,24)
	G.add_edge_using_ids(22,25)
	G.add_edge_using_ids(25,26)
	
	print("Road network example from the lecture")
	print("The graph:")
	G.display()
	
	# Uncomment this line once you implemented the algorithm
	DFS(G)
	
	print("Discovery and finishing times:")
	display(G)
	
	print("")
	
	# DFS example from the lecture
	H = Graph()
	for i in range(0,9):
	    H.add_node()
	H.add_directed_edge_using_ids(0,1)
	H.add_directed_edge_using_ids(1,2)
	H.add_directed_edge_using_ids(0,3)
	H.add_directed_edge_using_ids(0,4)
	H.add_directed_edge_using_ids(1,4)
	H.add_directed_edge_using_ids(3,7)
	H.add_directed_edge_using_ids(3,6)
	H.add_directed_edge_using_ids(4,7)
	H.add_directed_edge_using_ids(5,8)
	
	print("DFS example from the lecture")
	print("The graph:")
	H.display()
	
	# Uncomment this line once you implemented the algorithm
	DFS(H)
	
	print("Discovery and finishing times:")
	display(H)	
