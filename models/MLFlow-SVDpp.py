from sklearn.model_selection import cross_validate
import mlflow
import mlflow.sklearn
import pandas as pd
from surprise import Dataset, Reader, SVD, SVDpp, NMF, SlopeOne, KNNBaseline, KNNWithZScore, KNNWithMeans, BaselineOnly, CoClustering
from surprise.model_selection import cross_validate, train_test_split


experiment_name = 'Aghil-dsml-project-food'  
tracking_uri = 'http://18.237.76.205/'
# Set path to log
mlflow.set_tracking_uri(tracking_uri)
#set experiment
mlflow.set_experiment(experiment_name = experiment_name) 
experiment = mlflow.get_experiment_by_name(experiment_name)  

# models
model = SVDpp
model_name = 'SVDpp'
model_params = {'n_factors':[5, 10, 20, 50, 100], 'n_epochs':[5, 10, 20, 50, 100]}
#model_params = {'n_factors':[5], 'n_epochs':[5]}
#data_params = {'n_data':[1000, 5000, 10000, 50000, 100000]}
data_params = {'n_data':[100000]}

# reading data
reviews_train = pd.read_csv('./data/reviews_train.csv', usecols=['RecipeId', 'AuthorId', 'Rating'])
reader = Reader(rating_scale=(1, 5))

# experiments
for n_factors in model_params['n_factors']:
    for n_epochs in model_params['n_epochs']:
        for n_data in data_params['n_data']:

            params = {'n_factors':n_factors, 'n_epochs':n_epochs}
            trainset = Dataset.load_from_df(reviews_train.loc[:n_data, ["AuthorId", "RecipeId", "Rating"]], reader)
                      
            with mlflow.start_run(experiment_id = experiment.experiment_id):
                # model
                mod = model(**params)
            
                # fit model
                results = cross_validate(mod, trainset, measures=['RMSE', 'MAE'], cv=5, verbose=True);
            
                #log model params
                mlflow.log_params(params)
                mlflow.log_param('n_data', n_data)
                mlflow.log_param('model_name', model_name)
                mlflow.log_metrics({"rmse": results['test_rmse'].mean(), "mae": results['test_mae'].mean()})
                # log model (will save as pickle file)
                mlflow.sklearn.log_model(model, artifact_path = "mod")
                