import re
import os
import nltk
import json
import spacy
import pickle
import string
import time
import logging
import numpy as np
import streamlit as st
import seaborn as sns
import networkx as nx
import pandas as pd
from tqdm import tqdm
from spacy import displacy
import plotly.express as px
from pyvis.network import Network
import matplotlib.pyplot as plt
from nltk import word_tokenize
from nltk.corpus import stopwords 
import streamlit.components.v1 as components
import community.community_louvain as community_louvain

def character_evolution(character_list):
    index = ['Philosopher\'s Stone',
             'Chamber of Secrets',
             'Prisoner of Azkaban',
             'Goblet of Fire',
             'Order of the Phoenix',
             'Half-Blood Prince',
             'Deathly Hallows']
    
    df = pd.read_csv('character_evolution.csv')
    df = df.set_index(pd.Index(index))
    
    fig = px.line(df[character_list], markers=True) 
    fig.update_layout(height=550,
                      width=1000, 
                      xaxis_title="",
                      yaxis_title="Importance",
                      title={'text': "Evolution of Characters over the Books",
                             'y': 0.95,
                             'x': 0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'})
    left, middle, right = st.columns((2, 5, 2))
    with middle:
        st.plotly_chart(fig, theme=None, use_container_width=False)




