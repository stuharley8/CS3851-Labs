from collections import deque
import copy
import sys


class DiGraph:
    """
    Directed Graph class
    Implemented using a Dictionary; keys are vertices. values are a set of vertices which are connected to that vertex. 
    """
    def __init__(self):
        self._edges = {}
    
    """
    Adds a new vertex to the graph.
    """
    def add_vertex(self, v):
        if not self.vertex_exists(v):
            self._edges[v] = set()
    
    """
    Adds and edge to the directed graph. U is the starting vertex. V is the ending vertex.
    """
    def add_edge(self, u, v):
        if self.vertex_exists(u):
            self._edges[u].add(v)
        else:
            self.add_vertex(u)
            self._edges[u].add(v)
        if not self.vertex_exists(v):
            self.add_vertex(v)
    
    """
    Checks if a vertex exists in the graph.
    """
    def vertex_exists(self, v):
        if v in self._edges:
            return True
        return False
    
    """
    Returns the number of vertices are in the graph
    """
    def count_vertices(self):
        return len(self._edges.keys())
    
    """
    Returns the number of edges in the graph
    """
    def count_edges(self):
        return len(self.edge_set())
    
    """
    Return whether or not an edge exists
    """
    def edge_exists(self, u, v):
        if self.vertex_exists(u) and v in self._edges[u]:
            return True
        return False
    
    """
    Returns all the edges outgoing from vertex v
    """
    def get_outgoing_edges(self, v):
        if self.vertex_exists(v):
            return self._edges[v]
        return set()
    
    """
    This method will loop through all of the edges, create a 2-tuple of the vertices involved in each edge for each edge,
    and add the tuples to a set. The set will then be returned.
    """
    def edge_set(self):
        edge_set = set()
        for vertex in self._edges:
            for connected_vertex in self._edges[vertex]:
                edge_set.add((vertex, connected_vertex))
        return edge_set
        

class Vertex:
    """
    Models vertices in a graph.  The pi, color, and d attributes
    are used to store information as part of a breadth-first search.
    The name attribute is used for a unique identifier for each
    vertex.
    """
    def __init__(self, pi=None, color="WHITE", d=sys.maxsize, name=None):
        self.pi = pi
        self.color = color
        self.d = d
        self.name = name

def load_data(training_flname, testing_flname):
    """
    Loads the training and testing set data. Returns
    a pair of graphs corresponding to the two data sets.
    """
    # We want to avoid creating duplicate Vertex objects
    # for the same user.  We will check the dictionary for
    # an existing Vertex object before creating another
    vertices = dict()
    with open(training_flname) as fl:
        G1 = DiGraph()
        for ln in fl:
            cols = ln.split()
            if cols[0] not in vertices:
                vertices[cols[0]] = Vertex(name=cols[0])
            if cols[1] not in vertices:
                vertices[cols[1]] = Vertex(name=cols[1])
            u = vertices[cols[0]]
            v = vertices[cols[1]]
            G1.add_edge(u, v)
            
    with open(testing_flname) as fl:
        G2 = DiGraph()
        for ln in fl:
            cols = ln.split()
            if cols[0] not in vertices:
                vertices[cols[0]] = Vertex(name=cols[0])
            if cols[1] not in vertices:
                vertices[cols[1]] = Vertex(name=cols[1])
            u = vertices[cols[0]]
            v = vertices[cols[1]]
            G2.add_edge(u, v)

    return G1, G2

def precision(recommendations, testing_set):
    """
    Precision measures the fraction of positive predictions
    were found in the test set (were true positives).

    A precise algorithm rarely makes false positive predictions.
    """
    rec_edges = recommendations.edge_set()
    test_edges = testing_set.edge_set()
    intersection = rec_edges.intersection(test_edges)
    
    if len(rec_edges) == 0:
        return 0.0
    
    return float(len(intersection)) / len(rec_edges)
    
def recall(recommendations, testing_set):
    """
    Recall measures the fraction of test set that
    were predicted positively.
    """
    rec_edges = recommendations.edge_set()
    test_edges = testing_set.edge_set()
    intersection = rec_edges.intersection(test_edges)
    
    if len(test_edges) == 0:
        return 0.0
    
    return float(len(intersection)) / len(test_edges)

def bfs(G, s):
    """
    Performs a breadth-first search of the graph G, starting at vertex s.
    
    Hints:
     * sys.maxsize can be used in place of the INFTY constant.
     * The Python data structure deque is a double-ended queue. You can
       use q.append() to add the back of the queue, q.popleft() to remove
       items from the front of the queue, and len(q) to check if the queue
       is empty (len(q) == 0).
    """
    for u in G._edges.keys():
        u.color = "WHITE"
        u.d = sys.maxsize
        u.pi = None
    s.color = "GRAY"
    s.d = 0
    s.pi = None
    q = deque([s])
    while len(q) != 0:
        u = q.popleft()
        for v in G.get_outgoing_edges(u):
            if v.color is "WHITE":
                v.color = "GRAY"
                v.d = u.d + 1
                v.pi = u
                q.append(v)
        u.color = "BLACK"
          
def recommend_friends_for_user(G, s, max_depth):
    """
    Performs a breadth-first search of the graph G, starting at vertex s.
    Does not traverse vertices with d > max_depth.
    Returns a list of all vertices encountered.
    
    Hints:
     * sys.maxsize can be used in place of the INFTY constant.
     * The Python data structure deque is a double-ended queue. You can
       use q.append() to add the back of the queue, q.popleft() to remove
       items from the front of the queue, and len(q) to check if the queue
       is empty (len(q) == 0).
    """
    for u in G._edges.keys():
        u.color = "WHITE"
        u.d = sys.maxsize
        u.pi = None
    s.color = "GRAY"
    s.d = 0
    s.pi = None
    q = deque([s])
    recommended = []
    while len(q) != 0:
        u = q.popleft()
        for v in G.get_outgoing_edges(u):
            if v.color is "WHITE":
                v.color = "GRAY"
                v.d = u.d + 1
                v.pi = u
                if v.d <= max_depth:
                    q.append(v)
                    recommended.append(v)
        u.color = "BLACK"
    return recommended
    
def recommend_all_friends(G, max_depth):
    """
    Generates recommendations for all users by performing
    a depth-limited breadth-first search for each user.
    
    The resulting recommendations are stored as a DiGraph.
    """
    h = DiGraph()
    for u in G._edges.keys():
        targets = recommend_friends_for_user(G, u, max_depth)
        for v in targets:
            if not G.edge_exists(v, u):
                h.add_edge(u, v)
                h.add_edge(v, u)
    return h
