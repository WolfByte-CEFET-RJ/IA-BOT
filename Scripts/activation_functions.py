import numpy as np

class aF: # aF por causa de Activation Function

    @staticmethod
    def sigmoid(x): 
        return 1/(1+ np.exp(-x)) 

    @staticmethod
    def relu(x): 
        if(x > 0): 
            return x
        else: 
            return 0
    
    @staticmethod
    def leakyRelu(x): 
        if(x < 0):
            return 0.01 * x
        else: 
            return x

    @staticmethod
    def binaryStep(x): 
        if(x < 0): 
            return 0
        else: 
            return 1

    