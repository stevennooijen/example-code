# create your favorite model
model = RandomForestClassifier(n_estimators=100 , max_depth=7)

# fit your model
model = model.fit(X_train, y_train)

# predict with your model
pred = model.predict(X_test)
