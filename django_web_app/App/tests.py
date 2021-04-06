from django.test import TestCase
import pickle, gzip
from sklearn.linear_model import LogisticRegression
# Create your tests here.

with open("E:\\Dibyendu\Projects\\1. Machine Learning Projects\\Heart Disease Project-1\\Models_save\\logistic.pickle", 'rb') as f:
    model = pickle.load(f)
    prediction = model.predict([[63,1,3,145,233,1,0,150,0,2.3,0,0,1]])
    print(prediction)
