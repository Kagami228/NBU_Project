import trainingSet.py
import neuron.py
import net.py

def showVectorVals(label , v):
    print(label+" ")
    str=""
    for i in range(len(v)):
        str=str+v[i]+" "
    print(str)

trainingSet trainingData("testData.txt")# Обучаюзий набор из txt
list<unsigned> topology#вектор 
trainingData.getTopology(topology)#заполнить вектор topology
net net(topology)#сеть вектора

list<double> inputVals, targetVals, resultVals#входное значение, целевое значение, Значение результата

trainingPass = 0#Тренировочный проход

	#while (!trainingDat.isEOF())#пока не конец файла
while (!trainingData.isEOF()):#пока не конец файла
    trainingPass=trainingPass+1
    print("Pass: "+trainingPass)#вывод пути
    if (trainingData.getNextInputs(inputVals) != topology[0]): #если (полученные следующие входы) != значению(topology[0])) То  ↓
        exit(0) #остановка
    showVectorVals("Input:", inputVals)#Вызов функции Показать Входные значения!
    net.feedForward(inputVals)#Подаём вперёд данные
    trainingData.getTargetOutputs(targetVals)#получить целевые результаты
    showVectorVals("Targets:", targetVals)#ответ целевой
    assert(targetVals.size() == topology.back())#Проверка на ошибку, что то типа того
    net.getResults(resultVals)#получаем результат из сети
    showVectorVals("Outputs", resultVals)#Выписываем его
    net.backProp(targetVals)#вроде бы задня опора сети Или Высчет ошибки
    print("Net average error:" , net.getRecentAverageError())#вывод Чистая средняя ошибка 
    print(Done)#Типа закончили
   #if defined(_MSC_VER) || defined(_WIN32)//Проврка по макросам
system("PAUSE")#пауза
#endif
	#return(0)#ТОЧКА
