import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

data = pd.read_csv('Responses.csv')

# the function to encode all category data into numerical data
def label_encoder(df):
    df.dropna(axis = 1, inplace = True)
    le = LabelEncoder()
    for column in df.columns:
        df.loc[:, column+'_trans'] = le.fit_transform(df[column])
        
    return df


# function to select all important features for our machine learning model
def features(df):
    df_train = df.drop(columns = ['age_range', 'gender', 'residence_type', 'parent_occupation',
       'education_completed', 'medium', 'board', 'academics',
       'preferred_stream', 'engineering_stream', 'career_1', 'career_2',
       'career_3'])
    X = df_train.drop(columns = ['career_1_trans', 'career_2_trans',
       'career_3_trans'])
    y = df_train[['career_1_trans', 'career_2_trans',
       'career_3_trans']]
    return X, y

# spliting the data into training and testing 
df = label_encoder(data)
X, y = features(df)
X_train, X_test, y_train, y_test = train_test_split(X, y ,test_size=0.10, random_state=42)

# function for training out ML model and return the model
def train_model(X_train, y_train):
    reg = DecisionTreeRegressor()
    model = reg.fit(X_train, y_train)
    
    return model

# training our model
model = train_model(X_train, y_train)

# mapping predicted values
pred = model.predict([[0,2,2,2,1,0,3,2,1, 1]])
for i in range(1,4):
    print(df[f'career_{i}'].loc[df.index[(df['career_1_trans']==int(pred[0][i-1]))][0]])