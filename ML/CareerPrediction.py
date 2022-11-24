import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, OneHotEncoder


df = pd.read_csv('../Dataset/Responses.csv')

print(df.head())
print('The shape of our training set: %s professionals and %s features'%(df.shape[0],df.shape[1]))
print("Columns in our dataset: " , df.columns)
print("List of Numerical features: \n" , df.select_dtypes(include=np.number).columns.tolist())
print("\n\nList of Categorical features: \n" , df.select_dtypes(include=['object']).columns.tolist())
print("Null Values ===> ", df.isnull().sum(axis=0))
print("\n\nList of Categorical features: \n" , df.select_dtypes(include=['object']).columns.tolist())

# =============================================================================================================

# for i in df.columns:
#     df[i] = df[i].astype('category')
#     df[i + "_code"] = df[i].cat.codes

print("\n\nList of Categorical features: \n" , df.select_dtypes(include=['object']).columns.tolist())

print(df.head())

ft = df.copy()
ft.drop(['career_1','career_2','career_3'], axis = 1, inplace=True)

print(ft.head())

print("List of Numerical features: \n" , ft.select_dtypes(include=np.number).columns.tolist())
print("\n\nList of Categorical features: \n" , ft.select_dtypes(include=['object']).columns.tolist())

# =============================================================================================================

def prepare_inputs(X_train, X_test):
	ohe = OneHotEncoder(handle_unknown='infrequent_if_exist')
	ohe.fit(X_train)
	X_train_enc = ohe.transform(X_train)
	X_test_enc = ohe.transform(X_test)
	return X_train_enc, X_test_enc

# prepare target
def prepare_targets(y_train, y_test):
	le = LabelEncoder()
	le.fit(y_train)
	y_train_enc = le.transform(y_train)
	y_test_enc = le.transform(y_test)
	return y_train_enc, y_test_enc

# Taking all independent variable columns
df_train_x = ft.copy()
print(df_train_x.columns)
# Target variable column
df_train_y = df[['career_1']]
print(df_train_y.columns)

x_train, x_test, y_train, y_test = train_test_split(df_train_x, df_train_y, test_size=0.20, random_state=42)

# prepare input data
X_train, X_test = prepare_inputs(x_train, x_test)
# prepare output data
y_train, y_test = prepare_targets(y_train, y_test)

# ========================================================================================================

dtree = DecisionTreeClassifier(random_state=1)
dtree = dtree.fit(x_train, y_train)

y_pred = dtree.predict(x_test)
cm = confusion_matrix(y_test,y_pred)
accuracy = accuracy_score(y_test,y_pred)
print("confusion matrix=",cm)
print("  ")
print("accuracy=",accuracy*10)



rf = RandomForestClassifier(random_state = 10)
rf.fit(x_train, y_train)
rfc_y_pred = rf.predict(x_test)
rfc_cm = confusion_matrix(y_test,rfc_y_pred)
rfc_accuracy = accuracy_score(y_test,rfc_y_pred)
print("confusion matrics=",rfc_cm)
print("  ")
print("accuracy=",rfc_accuracy*10)


userdata = [['9','2','2']]
ynewclass = dtree.predict(userdata)
ynew = dtree.predict_proba(userdata)
print(ynewclass)
print("Probabilities of all classes: ", ynew)
print("Probability of Predicted class : ", np.max(ynew))