class Connection:

    def __init__(self, destination, T: float, C: float):
        self.dest = destination
        self.prop = T
        self.trans = C

    def get_trans(self):
        return self.trans

    def get_prop(self):
        return self.prop

    def get_dest(self):
        return self.dest