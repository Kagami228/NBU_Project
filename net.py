
import neuron
from NBU_Project import topology
import typing
from typing import List

class net(object):
    error=0.0
    recentAverageError=0.0
    recentAverageSmoothingFactor=0.0
    layers=[]


    def __init__(self,topology):
        numLayers = len(topology)
        for layerNum in range(numLayers):
            self.layers.append(Layer())
            if( layerNum == len(topology) - 1):
                numOutputs=0
            else:
                umOutputs=topology[layerNum + 1]
                for neuronNum in range(topology[layerNum]):
                    self.layers[-1].append(neuron(numOutputs, neuronNum))
            self.layers[-1][-1].setOutputVal(1.0)
           

    def feedForward(self,inputVals):
        assert(len(inputVals) == len(layers[0]- 1))
        for i in range(len(inputVals)):
            self.layers[0][i].setOutputVal(inputVals[i])
        for layerNum in range(len(self.layers)):
            prevLayer = self.layers[layerNum - 1]
            for n in range(len(self.layers[layerNum]) - 1):
                self.layers[layerNum][n].feedForward(prevLayer)


    def backProp(self,targetVals):
        outputLayer = self.layers[-1]
        error = 0.0
        for n in range(len(outputLayer - 1)):
            delta = targetVals[n] - outputLayer[n].getOutputVal()
            error += delta * delta
            error /= len(outputLayer) - 1
        error = sqrt(error)
        recentAverageError =(recentAverageError * recentAverageSmoothingFactor + error)/(recentAverageSmoothingFactor + 1.0)
        for n  in range(len(outputLayer - 1)):
            outputLayer[n].calcOutputGradients(targetVals[n])
        layerNum=len(self.layers)-2
        for layerNum in range(layerNum,0):
            hiddenLayer = self.layers[layerNum]
            nextLayer = self.layers[layerNum + 1]
            for n in range(len(hiddenLayer)):
                hiddenLayer[n].calcHiddenGradients(nextLayer)
            layerNum=len(self.layers)-1
        for layerNum in range(layerNum,0):
            layer = layers[layerNum]
            prevLayer = layers[layerNum - 1]
            for n in range(len(layer - 1)):
                layer[n].updateInputWeights(prevLayer)
    def getResults(self,resultVals):
        resultVals.clear()  
        for n in range(len(self.layers[-1]- 1)):
            resultVals.append(self.layers[-1][n].getOutputVal())
            recentAverageError=getRecentAverageError() 
            return recentAverageError
