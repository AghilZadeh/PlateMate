import json
import numpy as np
from sklearn.decomposition import TruncatedSVD, PCA

#model = TruncatedSVD(n_components=100, n_iter=7) # 100 compnents explain ~95% of variance
model = PCA(n_components=300)

# read data
with open('./data/embedding_v2.json', 'r') as f:
    embedding = json.load(f)
    print('JSON file loaded!')

# create numpy array using dict data
emb_keys = list(embedding.keys())
emb_array = np.array([embedding[k] for k in emb_keys])

# remove loaded json to free memory
del embedding

# creating svd transformation
model.fit(emb_array)
print('Explained variance:', model.explained_variance_ratio_.sum())
print('Singular values:', model.singular_values_)

# transforming data
emb_transformed = model.transform(emb_array)

# saving short embedding
emb_short = {}
for ind, row in enumerate(emb_transformed):
    emb_short[emb_keys[ind]] = list(row)
with open('./data/embedding_v2.3_short.json', 'w') as f:
    json.dump(emb_short, f, indent=4)
    print('JSON file saved!')