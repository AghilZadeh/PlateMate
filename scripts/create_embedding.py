import pandas as pd
import openai
import time
import json



def get_embedding(text:str, embedding_model) -> list:
    while True:
        try:
            response = openai.Embedding.create(input=text, model=embedding_model)['data'][0]['embedding']
            if len(response)>0:
                break
            else:
                continue
        except openai.error.OpenAIError as e:
            print(f"OpenAIError: {e}.")
            time.sleep(2)
    return response


if __name__=='__main__':

    # load & inspect dataset
    input_datapath = "./data/recipes_selected.csv"  # to save space, we provide a pre-filtered dataset
    cols = ['RecipeId', 'Name', 'Description', 'Image', 'RecipeCategory', 'Keywords',
       'AggregatedRating', 'ReviewCount', 'RecipeInstructions']
    df = pd.read_csv(input_datapath, index_col='RecipeId', usecols=cols)

    # create embedding using OpenAI API
    ## setting credentials
    with open('./credentials/api_key.txt', 'r') as f:
        api = f.readline().strip()
    openai.api_key = api
    ## embedding model parameters
    embedding_model = "text-embedding-ada-002"
    embedding_encoding = "cl100k_base"  # this the encoding for text-embedding-ada-002
    ## extracting embedding
    emb_dict = {}
    for ind in df.index:
        emb_dict[ind] = get_embedding(df.loc[ind, 'Keywords'], embedding_model)

    with open('./data/embedding.json', 'w') as f:
        json.dump(emb_dict, f, indent=4)
        print('JSON file saved!')
