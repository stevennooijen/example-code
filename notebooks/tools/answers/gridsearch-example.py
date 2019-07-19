# Import sklearn dependencies
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

# specify to be searched parameter grid
param_grid = {'n_estimators': [10, 50, 100, 200],
              'max_depth': [3,5,7,9]}
params_list = create_param_grid_list(param_grid)

# run the hyperparameter search
for params in params_list:
    
    with mlflow.start_run(run_name='RandomForestClassifier'):
        
        # create a model with specific hyperparameters
        model = RandomForestClassifier(**params)
        
        # fit and score your model
        cv_scores = cross_val_score(model, X_train, y_train, cv=5)

        # log parameters
        mlflow.log_param("n_estimators", params['n_estimators'])
        mlflow.log_param("max_depth", params['max_depth'])
        mlflow.log_param("cv", 5)
        # log metrics
        mlflow.log_metric("cv_accuracy_mean", cv_scores.mean())
        mlflow.log_metric("cv_accuracy_std", cv_scores.std())

        # possibly log mogel
#         mlflow.sklearn.log_model(model, "model")
