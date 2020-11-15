class Content:  

    def __init__(self):
        self.char_list = []

    def parse(self, chars): 
        self.char_list = []       
        for char in chars:
            self.char_list.append(char.upper())
        return self.char_list
    
    def render_hash(self, array_chars):
        hash_list = ''.join(array_chars)
        return hash_list