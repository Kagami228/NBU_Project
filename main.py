import treiningSet
import neuron
import net

def showVectorVals(label , v):
    print(label+" ")
    str=""
    for i in range(len(v)):
        str=str+v[i]+" "
    print(str)

trainingData=treiningSet("testData.txt")
topology=[]
trainingData.getTopology(topology)
net(topology)
inputVals=[]
targetVals=[]
resultVals=[]
trainingPass = 0
while trainingData.isEOF():
    trainingPass=trainingPass+1
    print("Pass: "+trainingPass)
    if (trainingData.getNextInputs(inputVals) != topology[0]): 
        exit(0) 
    showVectorVals("Input:", inputVals)
    net.feedForward(inputVals)
    trainingData.getTargetOutputs(targetVals)
    showVectorVals("Targets:", targetVals)
    assert(targetVals.size() == topology.back())
    net.getResults(resultVals)
    showVectorVals("Outputs", resultVals)
    net.backProp(targetVals)
    print("Net average error:" , net.getRecentAverageError())
    print(Done)
system("PAUSE")
