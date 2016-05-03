import os, re

class preprocess:
	def getCleanTxt(self, path, label):

		train = []
		deleteWord = ['i', 'me', 'my', 'us', 'we', 'you', 'he', 'she', 'your', 'his', 'him', 'her', 'they', 'them', 'their', 'the', 'this', 'that', 'a', 'an', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'being', 'have', 'has', 'had', 'and', 'will', 'it', 's', 'its', 'at', 'with', 'been', '', 'br', '', 'movie', 'film', 't', 'what', 'when', 'which', 'there', 'who', 'on', 'in', 'of', 'by', 'to', 'up', 'out', 'from', 'about','for']
		
		for filename in os.listdir(path):
			if filename == '.DS_Store':
				continue
			else:
				filepath = path + filename
				f = open(filepath, 'r')
				txt = f.read()
				cleanTxt = re.sub('[^A-Za-z]', ' ', txt).lower().split(' ')
				for word in deleteWord:
					while word in cleanTxt:
						cleanTxt.remove(word)
				train.append((cleanTxt, label))
				f.close()
		return train

	def getCleanTestData(self, path):

		test = []
		deleteWord = ['i', 'me', 'my', 'us', 'we', 'you', 'he', 'she', 'your', 'his', 'him', 'her', 'they', 'them', 'their', 'the', 'this', 'that', 'a', 'an', 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'being', 'have', 'has', 'had', 'and', 'will', 'it', 's', 'its', 'at', 'with', 'been', '', 'br', '', 'movie', 'film', 't', 'what', 'when', 'which', 'there', 'who', 'on', 'in', 'of', 'by', 'to', 'up', 'out', 'from', 'about','for']
		
		for filename in os.listdir(path):
			if filename == '.DS_Store':
				continue
			else:
				filepath = path + filename
				f = open(filepath, 'r')
				txt = f.read()
				cleanTxt = re.sub('[^A-Za-z]', ' ', txt).lower().split(' ')
				for word in deleteWord:
					while word in cleanTxt:
						cleanTxt.remove(word)
				test.append((cleanTxt, filename))
				f.close()
		return test