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

from streamlit_utils import character_evolution

def main():
    df = pd.read_csv('character_evolution.csv')
    
    # Set Title
    st.set_page_config(layout="wide")
    st.title("Relationship Extraction in Harry Potter Books")
    st.write('')
    st.write('')
    
    # Select Type of Analysis
    tab1, tab2, tab3, tab4 = st.tabs(['Network Graphs',
                                 '  ',
                                 'Evolution of Characters',
                                 '  '])
    
    # Network Graphs
    with tab1:
        st.write('')
        book = st.selectbox('Pick a Book to generate its graph', 
                            ['1. Philosopher\'s Stone',
                             '2. Chamber of Secrets',
                             '3. Prisoner of Azkaban',
                             '4. Goblet of Fire',
                             '5. Order of the Phoenix',
                             '6. Half-Blood Prince',
                             '7. Deathly Hallows',
                             'All Books Combined'])
        
        if st.button('Show Graph'):
            left, middle, right = st.columns((1, 5, 1))
            with middle:
                st.write('') 
                HtmlFile = open(f'new_graphs/{book}.html', 'r', encoding='utf-8')
                components.html(HtmlFile.read(), height=750)

                
    # Compare Network Graphs   
    # with tab2:
    #     st.write("tab2")
        

    # Evolution of Characters
    with tab3:
        st.write('')
        character_list = st.multiselect('Select Characters', list(df.columns)[1:])
        if st.button('Plot'):
            st.write('')
            character_evolution(character_list)

            
    # Exploratory Data Analysis   
    # with tab4:
    #     st.write("tab4")

        
if __name__ == '__main__':
    main()