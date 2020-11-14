abc = [
        'A',
        'B',
        'C','D',
        'E','F','G',
        'H','I','J','K','L',
        'M', '0', '1', '2', '3', '4', '5', '6',
        '7', '8', '9','N','Ñ','O','P','Q','R','S','T','U','V',
        'W','X','Y','Z','@','!','%','#','$',' ','?','-',')','/','.','(','=','"','+','*'
        ]
class Alphabet:
    
    def __init__(self):
        self.data = abc

    def position(self):
        for item in self.data:
            print('Posición ',self.data.index(item)+1, ' -> ', item )
    