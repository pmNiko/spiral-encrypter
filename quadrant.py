class Quadrant:
    def __init__(self, number, name):
        self.items = []
        self.large = number
        self.name = name
    def add(self,parameter_list):
        for ele in parameter_list:
            self.items.append(ele)
    
    # def procesar(characters):
    #     if len(self.tems) <= self.large:
    #     for char in characters
    #         sel