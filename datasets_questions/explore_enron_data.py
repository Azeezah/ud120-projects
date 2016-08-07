#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from time import time
t0 = time()
print("Loading data...")

#changed 'r' to 'rb' for python 3
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", 'rb'))
print("Loading time:", time()-t0)
print("Number of people:", len(enron_data))
print("Number of features:", len(enron_data["SKILLING JEFFREY K"].keys()))
print("Number of interesting people:", sum(enron_data[person]['poi'] for person in enron_data.keys()))
print(list(enron_data.keys()))
print(list(enron_data["SKILLING JEFFREY K"].keys()))

