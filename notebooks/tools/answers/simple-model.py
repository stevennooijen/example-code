# Import sklearn dependencies
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score

# create a model
model = LogisticRegression(solver='liblinear', penalty='l1')

# fit, run, and/or score your model
cv_scores = cross_val_score(model, X_train, y_train, cv=5)

# print the metrics that you are interested in
print('cv_mean', cv_scores.mean())
print('cv_mean', cv_scores.std())
