import torch.nn as nn   #pip insall tourch
import torch.nn.functional as F

class NeuralNetwork(nn.Module): # Create a neural network class and call nn.module which is a module of Neural Network

    def __init__(self, input_size,hidden_size,num_classes):  # Define a func __init__ and initialize 3 linear model
        super(NeuralNetwork,self).__init__()
        
        # So besically Neural network is a Linear module (perceptron) which is created by multiple layer like One Input layer, One or more hidden layer 
        self.l1 = nn.Linear(input_size,hidden_size)     # Layer 1
        self.l2 = nn.Linear(hidden_size,hidden_size)    # Layer 2
        self.l3 = nn.Linear(hidden_size,num_classes)    # Layer 3
        self.relu = nn.ReLU # ReLU is an Activation function --> max(0,x)

    def forward(self,x):    # Here 'x' var is an output
        out = self.l1(x)    # x --> l1
        out = F.relu(out)   # Relucate into l2
        out = self.l2(out)  
        out = F.relu(out)   #  Relucate into l3
        out = self.l3(out)
        return out
