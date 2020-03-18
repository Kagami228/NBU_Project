import random

class Neuron(object):
    numOtputs=0.0
    myIndex=0.0
    eta = 0.15
    alpha = 0.5
    outputVal
    m_myIndex
    gradient
    outputWeights=[]

    def __init__(self,numOutputs,myIndex):
        """Constructor"""
        self.numOtputs = numOtputs
        self.myIndex = myIndex
         
        for c in range(numOutputs):
            self.outputWeights.append(Connection())
            self.outputWeights[-1].weight= randomWeight()
        self.m_myIndex = myIndex


    def updateInputWeights(self,prevLayer):
        for n in range(len(prevLayer)):
            Neuron1 = prevLayer[n]
            soldDeltaWeight = Neuron1.outputWeights[self.m_myIndex].deltaWeight
            newDeltaWeight = self.eta * Neuron1.getOutputVal() * self.gradient + self.alpha * oldDeltaWeight
            Neuron1.outputWeights[self.m_myIndex].deltaWeight = newDeltaWeight
            Neuron1.outputWeights[self.m_myIndex].weight += newDeltaWeight


    def randomWeight(self):
      return( random.randint(0, 2147483647)/2147483647)



    def sumDOW(self,nextLayer):
        sum = 0.0
        for n in range (len(nextLayer)-1):
            sum += self.outputWeights[n].weight * nextLayer[n].self.gradient
        return sum



    def calcHiddenGradients (self,nextLayer):
         dow = sumDOW(nextLayer)
         self.gradient = dow * activationFunctionDerivative(self.outputVal)

         
    def activationFunction(x):
        return tanh(x)


    def calcOutputGradients(self): 
        targetVals=0.0


    def activationFunctionDerivative(x):
        return 1.0 - x * x
     
    
    def feedForward(self,prevLayer):
     sum = 0.0
     for n in range(len(prevLayer)):
         sum += prevLayer[n].getOutputVal() 
         prevLayer[n].self.outputWeights[self.m_myIndex].weight

     self.outputVal = activationFunction(sum)



class Connection(object):
    weight=0.0
    deltaWeight=0.0
    def __init__(self,weight,deltaWeight):
        self.deltaWeight=deltaWeight
        self.weight=weight
