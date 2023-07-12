import streamlit as st
import pandas as pd
import re
from utils import *


# Main Streamlit app
def main():

    # page details
    st.set_page_config(
    page_title="PlateMate",
    page_icon="🧑🏽‍🍳",
    initial_sidebar_state="collapsed",
    )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write("# PlateMate 🧑🏽‍🍳")
    #st.sidebar.success("Select a demo above.")
    st.markdown("""
        #### Tap Your Way to Deliciousness! \n #
    """)

    # setting session state
    if 'recipes_notshown' not in st.session_state:
        # Getting recipe data
        cols = ['RecipeId', 'Name', 'Description', 'Image', 'RecipeCategory', 'Keywords',
       'AggregatedRating', 'ReviewCount', 'RecipeInstructions', 'AuthorName']
        df_recipes = pd.read_csv('./data/recipes_selected_summarized.csv', usecols=cols, index_col='RecipeId')
        (recipes_indices, emb_array) = load_embedding()

        # initializing session states
        st.session_state['recipes_df'] = df_recipes
        st.session_state['recipes_notshown'] = df_recipes.index.tolist()
        st.session_state['recipes_liked'] = []
        st.session_state['recipes_disliked'] = []
        st.session_state['recipes_embeddings'] = emb_array
        st.session_state['user_emb'] = np.zeros(emb_array.shape[1]) # setting initial
        st.session_state['model_temp'] = 1 # setting model tempreture 
        
    # choosing a recipe to show
    query = st.session_state['user_emb']/(len(st.session_state['recipes_liked'])+1)
    # setting tempreture such that at first it shows recipes more randomly
    tempreture = np.exp(-len(st.session_state['recipes_liked'])/5) + 0.01
    recipe_ind  = draw_ind(query, st.session_state['recipes_notshown'], st.session_state['recipes_embeddings'], t=0.01)
    
    # changing state variables
    row_ind = np.where(st.session_state['recipes_notshown']==recipe_ind)
    recipe_emb = st.session_state['recipes_embeddings'][row_ind].reshape(-1)
    st.session_state['recipes_embeddings'] = np.delete(st.session_state['recipes_embeddings'], row_ind, 0)
    st.session_state['recipes_notshown'].remove(recipe_ind)
    
    # showing recipe
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🙄 Meh!"):
            st.session_state['recipes_disliked'].append(recipe_ind)
    with col2:
        if st.button("😋 Tasty!"): 
            st.session_state['recipes_liked'].append(recipe_ind)
            st.session_state['user_emb'] += recipe_emb
    
    col_rec1, col_rec2 = st.columns(2)
    
    with col_rec1:
        render_recipe(recipe_ind, st.session_state['recipes_df'])
    with st.expander("Recipe Details"):
        render_details(recipe_ind, st.session_state['recipes_df'])


if __name__ == '__main__':
    main()