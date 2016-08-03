#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
from time import time

t0 = time()
print("Loading data...")
features_train, labels_train, features_test, labels_test = makeTerrainData()
print("Loading time:", time()-t0)

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

from sklearn.ensemble import AdaBoostClassifier as ABC

clf = ABC(n_estimators=100)

t0 = time()
print("Training...")
### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary
clf.fit(features_train, labels_train)

print("Training time:", time()-t0)

t0 = time()
print("Predicting...")

y = clf.predict(features_test)
print("Predicting time:", time()-t0)

scores = (y == labels_test)
num_correct = scores.sum()
total = scores.size
percentage = (num_correct*100) / total

print("Percent Correct: %.1f%% (that's %d of %d)" % (percentage, num_correct, total))




try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
