class Quadrant:
    def __init__(self, large, start,name):
        self.items = []
        self.large = large
        self.start = start
        self.name = name

    def add(self,parameter_list):
        for ele in range(self.start,len(parameter_list)):
            if len(self.items) < self.large:
                self.items.append(parameter_list[ele])