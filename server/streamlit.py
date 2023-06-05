import streamlit as st
from funcs import find_url
import pandas as pd
import re
#from surprise import SVD
import sys

st.set_page_config(
    page_title="Home",
    page_icon="🧑🏽‍🍳",
)
st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

st.write("# Welcome to Test Your Taste! 🧑🏽‍🍳")
print(sys.path)

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Tell me about what you like, I will recommend you recipes to try!
"""
)

recipes = pd.read_csv('./data/recipes.csv', usecols=['RecipeId', 'Name', 'Images'], nrows=15)
recipes['Images'] = list(map(find_url, recipes['Images']))
n_recipes = 10
choices = range(1,6)
selection = [0]*n_recipes
for i in range(n_recipes):
    selection[i] = st.radio(recipes['Name'][i], choices, index=2)
    st.image(recipes['Images'][i], width=200)
    st.text('')

if st.button('submit'):
    df_new = pd.DataFrame({'user':['new']*n_recipes, 'item':recipes['RecipeId'][:n_recipes], 'Rating': selection})
    #print(df_new)















# #urls = pd.read_csv('../data/recipes.csv', usecols=['Images'], nrows=10).values.flatten()
# #imgs = list(map(find_url, urls))
# imgs = [
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/45809/AELeDrJmT1aPk0ADFr6d_10101046640053887.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/2886/xeKul9ZdTxKTXs3IGs16_20170323_193853.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/27208/rtdzvMzETmOyHx89FbaN_5AECF2F4-AE9E-4245-8948-FC9C7527C8DF.jpeg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/89204/eOEFikGTxil0TC3K3tGr_image.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/39087/WHnfAAGES8qMRC5hA4sw_IMG_20170417_052205224_HDR-7000x3937.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/35813/tDxRW7TeQsKEbvZ6MTjl_IMG_1468.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/67256/2jCcfG4AT667ziyZo924_20190421_174125.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/54257/xELVM3QvQuCK5oNcuAJ9_IMG_20170212_212029.jpg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/22782/RSS2jqMfQeu2FGvMkuyg_20170806_182816-01.jpeg',
#  'https://img.sndimg.com/food/image/upload/v1/img/feed/32204/PZG96oOQDCIJ4DyeH5Mc_91FD65B7-FB99-4CC2-83BC-A8FBBF991977.jpeg']

# image_iterator = paginator("What do you like?", imgs)
# indices_on_page, images_on_page = map(list, zip(*image_iterator))
# st.image(images_on_page, width=100, caption=indices_on_page)