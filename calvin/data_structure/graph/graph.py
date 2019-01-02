from calvin.data_structure.stack import Stack
from enum import Enum
from calvin.data_structure.linkedlist import LinkedList

class State(Enum):
    VISITED = 1
    UNVISITED = 2

class Node(object):
    def __init__(self, vertex=None, children=0):
        self.vertex = vertex
        self.childCount = 0
        self.children = [None] * children
        self.state = State.UNVISITED

    def add_child_node(self, adj):
        adj.state = State.UNVISITED
        if (self.childCount < 30):
            self.children[self.childCount] = adj
            self.childCount+=1

    def get_child(self):
        return self.children

    def get_vertex(self):
        return self.vertex

    def __repr__(self):
        return "Node("+str(self.vertex)+")"

class Graph(object):
    def __init__(self, size=10):
        self.vertices = [None] * size
        self.count = 0

    def add_node(self, n):
        if (self.count < 10):
            self.vertices[self.count] = n
            self.count += 1

    def get_node(self):
        return self.vertices

class Traversals(object):
    def __init__(self):
        self.vertices = []

    def dfs_iterative(self, root):
        s=Stack()
        s.push(root)
        while s.size() > 0:
            vertex = s.pop()
            self.vertices.append(vertex.get_vertex())
            for neighbor in vertex.get_child():
                if neighbor and neighbor.state == State.UNVISITED:
                    s.push(neighbor)
                    vertex.state = State.VISITED

    def dfs(self, root):
        if root == None:
            return

        self.vertices.append(root.get_vertex())
        root.state = State.VISITED

        for n in root.get_child():
            if n and n.state == State.UNVISITED:
                self.dfs(n)

    def bfs(self, root, match=None):
        if root == None:
            return False

        from collections import deque
        q = deque()
        root.state = State.VISITED
        q.append(root)

        while q:
            r = q.popleft()
            if match and r.get_vertex() == match.get_vertex():
                return True
            self.vertices.append(r.get_vertex())
            for n in r.get_child():
                if (n and n.state == State.UNVISITED):
                    q.append(n)
                    n.state = State.VISITED

        return False

    def route_between_two_nodes(self, a, b):
        return self.bfs(a,b)

    def detect_cycle(self, g):
        exists=set()
        for node in g.vertices:
            if self.__detect_cycle_rec(node,exists):
                return True
        return False

    def __detect_cycle_rec(self,node,exists):
        if node.vertex in exists:
            return True

        if node.state==State.VISITED:
            return False

        node.state=State.VISITED
        exists.add(node.vertex)
        for n in node.children:
            if self.__detect_cycle_rec(n,exists):
                return True

        exists.remove(node.vertex)
        return False

class Sorting(object):
    def __init__(self,graph=None):
        self.graph=graph

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, node, stack):

        # Mark the current node as visited.
        node.state=State.VISITED

        # Recur for all the vertices adjacent to this vertex
        for n in node.get_child():
            if n.state==State.UNVISITED:
                self.topologicalSortUtil(n, stack)

        # Push current vertex to stack which stores result
        stack.insert(0, node)

        # The function to do Topological Sort. It uses recursive

    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for node in self.graph.vertices:
            if node.state == State.UNVISITED:
                self.topologicalSortUtil(node, stack)

        return stack

class AdjacencyListGraph(object):
    def __init__(self, vertices):
        self.vertices = vertices
        self.array = []
        for i in range(vertices):
            temp = LinkedList()
            self.array.append(temp)

    def addEdge(self, source, destination):
        # As we are implementing a directed graph, (1,0) is not equal to (0,1)
        self.array[source].prepend(destination)

    def printGraph(self):
        print(">>Adjacency List of Directed Graph<<")
        print()
        for i in range(self.vertices):
            print("|", i, "| => "+str(self.array[i])+" -> ",end='')
            print("None")