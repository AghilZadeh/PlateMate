import streamlit as st
import pandas as pd
import re
from utils import *


# Function to render a recipe profile
def render_recipe(ind, recipes):
    st.write("##")
    st.image(recipes.loc[ind, 'Image'], height=400)
    st.write(f"**{recipes.loc[ind, 'Name']}**")
    # desc = recipes.loc[ind, 'Description']
    # if len(desc)>100:
    #     st.write(desc[:100], '...')
    # else:
    #     st.write(desc)

def render_details(ind, recipes):
    st.write(f"**Description:** {recipes.loc[ind, 'Description']}")
    st.write(f"**Category:** {recipes.loc[ind, 'RecipeCategory']}")
    st.write(f"**Rating:** {recipes.loc[ind, 'AggregatedRating']}")
    inst = ' '.join(str2list(recipes.loc[ind, 'RecipeInstructions']))
    st.write(f"**Instruction:**  {inst}")


def str2list(s: str) -> list:
    'returns a list of strings breaking the original string by "" '
    return re.findall(r'"(.*?)"', s)

# Main Streamlit app
def main():

    # page details
    st.set_page_config(
    page_title="Home",
    page_icon="🧑🏽‍🍳"
    )
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    st.write("# PlateMate 🧑🏽‍🍳")
    #st.sidebar.success("Select a demo above.")
    st.markdown("""
        #### Swipe Your Way to Deliciousness!
    """)

    # setting session state
    if 'recipes_notshown' not in st.session_state:
        # Getting recipe data
        cols = ['RecipeId', 'Name', 'Description', 'Image', 'RecipeCategory', 'Keywords',
       'AggregatedRating', 'ReviewCount', 'RecipeInstructions']
        df_recipes = pd.read_csv('./data/recipes_selected_summarized.csv', usecols=cols, index_col='RecipeId')
        (recipes_indices, emb_array) = load_embedding()

        # initializing session states
        st.session_state['recipes_df'] = df_recipes
        st.session_state['recipes_notshown'] = recipes_indices
        st.session_state['recipes_liked'] = []
        st.session_state['recipes_disliked'] = []
        st.session_state['recipes_embeddings'] = emb_array
        st.session_state['user_emb'] = np.zeros(emb_array.shape[1]) # setting initial 
        
    # choosing a recipe to show
    query = st.session_state['user_emb']/(len(st.session_state['recipes_liked'])+1)
    recipe_ind  = draw_ind(query, st.session_state['recipes_notshown'], st.session_state['recipes_embeddings'], t=0.1)
    
    # changing state variables
    row_ind = np.where(st.session_state['recipes_notshown']==recipe_ind)
    recipe_emb = st.session_state['recipes_embeddings'][row_ind].reshape(-1)
    st.session_state['recipes_embeddings'] = np.delete(st.session_state['recipes_embeddings'], row_ind, 0)
    st.session_state['recipes_notshown'].remove(recipe_ind)
    
    # showing recipe
    render_recipe(recipe_ind, st.session_state['recipes_df'])
    col1, col2 = st.columns(2)
    with col1:
        if st.button("😒 Dislike"):
            st.session_state['recipes_disliked'].append(recipe_ind)
    with col2:
        if st.button("🤤 Like "): 
            st.session_state['recipes_liked'].append(recipe_ind)
            st.session_state['user_emb'] += recipe_emb
    with st.expander("Recipe Details"):
        render_details(recipe_ind, st.session_state['recipes_df'])


if __name__ == '__main__':
    main()