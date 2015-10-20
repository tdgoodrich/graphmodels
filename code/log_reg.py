from abcd import Abcd
import arff
import sys
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn import cross_validation

# Usage:
#   python log_red.py [dataset directory] [datasets]
#
# Assumes:
# - Arguments are valid arff files in the dataset folder
# - Output is the last column in arff file
def main():
	dataset_dir = sys.argv[1]
	for filename in sys.argv[2:]:
		# Read in arff file
		dataset = arff.load(open("%s%s.arff" % (dataset_dir, filename), "rb"))
		data = np.array(dataset['data'])

		# Take only the numeric features (exclude the output field here)
		numericRows = [i for i in xrange(len(dataset["attributes"])-1) if dataset["attributes"][i][1] == "NUMERIC"]
		train = np.array([[row[i] for i in numericRows] for row in data], dtype=float)
		target = np.array([row[-1] for row in data], dtype=float)
		# If we want boolean target:
	  	target = np.array([int(x > 0) for x in target], dtype=str)

		# Set up the learner we want
		lr = LogisticRegression()

		# Do a 10-fold stratified cross validation
		k = min(10, len(target))
		skf = cross_validation.StratifiedKFold(y=target, n_folds=k)

		count = 0
		for traincv, testcv in skf:
			count += 1
			print "\n%d-Fold Cross Validation Fold #%d" % (k, count)
			abcd = Abcd(db="ant", rx="LogReg")
			model = lr.fit(train[traincv], target[traincv])
			predicted = model.predict(train[testcv])
			for act, pred in zip(target[traincv], predicted):
				abcd.tell(actual=act, predict=pred)
			abcd.header()
			abcd.ask()

if __name__ == "__main__":
	main()