import streamlit as st

st.set_page_config(
    page_title="FAQ"
)

st.write("# FAQ 🧑🏽‍🍳")

with st.expander("What is **PlateMate**?"):
    st.write("""
        **PlateMate** is your personal recipe genie! It's like having a food-loving friend who knows all the best recipes! 
        Sometimes you crave for something you don't know until you see and try! **PlateMate** shows you recipes and learns 
        from your choices and refines its recommendations. It scans through a treasure trove of recipes and 
        compares your preferences with other recipes to continuously suggest you a new recipe to try! 
         
        Let the food exploration begin! Bon appétit! 🌮🍕🍣

        **PlateMate** is open source and the repo can be found here: \n
         https://github.com/AghilZadeh/PlateMate

    """)

with st.expander("Where does the data come from?"):
    st.write("""
        The data on this website consists of a comprehensive collection of recipes and reviews. 
        These datasets were obtained by scraping information from [food.com](www.food.com) and cover the period from 1999 to 2020. 
        The recipes dataset encompasses approximately 500,000 recipes across 312 different categories. 
        It provides detailed information about each recipe, including cooking times, servings, ingredients, nutrition facts, instructions, and more.

        The reviews dataset, on the other hand, comprises around 1,400,000 reviews contributed by approximately 270,000 distinct users. 
        This dataset offers valuable insights into the authorship, ratings, review text, and additional information. 
        These reviews play a significant role in the development of our recommender system model.

    """)

with st.expander("What type of model is being used?"):
    st.write("""
        The recommender model on this website is based on a matrix factorization technique. 
        It utilizes the scikit-surprise library, a powerful tool for building recommendation systems. 
        By employing matrix factorization, the model can extract meaningful patterns and relationships from the dataset. 
        The recommender model is trained using our dataset, which includes a collection of recipes and reviews. 
        Additionally, the model takes into account the preferences expressed by the user. 
        By incorporating these preferences, the model can personalize recommendations based on individual tastes and interests. 
    """)

with st.expander("Download dataset"):
    st.write("""
        All data is accessible through an AWS S3 link. It contains all reviews ([reviews.csv](https://foodcom.s3.us-east-2.amazonaws.com/reviews.csv)) 
        and all recipes ([recipes.csv](https://foodcom.s3.us-east-2.amazonaws.com/recipes.csv)).
        Reviews are split into train ([reviews_train.csv](https://foodcom.s3.us-east-2.amazonaws.com/reviews_train.csv]) 
        and test ([reviews_test.csv](https://foodcom.s3.us-east-2.amazonaws.com/reviews_test.csv)) sets by 9 to 1 ratio. 
        The test and train sets contain disjoint users. A portion of recipes that are highly rated and famous are selected 
        ([recipes_selected.csv](https://foodcom.s3.us-east-2.amazonaws.com/recipes_selected.csv) to be used in the recommender system. 
    """)