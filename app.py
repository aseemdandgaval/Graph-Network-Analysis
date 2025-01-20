import pandas as pd
import streamlit as st
import plotly.express as px
import streamlit.components.v1 as components


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


def main():
    df = pd.read_csv('character_evolution.csv')
    
    st.set_page_config(layout="wide")
    st.title("Relationship Extraction in Harry Potter Books")
    st.write('')
    st.write('')
    
    # Select Type of Analysis
    tab1, tab2 = st.tabs(['Network Graphs',
                          'Evolution of Characters'
                        ])
    
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
                HtmlFile = open(f'graphs/{book}.html', 'r', encoding='utf-8')
                components.html(HtmlFile.read(), height=1500, width=1000)

    # Evolution of Characters
    with tab2:
        st.write('')
        character_list = st.multiselect('Select Characters', list(df.columns)[1:])
        if st.button('Plot'):
            st.write('')
            character_evolution(character_list)
        

if __name__ == '__main__':
    main()