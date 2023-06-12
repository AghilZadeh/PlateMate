import streamlit as st
import re

def str2list(s: str) -> list:
    'returns a list of strings breaking the original string by "" '
    return re.findall(r'"(.*?)"', s)

def str2url(s: str) -> str:
    'returns a list of strings breaking the original string by "" '
    return re.search(r'"(.*?)"', s).group(0)[1:-1]
