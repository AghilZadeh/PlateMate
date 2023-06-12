import streamlit as st
import pandas as pd
import re
import sys
import random

# Getting recipe data
cols = ['RecipeId', 'Name', 'Description', 'Image', 'RecipeCategory', 'Keywords',
       'AggregatedRating', 'ReviewCount', 'RecipeInstructions']
recipes = pd.read_csv('./data/recipes_selected.csv', usecols=cols)

# Function to render a recipe profile
def render_recipe(ind):
    st.image(recipes.loc[ind, 'Image'], width=300)
    st.write(f"**{recipes.loc[ind, 'Name']}**")
    desc = recipes.loc[ind, 'Description']
    if len(desc)>100:
        st.write(desc[:100], '...')
    else:
        st.write(desc)

# Main Streamlit app
def main():

    # index list of recipes shown to or hidden from the user
    recipes_hidden = recipes.index.to_list() 
    recipes_shown = []
    
    st.set_page_config(
    page_title="Home",
    page_icon="🧑🏽‍🍳",
    )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write("# Welcome to Test Your Taste! 🧑🏽‍🍳")
    #st.sidebar.success("Select a demo above.")
    st.markdown(
        """
        #### Tell me what you like, I will recommend you recipes to try!
    """
    )

    cols_1 = st.columns(2)
    cols_2 = st.columns(2)
    cols = cols_1 + cols_2
      
    for i in range(len(cols)):

        # choosing a recipe to show
        rand_ind = random.choice(recipes_hidden)
        recipes_shown.append(rand_ind)
        recipes_hidden.remove(rand_ind)
        with cols[i]:
            render_recipe(rand_ind)
            st.button("Like", key=i)
            
        
        

if __name__ == '__main__':
    main()