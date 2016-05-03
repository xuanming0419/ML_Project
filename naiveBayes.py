import math

class naiveBayes:
	def train(self, posTrain, negTrain, testData):

		posWords = {}
		negWords = {}
		testResult = {}

		posWordsCount = 0
		negWordsCount = 0

		m = 0.84

		for i in posTrain:
			for j in i[0]:
				if posWords.has_key(j):
					posWords[j] = posWords[j] + 1
				else:
					posWords[j] = 1

		posVocabulary = len(posWords)
		for i in posWords:
			posWordsCount = posWordsCount + posWords[i]	


		for i in negTrain:
			for j in i[0]:
				if negWords.has_key(j):
					negWords[j] = negWords[j] + 1
				else:
					negWords[j] = 1

		negVocabulary = len(negWords)
		for i in negWords:
			negWordsCount = negWordsCount + negWords[i]	

		print 'Postive total words: ' + str(posWordsCount)
		print 'Negtive total words' + str(negWordsCount)
		print 'Postive vocabulary size: ' + str(len(posWords))
		print 'Negtive vocabulary size: ' + str(len(negWords))

		for i in posWords:
			posWords[i] = posWords[i] ** 3

		for i in negWords:
			negWords[i] = negWords[i] ** 3

		for i in testData:
			txtPosProbability = 0
			txtNegProbability = 0
			for j in i[0]:
				if posWords.has_key(j):
					wordPosProbability = (posWords[j] + m) * 1.0 / (posWordsCount + m * posVocabulary)
				else:
					wordPosProbability = (0 + m) * 1.0 / (posWordsCount + m * posVocabulary)
				txtPosProbability = txtPosProbability + math.log(wordPosProbability, 2)

				if negWords.has_key(j):
					wordNegProbability = (negWords[j] + m) * 1.0 / (negWordsCount + m * negVocabulary)
				else:
					wordNegProbability = (0 + m) * 1.0 / (negWordsCount + m * negVocabulary)
				txtNegProbability = txtNegProbability + math.log(wordNegProbability, 2)

			number = int(i[1].split('.')[0])
			if txtPosProbability >= txtNegProbability:
				testResult[number] = '1'
			else:
				testResult[number] = '0'
		return testResult

	def test(self, posTrain, negTrain, testData):

		posWords = {}
		negWords = {}
		testResult = []
		testData.sort()

		posWordsCount = 0
		negWordsCount = 0

		m = 0.84

		for i in posTrain:
			for j in i[0]:
				if posWords.has_key(j):
					posWords[j] = posWords[j] + 1
				else:
					posWords[j] = 1

		posVocabulary = len(posWords)
		for i in posWords:
			posWordsCount = posWordsCount + posWords[i]	


		for i in negTrain:
			for j in i[0]:
				if negWords.has_key(j):
					negWords[j] = negWords[j] + 1
				else:
					negWords[j] = 1

		negVocabulary = len(negWords)
		for i in negWords:
			negWordsCount = negWordsCount + negWords[i]	

		for i in posWords:
			posWords[i] = posWords[i] ** 3
		for i in negWords:
			negWords[i] = negWords[i] ** 3

		k = 0
		for i in testData:
			txtPosProbability = 0
			txtNegProbability = 0
			for j in i[0]:
				if posWords.has_key(j):
					wordPosProbability = (posWords[j] + m) * 1.0 / (posWordsCount + m * posVocabulary)
				else:
					wordPosProbability = (0 + m) * 1.0 / (posWordsCount + m * posVocabulary)
				txtPosProbability = txtPosProbability + math.log(wordPosProbability, 2)

				if negWords.has_key(j):
					wordNegProbability = (negWords[j] + m) * 1.0 / (negWordsCount + m * negVocabulary)
				else:
					wordNegProbability = (0 + m) * 1.0 / (negWordsCount + m * negVocabulary)
				txtNegProbability = txtNegProbability + math.log(wordNegProbability, 2)

			if txtPosProbability >= txtNegProbability:
				testResult.append((i[1], 'pos'))
			else:
				testResult.append((i[1], 'neg'))
			k = k + 1
		return testResult