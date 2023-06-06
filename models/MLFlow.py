import os
import numpy as np
from scipy.stats import uniform
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn import metrics
from sklearn.model_selection import ParameterSampler
from sklearn.ensemble import RandomForestClassifier
import mlflow
import mlflow.sklearn
import pandas as pd
from matplotlib import pyplot as plt 
import numpy as np
from surprise import Dataset, Reader, KNNWithMeans, SVD, accuracy
from surprise.model_selection import cross_validate, train_test_split


experiment_name = 'Aghil-surprise-SVD'  
tracking_uri = 'http://18.237.76.205/'  # this will be provided for you

# Set path to log
mlflow.set_tracking_uri(tracking_uri)

#set experiment
mlflow.set_experiment(experiment_name = experiment_name) 
experiment = mlflow.get_experiment_by_name(experiment_name)
run_hyperparams = {'n_factors':100, 'n_epochs':20, 'n_data':10000}

# reading data
reviews_train = pd.read_csv('./data/reviews_train.csv', usecols=['RecipeId', 'AuthorId', 'Rating'])
reader = Reader(rating_scale=(1, 5))
trainset = Dataset.load_from_df(reviews_train.loc[:run_hyperparams['n_data'], ["AuthorId", "RecipeId", "Rating"]], reader)


                   
with mlflow.start_run(experiment_id = experiment.experiment_id):
   
    # model
    svd = SVD(n_factors = run_hyperparams['n_factors'], 
                n_epochs = run_hyperparams['n_epochs'])
    
    # fit model
    results = cross_validate(svd, trainset, measures=['RMSE', 'MAE'], cv=5, verbose=True);
    
    #log model params
    mlflow.log_params(run_hyperparams)

    # log model params
    mlflow.log_metrics({"rmse": results['test_rmse'].mean(), "mae": results['test_mae'].mean()})

    # log model (will save as pickle file)
    mlflow.sklearn.log_model(svd, artifact_path = "mod")