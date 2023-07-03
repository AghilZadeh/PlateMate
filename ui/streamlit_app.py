import streamlit as st
import pandas as pd
import random
import re


# Function to render a recipe profile
def render_recipe(ind, recipes):
    st.write("##")
    st.image(recipes.loc[ind, 'Image'], width=400)
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
    st.write("# Welcome to Test Your Taste! 🧑🏽‍🍳")
    #st.sidebar.success("Select a demo above.")
    st.markdown("""
        #### Tell me what you like, I will recommend you recipes to try!
    """)

    # setting session state
    if 'recipes_notshown' not in st.session_state:
        # Getting recipe data
        cols = ['RecipeId', 'Name', 'Description', 'Image', 'RecipeCategory', 'Keywords',
       'AggregatedRating', 'ReviewCount', 'RecipeInstructions']
        recipes = pd.read_csv('./data/recipes_selected.csv', usecols=cols)

        # initializing session states
        st.session_state['recipes_df'] = recipes
        st.session_state['recipes_notshown'] = recipes.index.to_list()
        st.session_state['recipes_shown'] = []
        st.session_state['recipes_liked'] = []
        st.session_state['recipes_disliked'] = []
    

    # choosing a recipe to show
    rand_ind = random.choice(st.session_state['recipes_notshown'])
    st.session_state['recipes_shown'].append(rand_ind)
    st.session_state['recipes_notshown'].remove(rand_ind)
    render_recipe(rand_ind, st.session_state['recipes_df'])
    col1, col2 = st.columns(2)
    with col1:
        b1 = st.button("😒 Dislike")
        st.session_state['recipes_disliked'].append(rand_ind)
    with col2:
        if st.button("🤤 Like "): 
            st.session_state['recipes_liked'].append(rand_ind)
            print(st.session_state['recipes_liked'])
    with st.expander("Recipe Details"):
        render_details(rand_ind, st.session_state['recipes_df'])

    st.write(st.session_state['recipes_liked'])


if __name__ == '__main__':
    main()