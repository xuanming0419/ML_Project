from naiveBayes import naiveBayes

class crossValidation:
	def tenCrossValidation(self, posTrain, negTrain):

		def getError(result):

			error = 0

			for i in result:
				if i[0] != i[1]:
					error = error + 1

			return error

		posTrain.sort()
		negTrain.sort()

		error = 0
		classifier = naiveBayes()

		for i in range(1, 11):
			posCrossValidationTrain = posTrain[0 : 1250 * (i - 1)] + posTrain[1250 * i : 12500]
			negCrossValidationTrain = negTrain[0 : 1250 * (i - 1)] + negTrain[1250 * i : 12500]
			crossValidationTest = posTrain[1250 * (i - 1) : 1250 * i] + negTrain[1250 * (i - 1) : 1250 * i]
			result = classifier.test(posCrossValidationTrain, negCrossValidationTrain, crossValidationTest)
			error = error + getError(result)

		return error