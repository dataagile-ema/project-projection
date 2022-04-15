from faulthandler import disable
import streamlit as st
from PIL import Image
from itertools import compress

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame()



def str2num(s):
    try:
        return float(s.replace(",", "."))
    except ValueError:
        st.write("Måste vara ett tal")
        return np.nan
        

# sida
im = Image.open("favicon.ico")
st.set_page_config(page_title="Project projection", page_icon=im)
"""
# Project projection
"""

left, right = st.columns(2)
with left:

    min_for_story = str2num(st.text_input("Min för en User Story", value="5", key="text"))
    no_of_stories = str2num(st.text_input("Antal User Stories", value="10", key="text"))    
with right:
    max_for_story = str2num(st.text_input("Max för en User Story", value="15", key="text"))
    share_rework = str2num(st.text_input("Procent av User Stories som är Rework", value="10", key="text"))


#st.write(no_of_stories, min_for_story, max_for_story)


def calc_uniform_simulation(no_of_stories, min_for_story, max_for_story):
    return np.sum(np.random.uniform(min_for_story, max_for_story, int(no_of_stories)))

if no_of_stories > 0.0 and min_for_story > 0.0 and max_for_story > 0.0:
    np.random.seed(42)



    df["value"] = [calc_uniform_simulation(int(no_of_stories), min_for_story, max_for_story) for i in range(5000)]

        


    plt.style.use('ggplot')

    fig, ax = plt.subplots()

    # dist plot without label for 'value'
    ax.hist(df["value"], bins=20, density=True, alpha=0.5)
    #df.plot.kde(ax=ax, legend=False, label="")

    ax.set_xlim(0, max_for_story*no_of_stories)


    # calc 85th percentile
    p85th = df.value.quantile(0.85)
    p50th = df.value.quantile(0.5)

    ax.axvline(p85th, color='g', linestyle='--', label=f'85th percentile: {round(p85th,0)}')

    ax.axvline(p50th, color='b', linestyle='--', label=f'50th percentile: {round(p50th,0)}')



    ax.legend(loc='upper left')

    # set height of plot
    fig.set_size_inches(10, 5)

    st.pyplot(fig)




 






