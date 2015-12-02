
from abcd import Abcd
import arff
import sys
import os
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn import cross_validation

dataset_dir = "datasets"

def readArff(filename):
	# Read in arff file
	dataset = arff.load(open(os.path.join(dataset_dir, filename + ".arff"), "rb"))
	data = np.array(dataset['data'])

	# Take only the numeric features (exclude the output field here)
	numericRows = [i for i in xrange(len(dataset["attributes"])-1) if dataset["attributes"][i][1] == "NUMERIC"]
	train = np.array([[row[i] for i in numericRows] for row in data], dtype=float)
	target = np.array([row[-1] for row in data], dtype=float)
	# If we want boolean target:
  	target = np.array([int(x > 0) for x in target], dtype=str)
  	return train, target

def printStatistics(k, count, actual, predicted):
	print "\n%d-Fold Cross Validation Fold #%d" % (k, count)
	abcd = Abcd(db="ant", rx="LogReg")
	for act, pred in zip(actual, predicted):
		abcd.tell(actual=act, predict=pred)
	abcd.header()
	abcd.ask() 

def main():
	for filename in sys.argv[1:]:
		train, target = readArff(filename)

		# Set up the learner we want
		eps = 50
		min_samples = 5
		learner = DBSCAN(eps=eps, min_samples=min_samples)
		clusters = learner.fit_predict(train)
		print clusters, len(set(clusters))

if __name__ == "__main__":
	main()