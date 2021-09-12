#-------------------------------------------------------------------------
# AUTHOR: Josephine Nguyen
# FILENAME: decision_tree.py
# SPECIFICATION: This program reads the csv file, "contact_lens", then produces a decision tree based on ID3.
# FOR: CS 4200- Assignment #1
# TIME SPENT: 30 min
# #-----------------------------------------------------------*/
#
# #IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY T
#
# importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i, row in enumerate(reader):
        if i > 0: #skipping the header
            db.append(row)
            print(row)

#transform the original training features to numbers and add to the 4D array X. Forinstance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2,2, 2], ...]]
# Age:                    (Young = 1), (Presbyopic = 2), (Prepresbyopic = 3)
# Spectacle Prescription: (Myope = 1), (Hypermetrope = 2)
# Astigmatism:            (No = 1), (Yes = 2)
# Tear Production Rate:   (Reduced = 1), (Normal = 2)
X = [
    [1, 1, 1, 1],
    [2, 1, 1, 2],
    [3, 1, 1, 1],
    [3, 1, 1, 2],
    [2, 1, 2, 2],
    [1, 1, 2, 2],
    [1, 2, 1, 1],
    [3, 1, 2, 1],
    [2, 2, 1, 1],
    [1, 1, 2, 1],
]


# #transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
# Recommended Lenses:  (Yes = 1), (No = 2)
Y = [2, 2, 2, 1, 1, 1, 2, 2, 2, 1]


# #fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
