#pragma once

class net: #сеть которой передали набор для обучения
	#VERNIS list layers#layers[layerNumber][NeuronNumber]__Нейронная Сеть__ #вектор векторов нейронов
	error=0.0# ошибка
	recentAverageError=0.0#Средняя ошибка за последнее время
	recentAverageSmoothingFactor=0.0#Средний коэффициент сглаживания в последнее время

	def __init__(self,topology):#Constructor 
	#vector с набором для обучения
	#						Cтроим сеть
	#						Розставляем нейронны, управляем и перебераем
	#						выворачиваем мозги, но понимаем(частично)
	   numLayers = len(topology)#Размер вектора входящих данных
	   for layerNum in range(numLayers):#Грубо говоря, по размеру вектора пошли, layerNum- от
           	self.layers.append(Layer())# в вектор (вектора нейронов) добавляем ещё вектор нейронов 
           if( layerNum == len(topology) - 1):
	       numOutputs=0
           else:
               umOutputs=topology[layerNum + 1]#если layerNum == размеру входного вектора данных ((topology.size()-1)), то numOutputs=0, иначе _topology[layerNum + 1]
               for neuronNum in range(topology[layerNum]):# от нуля по размеру topology[layerNum], neuronNum отсчётное значение
                   self.layers[-1].append(neuron(numOutputs, neuronNum))# в вектор векторов нейронов закидываем нейрон со значениями numOutputs И neuronNum
           self.layers[-1][-1].setOutputVal(1.0)#выдаём ответ последнего нейрона
    #
	def feedForward(self,inputVals):#подача вперед
		assert(len(inputVals) == len(layers[0]- 1))#Проверка на ошибку, что то типа того
		
		for i in range(len(inputVals)):
			self.layers[0][i].setOutputVal(inputVals[i])#устанавливаем выходные значения

		for layerNum in range(len(self.layers)):#Номер слоя
			prevLayer = self.layers[layerNum - 1]# предыдущий слой
			
			for n in range(len(self.layers[layerNum]) - 1):# по слоям
			    self.layers[layerNum][n].feedForward(prevLayer)# подаём вперёд

	def backProp(self,targetVals):#задняя опора(Или обратное распространение)
	#Обратное распростронение, если я правильно понимаю
	    outputLayer = self.layers[-1]#ссылка на последний элемент вектора layers // Выходной слой
            error = 0.0# обозначение ошибки 
            for n in range(len(outputLayer - 1)): #проход от 0 до outputLayer
                delta = targetVals[n] - outputLayer[n].getOutputVal()# высчитываем delta
                error += delta * delta#теперь ошибку
                error /= len(outputLayer) - 1#ошибка
	    error = sqrt(error)# квадратичное

	    recentAverageError =(recentAverageError * recentAverageSmoothingFactor + error)/(recentAverageSmoothingFactor + 1.0)#Чистая средняя ошибка 

	    for n  in range(len(outputLayer - 1)):#до размера выходного слоя
	   	outputLayer[n].calcOutputGradients(targetVals[n])# Высчитываем Градиент

	    layerNum=len(self.layers)-2
	    for layerNum in range(layerNum,0):# Пройдёмся от layers.size() - 2 до 0.
	 	hiddenLayer = self.layers[layerNum]#Нейронны скрытого слоя
		nextLayer = self.layers[layerNum + 1]#Нейроны следуйщего слоя

		for n in range(len(hiddenLayer)):#пойдём по скрытому слою
			hiddenLayer[n].calcHiddenGradients(nextLayer)#считаем градиент для каждого нейрона в скрытом слое
			
		layerNum=len(self.layers)-1
            for layerNum in range(layerNum,0):#Опять по слою
		 layer = layers[layerNum];#слой
		 prevLayer = layers[layerNum - 1];#Предыдущий слой
		 
		 for n in range(len(layer - 1)):
			layer[n].updateInputWeights(prevLayer);#считаем градиент данного нейронна из этого слоя
	
	def getResults(self,resultVals):#получить результаты
		#Выбираем ответ из сети Нейронов
	    resultVals.clear()#Очищаем  
            for n in range(len(self.layers[-1]- 1)):# по размеру Нейронной Сети
		    resultVals.append(self.layers[-1][n].getOutputVal())#закидываем ответы
            getRecentAverageError() 
            return recentAverageError #получить недавнюю среднюю ошибку  ... /Чистая средняя ошибка 
