from preprocess import preprocess
from naiveBayes import naiveBayes

class trainError:
	def computerTrainError(self):
		posPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/train/pos/'
		negPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/train/neg/'
		testPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/train/pos/'

		process = preprocess()

		posTrain = []
		negTrain = []
		testData = []

		posTrain = process.getCleanTxt(posPath, 'pos')
		negTrain = process.getCleanTxt(negPath, 'neg')
		testData = process.getCleanTestData(testPath)

		classifier = naiveBayes()
		result = classifier.test(posTrain, negTrain, testData)

		errorCount = 0
		for i in result:
			if i[1] == 'neg':
				errorCount = errorCount + 1

		testPath = '/Users/sunxinzi/Documents/Machine_Learning/Project/Sentiment Prediction/train/neg/'

		testData = []

		testData = process.getCleanTestData(testPath)
		result = classifier.test(posTrain, negTrain, testData)

		for i in result:
			if i[1] == 'pos':
				errorCount = errorCount + 1

		return errorCount