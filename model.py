import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

chatterbox = pd.read_csv("Train_Dataset_190525X.csv")

chatterbox = chatterbox.replace({'Churn': {'Yes': 1, 'No': 0}})
chatterbox = chatterbox.replace({'yes': 1, 'no': 0})

#upsampling
train_no = chatterbox[chatterbox.Churn == 0]
train_yes = chatterbox[chatterbox.Churn == 1]
train_yes_upsampled = train_yes.sample(n=len(train_no), replace=True, random_state=42)
print(len(train_yes_upsampled))
train_upsampled = train_no.append(train_yes_upsampled).reset_index(drop=True)

xtrain = train_upsampled.drop(['Churn', 'customer_id'], axis=1)
ytrain = train_upsampled['Churn']

# clf = RandomForestClassifier(n_estimators = 15, random_state = 0)
clf = RandomForestClassifier(bootstrap=False, max_depth=40, n_estimators=1400)
clf.fit(xtrain, ytrain)

joblib.dump(clf, "clf.pkl")
