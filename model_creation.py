#%%
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

#%%
# Load up classic Titanic dataset
titanic=pd.read_csv('data/train.csv')
# For simplification, we will build a LogReg model using only 2 features
# Use Age and Fare to predict Survived
df=titanic[['Survived','Fare','Age']].dropna()

#%%
X=df[['Fare','Age']]
y=df[['Survived']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=22)

#%%
# Train the model and predictor
classifier = LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)
#%%
# Example: Given inputs 27.0 and 34, what probability does the model predict for class 0?
print(classifier.predict_proba([[27.0,34]])[:,0])
# [0.64389339]
#%%
# Save the model as a pickle file
pickle.dump(classifier, open('model.pickle', 'wb'))


#%%
