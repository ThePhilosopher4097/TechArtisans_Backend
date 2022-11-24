from joblib import dump, load
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

def predictCareer():

    df = pd.read_csv('../Dataset/Responses.csv')
    le = LabelEncoder()
    df_cleaned = df.dropna(axis = 1)

    for column in df_cleaned.columns:
        df_cleaned[column] = le.fit_transform(df[column])
    
    X = df_cleaned.drop(columns = ['age_range','career_1', 'career_2', 'career_3'])
    y = df_cleaned[['career_1']]

    X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.20, random_state=42)

    dtree = DecisionTreeClassifier(random_state=1)
    dtree = dtree.fit(X_train, y_train)

    y_pred = dtree.predict(X_test)
    cm = confusion_matrix(y_test,y_pred)
    accuracy = accuracy_score(y_test,y_pred)
    print("confusion matrics=",cm)
    print("  ")
    print("accuracy=",accuracy*10)

    dump(dtree, 'ML_Model.joblib')

predictCareer()