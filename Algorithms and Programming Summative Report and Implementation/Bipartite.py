# Candidate number: 14459
# Using Python 3

from collections import deque
from Graph import Graph

# Checks whether a given undirected graph is bipartite
def is_bipartite(G):
    q = []
    for a in G.V:
        a.color = None
    for a in G.V:
        if a.color == None:
            q.append(a)
            a.color = 'white'
            while len(q)>0:
                u = q.pop()
                if u in G.Adj[u.id]:
                    return False
                for v in G.Adj[u.id]:
                    if v.color == None:
                        if u.color == 'white':
                            v.color = 'black'
                        else:
                            v.color = 'white'
                        q.append(v)
                    elif u.color == v.color:
                        return False
    return True
            
        
            
if __name__ == '__main__':
    G = Graph()
    for i in range(0,9):
        G.add_node()
    G.add_edge_using_ids(0,1)
    G.add_edge_using_ids(2,1)
    G.add_edge_using_ids(2,3)
    G.add_edge_using_ids(4,3)
    
    
print(is_bipartite(G))
