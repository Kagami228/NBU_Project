
class trainingSet(object):)
    trainingDataFile
    def __init__(self,name):
        self.trainingDataFile.open(str(name))
    def isEOF(self):
        return self.trainingDataFile.read(1)
    def getTopology(self,topology):
        line=""
        label=""
        n=0
        f = open(self.trainingDataFile)
        if(self.isEOF() and f.compare("topology:")!=0):
            os.abort()
        while(!f.isEOF):
            f.line()=n
            topology.append(n)
        return
    def getNextInputs(self,inputVals):
        inputVals.clear()
        line=""
        f = open(self.trainingDataFile)
        label=""
        if(f.compare("in:")==0):
            oneValue=0.0
            while(f.oneValue):
                inputVals.append(oneValue)
        return len(inputVals)
    def getTargetOutputs(self,targetOutputVals):
        targetOutputVals.clear()
        line=""
        label=""
        n=0
        f = open(self.trainingDataFile)
        if(f.compare("out:")==0):
            oneValue=0.0
            while(f.oneValue):
                targetOutputVals.append(oneValue)
        return len(targetOutputVals)
