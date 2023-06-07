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
models = [BaselineOnly, SVD, SVDpp, NMF, SlopeOne, KNNBaseline, KNNWithZScore, KNNWithMeans, CoClustering]
model_names = ['BaselineOnly', 'SVD', 'SVDpp', 'NMF', 'SlopeOne', 'KNNBaseline', 'KNNWithZScore', 'KNNWithMeans', 'CoClustering']
model_params = [{},
                {'n_factors':100, 'n_epochs':20},
                {'n_factors':20, 'n_epochs':20},
                {'n_factors':15, 'n_epochs':50},
                {},
                {'k':40},
                {'k':40},
                {'k':40},
                {'n_cltr_u':20, 'n_cltr_i':20, 'n_epochs':20}
                ]
data_params = {'n_data':10000}

# reading data
reviews_train = pd.read_csv('./data/reviews_train.csv', usecols=['RecipeId', 'AuthorId', 'Rating'])
reader = Reader(rating_scale=(1, 5))
trainset = Dataset.load_from_df(reviews_train.loc[:data_params['n_data'], ["AuthorId", "RecipeId", "Rating"]], reader)

# experiments
for model, name, params in zip(models, model_names, model_params):
                      
    with mlflow.start_run(experiment_id = experiment.experiment_id):
        # model
        mod = model(**params)
    
        # fit model
        results = cross_validate(mod, trainset, measures=['RMSE', 'MAE'], cv=5, verbose=True);
    
        #log model params
        mlflow.log_params(params)
        mlflow.log_params(data_params)
        mlflow.log_metrics({"rmse": results['test_rmse'].mean(), "mae": results['test_mae'].mean()})
        # log model (will save as pickle file)
        mlflow.sklearn.log_model(model, artifact_path = "mod")