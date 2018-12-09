class Point(object):
    def __init__(self, row=None, col=None, dist=None):
        self.row=row
        self.col=col
        self.dist=dist

    def __repr__(self):
        return "(" + str(self.row) + ", " + str(self.col) + ", " + str(self.dist) + ")"