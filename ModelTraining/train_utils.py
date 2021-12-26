import pandas as pd
from imblearn.combine import SMOTEENN
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RandomizedSearchCV, RepeatedStratifiedKFold

def transform(transformer,X,y):
    print("Transforming {}".format(transformer.__class__.__name__))
    X_resampled,y_resampled = transformer.fit_resample(X,y)
    return transformer.__class__.__name__,pd.DataFrame(X_resampled), pd.DataFrame(y_resampled)

def benchmark(sampling_type,X,y):
    rf = RandomForestClassifier()
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    param_grid = {"max_depth": range(10,100),
                  'n_estimators':[100,200,500,600,700]}
    rf_random = RandomizedSearchCV(estimator = rf, param_distributions=param_grid,scoring='roc_auc', cv = cv,random_state=1,n_jobs=-1,verbose=2)
    rf_random = rf_random.fit(X,y)
    #Store the best score:
    print("Tuned Random Forest parameters: {0}".format(rf_random.best_params_))
    print('Best estimator AUC score: {0}'.format(rf_random.best_score_))
    return sampling_type,rf_random.best_score_,rf_random.best_params_


