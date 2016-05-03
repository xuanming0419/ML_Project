from preprocess import preprocess
from selector import selector
from crossValidation import crossValidation
from naiveBayes import naiveBayes
from trainError import trainError
import csv

posPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/train/pos/'
negPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/train/neg/'
testPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/test/'

process = preprocess()

posTrain = []
negTrain = []
testData = []

posTrain = process.getCleanTxt(posPath, 'pos')
negTrain = process.getCleanTxt(negPath, 'neg')
testData = process.getCleanTestData(testPath)

cvTrainError = crossValidation()
crossValidationResult = cvTrainError.tenCrossValidation(posTrain, negTrain)
print 'The 10 cross-validation accuracy is ' + str(1 - crossValidationResult * 1.0 /25000)

trainError = trainError()
trainErrorResult = trainError.computerTrainError()
print 'The train error is : ' + str(trainErrorResult * 1.0 / 25000)

classifier = naiveBayes()
result = classifier.train(posTrain, negTrain, testData)

fout = file('result.csv', 'w')
fout = open('result.csv', 'a')
fout.write('id,labels\n')

result.keys().sort()
for i in result:
    fout.write(str(i) + ',' + result[i] + '\n')

fout.close()
