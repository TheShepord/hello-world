class Node(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name
    
class Edge(object):
    def __init__(self,src,dest):
        """ASsumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()
    
class Digraph(object):
    """edges is a dict mapping each node to a list of its children"""
    def __init__(self):
        self.edges = {}
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node] = []
    def addEdge(self,edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    def getChildrenOf(self,node):
        return self.edges[node]
    def hasNode(self,node):
        return node in self.edges
    def getNode(self,node):
        for n in self.edges:
            if n.getName() == node:
                return n
        raise NameError(n)
    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result[:-1]
    
class Graph(Digraph):
    def addEdge(self,edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)
 
def DFS(graph,start,end,path,shortest):
    path = path + [start]
    
    if start == end:
        return path
    
    for node in graph.getChildrenOf(start):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = DFS(graph,node,end,path,shortest)
                if newPath != None:
                    shortest = newPath
    return shortest
    
   

def shortestPath(graph,start,end):
    result = DFS(graph,start,end,[],None)
    for i in result:
        if str(i) == 'ABC':
            print(0, end='')
        elif str(i) == 'ACB':
            print(1, end='')
        elif str(i) == 'BAC':
            print(2, end='')
        elif str(i) == 'BCA':
            print(3, end='')
        elif str(i) == 'CAB':
            print(4, end='')
        elif str(i) == 'CBA':
            print(5, end='')
def powerSeries(items):
    N = len(items)
    result = []
    for i in range(2**N):
        key = []
        for j in range(N):
            if (i>>j)%2 == 1:
                key = key + [items[j]]
        result.append(key)
    return result

def all_perms(elements):
    if len(elements) <=1:
        return elements
    else:
        tmp = []
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                tmp.append(perm[:i] + elements[0] + perm[i:])
        return tmp

    
    


nodes = []
nodes.append(Node("ABC")) # nodes[0]
nodes.append(Node("ACB")) # nodes[1]
nodes.append(Node("BAC")) # nodes[2]
nodes.append(Node("BCA")) # nodes[3]
nodes.append(Node("CAB")) # nodes[4]
nodes.append(Node("CBA")) # nodes[5]

g = Graph()
for n in nodes:
    g.addNode(n)

memo = []
for node in nodes:
    if node not in memo:
        for i in range(len(node.getName())-1):
            for node2 in nodes:
                if node.getName()[i] == node2.getName()[i+1] and node.getName()[i+1] == node2.getName()[i]:
                    g.addEdge(Edge(node,node2))
                    memo.append(node2)
