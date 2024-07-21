class Neuron:
    def __init__ (self, w):
        self.w = w
        
    def у(self, x):
        i = 0
        s = []
        for value in x:
            s.append(value * self.w[i])
            i += 1
        return sum(s)
    
    def onestep(self, x): # Функция активации
        if x >= 0:
            return 1
        else:
            return 0