from collections import deque
import enum
from collections import defaultdict as dd

class Graph(object):
    def __init__(self):
        self.nodes = []
        self.map = dict()

    def create_node(self, name):
        if not name in self.map:
            n = Project(name)
            self.nodes.append(n)
            self.map[name] = n

        return self.map[name]

    def add_edge(self, startname, endname):
        start = self.create_node(startname)
        end = self.create_node(endname)
        start.add_neighbor(end)


class Project(object):
    class State(enum.Enum):
        BLANK = 1,
        PARTIAL = 2,
        COMPLETE = 3

    def __init__(self, name):
        self.name = name
        self.map = dd(str)
        self.children = []
        self.state = Project.State.BLANK


    def add_neighbor(self, n):
        if not self.map[n.name]:
            self.children.append(n)
            self.map[n.name] = n

class BuildOrder(object):
    def __init__(self, graph):
        if graph == None:
            raise ("Construct a graph first!")
        self.graph = graph

    def get_project_order(self, projects):
        g = self.graph
        s = deque()
        for project in projects:
            if project.state == Project.State.BLANK:
                if not self.run_dfs(project, s):
                    return None
        return s

    def run_dfs(self, project, s):
        if project.state == Project.State.PARTIAL:
            return False

        if project.state == Project.State.BLANK:
            project.state = Project.State.PARTIAL
            children = project.children
            for child in children:
                if not self.run_dfs(child, s):
                    return False
            project.state = Project.State.COMPLETE
            s.append(project.name)

        return True
