import streamlit as st
from funcs import paginator

st.set_page_config(
    page_title="Home",
    page_icon="🧑🏽‍🍳",
)

st.write("# Welcome to Test Your Taste! 🧑🏽‍🍳")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Tell me about what you like, I will recommend you recipes to try!
"""
)

sunset_imgs = [
    'https://unsplash.com/photos/-IMlv9Jlb24/download?force=true',
    'https://unsplash.com/photos/ESEnXckWlLY/download?force=true',
    'https://unsplash.com/photos/mOcdke2ZQoE/download?force=true',
    'https://unsplash.com/photos/GPPAjJicemU/download?force=true',
    'https://unsplash.com/photos/JFeOy62yjXk/download?force=true',
    'https://unsplash.com/photos/kEgJVDkQkbU/download?force=true',
    'https://unsplash.com/photos/i9Q9bc-WgfE/download?force=true',
    'https://unsplash.com/photos/tIL1v1jSoaY/download?force=true',
    'https://unsplash.com/photos/-G3rw6Y02D0/download?force=true',
    'https://unsplash.com/photos/xP_AGmeEa6s/download?force=true',
    'https://unsplash.com/photos/4iTVoGYY7bM/download?force=true',
    'https://unsplash.com/photos/mBQIfKlvowM/download?force=true',
    'https://unsplash.com/photos/A-11N8ItHZo/download?force=true',
    'https://unsplash.com/photos/kOqBCFsGTs8/download?force=true',
    'https://unsplash.com/photos/8DMuvdp-vso/download?force=true'
]
image_iterator = paginator("Select a sunset page", sunset_imgs)
indices_on_page, images_on_page = map(list, zip(*image_iterator))
st.image(images_on_page, width=100, caption=indices_on_page)