import json
import numpy as np
import re
import pandas as pd
import streamlit as st


# Function to render a recipe profile
def render_recipe(ind, recipes):
    st.write(f"**{recipes.loc[ind, 'Name']}**")
    st.image(recipes.loc[ind, 'Image'], width=315)
    # desc = recipes.loc[ind, 'Description']
    # if len(desc)>100:
    #     st.write(desc[:100], '...')
    # else:
    #     st.write(desc)

def render_details(ind, recipes):
    
    st.write(f"{recipes.loc[ind, 'Description']}")
    inst = ' '.join(str2list(recipes.loc[ind, 'RecipeInstructions']))
    st.write(f"**Instruction:**  {inst}")
    st.write(f"**Rating:** {recipes.loc[ind, 'AggregatedRating']}")
    st.write(f"**Author:** {recipes.loc[ind, 'AuthorName']}")
    

def str2list(s: str) -> list:
    'returns a list of strings breaking the original string by "" '
    return re.findall(r'"(.*?)"', s)

def load_embedding(path='./data/embedding_v1.2_short.json'):
    'loads the embedding data base into a numpy array and returns the indices and embedding numpy array'
    with open(path, 'r') as f:
        embedding = json.load(f)    
    emb_keys = list(map(int, embedding.keys()))
    emb_array = np.array([embedding[str(k)] for k in emb_keys])
    return(emb_keys, emb_array)

def calc_similarity(query, emb_array):
    'given a query embedding, calculates the similarity of query with all emb_array rows'
    sim_vec = np.dot(query, emb_array.T)
    return sim_vec
    
def select_ind(indices, sim_vec, t=1):
    'selects an index randomly based on softmax probablities of sim_vec, t is tempreture'
    prob = np.exp(sim_vec/t)/sum(np.exp(sim_vec/t))
    ind = np.random.choice(indices, p=prob)
    return ind

def draw_ind(query, indices, emb_array, t=1):
    sim_vec = calc_similarity(query, emb_array)
    ind = select_ind(indices, sim_vec, t)
    return ind


if __name__=='__main__':
    (indices, emd_array) = load_embedding()
    sim_arr  = calc_similarity(emd_array[0], emd_array)
    print(sorted(sim_arr, reverse=True)[7000:7100])
    