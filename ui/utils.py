import json
import numpy as np

def load_embedding(path='./data/embedding_v1_short.json'):
    'loads the embedding data base into a numpy array and returns the indices and embedding numpy array'
    with open(path, 'r') as f:
        embedding = json.load(f)    
    emb_keys = list(embedding.keys())
    emb_array = np.array([embedding[k] for k in emb_keys])
    return(emb_keys, emb_array)

def calc_similarity(query, emb_array):
    'given a query embedding, calculates the similarity of query with all emb_array rows'
    sim_vec = 0
    return sim_vec

def select_ind(indices, sim_vec, t=1):
    'selects an index randomly based on softmax probablities of sim_vec, t is tempreture'
    ind = 0
    return ind

if __name__=='__main__':
    (indices, emd_array) = load_embedding()
    print(indices)