from collections import deque
#using Python 3

class Node:
    # creates a node
    def __init__(self, i):
        self.id = i
        self.color = "white"
        self.d = 0
        self.f = 0
        self.pi = None

class Graph:
	# creates a graph
	def __init__(self):
	    self.n = 0		# Number of vertices
	    self.V = []		# Vertices
	    self.Adj = []	# Adjacency list
	
	# add a node
	def add_node(self):
		node = Node(self.n)
		self.n = self.n+1
		self.V.append(node)
		self.Adj.append(deque())
		return node
		
	# get node with id
	def get_node(self, vid):
		node = None
		for v in self.V:
			if v.id == vid:
				node = v
				break
		return node
	
	# add an undirected edge
	def add_edge(self, u, v):
		self.Adj[u.id].append(v)
		self.Adj[v.id].append(u)
			
	# add an undirected edge using ids
	def add_edge_using_ids(self, uid, vid):
		node_u = self.get_node(uid)
		node_v = self.get_node(vid)
		self.add_edge(node_u,node_v)
		
	# add a directed edge
	def add_directed_edge(self, u, v):
		self.Adj[u.id].append(v)
		
	# add a directed edge using ids
	def add_directed_edge_using_ids(self, uid, vid):
		node_u = self.get_node(uid)
		node_v = self.get_node(vid)
		self.add_directed_edge(node_u,node_v)
	
	# display info about nodes	
	def display_nodes(self):
		print("id color d f pi:")
		for v in self.V:
			if v.pi == None:
				print(v.id, v.color, v.d, v.f, "None")
			else:
				print(v.id, v.color, v.d, v.f, v.pi.id)
	
	# display graph itself		
	def display(self):
		for i in range(0,self.n):
			s = ""
			for v in self.Adj[i]:
				vid = str(v.id)
				s = vid + " " + s
			s = str(i) + ": " + s
			print(s)
			
