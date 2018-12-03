from calvin.data_structure.stack import Stack

from enum import Enum
class State(Enum):
    VISITED = 1
    UNVISITED = 2

class Node(object):
    def __init__(self, vertex=None, children=0):
        self.vertex = vertex
        self.childCount = 0
        self.children = [None] * children
        self.state = None

    def add_child_node(self, adj):
        adj.state = State.UNVISITED
        if (self.childCount < 30):
            self.children[self.childCount] = adj
            self.childCount+=1

    def get_child(self):
        return self.children

    def get_vertex(self):
        return self.vertex

class Graph(object):
    def __init__(self):
        self.vertices = [None] * 10
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


