# PlateMate (A recipe recommender system)

## Overview:

**PlateMate** is your personal recipe genie! It's like having a food-loving friend who knows all the best recipes! 
        Sometimes you crave for something you don't know until you see and try! **PlateMate** shows you recipes and learns 
        from your choices and refines its recommendations. It scans through a treasure trove of recipes and 
        compares your preferences with other recipes to continuously suggest you a new recipe to try! 

<img src="https://github.com/AghilZadeh/PlateMate/assets/35585082/6ec38c05-81cd-4cc3-b58e-64ca70d21a5e" alt="drawing" width="300"/>

         
Let the food exploration begin! Bon appétit! 🌮🍕🍣

## Data:

The data this project consists of a comprehensive collection of recipes and reviews. 
These datasets were obtained by scraping information from [food.com](www.food.com) available on [Kaggle](https://www.kaggle.com/datasets/irkaal/foodcom-recipes-and-reviews)  and cover the period from 1999 to 2020. 
The recipes dataset encompasses approximately 500,000 recipes across 312 different categories. 
It provides detailed information about each recipe, including cooking times, servings, ingredients, nutrition facts, instructions, and more.

The reviews dataset, on the other hand, comprises around 1,400,000 reviews contributed by approximately 270,000 distinct users. 
This dataset offers valuable insights into the authorship, ratings, review text, and additional information. 
These reviews play a significant role in the development of our recommender system model.

All data is accessible through an AWS S3 link. It contains all reviews ([reviews.csv](https://foodcom.s3.us-east-2.amazonaws.com/reviews.csv)) and all recipes ([recipes.csv](https://foodcom.s3.us-east-2.amazonaws.com/recipes.csv)).
Reviews are split into train ([reviews_train.csv](https://foodcom.s3.us-east-2.amazonaws.com/reviews_train.csv)) and test ([reviews_test.csv](https://foodcom.s3.us-east-2.amazonaws.com/reviews_test.csv)) sets by 9 to 1 ratio. The test and train sets contain disjoint users.
A portion of recipes that are highly rated and famous are selected ([recipes_selected.csv](https://foodcom.s3.us-east-2.amazonaws.com/recipes_selected.csv)) to be used in the recommender system. The selection criteria can be seen [in this notebook](./notebooks/data_cleaning.ipynb).

The data used in the modelings are only reviews_train.csv and recipes_selected.csv and can be downloaded using the script in the Usage Instruction.

## Methods:

The recommender model on this website is based on two different algorithms:

1. A collaborative filtering aproach using a matrix factorization technique: 
It utilizes the [scikit-surprise library](https://surpriselib.com/), a powerful tool for building recommendation systems. 
By employing matrix factorization, the model can extract meaningful patterns and relationships from the dataset. 
The recommender model is trained using our dataset, which includes a collection of recipes and reviews. 
Additionally, the model takes into account the preferences expressed by the user. 
By incorporating these preferences, the model can personalize recommendations based on individual tastes and interests.

2. A content-based approach using keywords and instructions of recipes: Recipes are mapped to a vector embedding space. The embedding space is constructed by feeding the recipe keywords and instructions to OpenAI second generation text-embedding-ada-002 model API. Users embedding is calculated by mean vector of their liked recipes. At each step, a similarity score is calculated by cosine similarity of user and recipes. The next recipe is drawn randomly using probabilities calculated by SoftMax of similarity scores with temperature. The temperature decreases as the number of clicks increases to address the cold start problem. To improve speed and efficiency, the embedding dimensionality is reduced resulting in 15-fold improvement in memory and speed.

<img src="https://github.com/AghilZadeh/PlateMate/assets/35585082/d0acdf3b-2f33-45a7-964e-4ced3582dab1" alt="drawing" width="600"/>


## Results:

The utilized model for this project is [SVD++](https://surprise.readthedocs.io/en/stable/matrix_factorization.html) from scikit-surprise. The model was evaluated using cross-validation on the training set. It scores better than other collaborative filtering methods of scikit-surprise such as KNN or clustering methods.

<img src="https://github.com/AghilZadeh/PlateMate/assets/35585082/caf2b81f-ec4f-4bd1-a9ef-cb5b8165ef54" alt="drawing" width="300"/>



## Usage Instruction:

The app can be found online at https://platemate.streamlit.app/

Additionally, you can use the app in just a few steps locally:
1. clone the repository in your local machine and install requirements
    ```js
    git clone https://github.com/AghilZadeh/dsml-fullstack-food-recommender/
    pip install -r requirements.txt
    ```
3. download the neccessary data:
    ```js
    wget -O ./data/reviews_train.csv https://foodcom.s3.us-east-2.amazonaws.com/reviews_train.csv
    wget -O ./data/recipes_selected.csv https://foodcom.s3.us-east-2.amazonaws.com/recipes_selected.csv
    ```
4. run streamlit app locally using the command below:
    ```js
    streamlit run ./ui/PlateMate.py
    ```



